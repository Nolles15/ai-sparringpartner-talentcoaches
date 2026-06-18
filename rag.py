"""
rag.py — de zoek-motor van de AI-sparringpartner.

Wat dit doet, in gewone taal:
1. Leest de documenten uit de map `kennisbank/` (de "boekenplank").
2. Knipt ze in kleine stukjes (ongeveer een alinea).
3. Zet de stukjes klaar om op betekenis te doorzoeken (via OpenAI-embeddings) en
   bewaart dat op schijf, zodat zoeken daarna snel is.
4. Geeft bij een vraag de best passende stukjes terug, met de bron erbij.

De UI (`app.py`) gebruikt alleen `bouw_index()`, `zoek()` en `index_status()`.
Deze motor staat los van de UI, zodat we de binnenkant later kunnen vervangen
(bijv. zoeken in de EU/op eigen computer) zonder de app te herbouwen.
"""

import hashlib
import json
from pathlib import Path

import numpy as np
from openai import OpenAI

KENNISBANK = Path(__file__).resolve().parent / "kennisbank"
INDEX_BESTAND = KENNISBANK / ".index.json"
EMBED_MODEL = "text-embedding-3-small"
STUKJE_TEKENS = 800  # streefgrootte van een stukje (in tekens)


# --- documenten inlezen ----------------------------------------------------

def _lees_bestand(pad: Path) -> str:
    """Haalt platte tekst uit een .md/.txt/.pdf-bestand."""
    if pad.suffix.lower() in (".md", ".txt"):
        return pad.read_text(encoding="utf-8", errors="ignore")
    if pad.suffix.lower() == ".pdf":
        from pypdf import PdfReader  # alleen importeren als er echt een PDF is
        try:
            reader = PdfReader(str(pad))
            return "\n\n".join((p.extract_text() or "") for p in reader.pages)
        except Exception:
            return ""
    return ""


def _lees_documenten():
    """Geeft een lijst van (bron, tekst) voor alle bruikbare documenten, ook in submappen."""
    if not KENNISBANK.exists():
        return []
    documenten = []
    for pad in sorted(KENNISBANK.rglob("*")):
        if not pad.is_file():
            continue
        if "__MACOSX" in pad.parts:           # Mac-zip-rommel overslaan
            continue
        if pad.name.startswith(".") or pad.name.lower() == "readme.md":
            continue
        if pad.suffix.lower() not in (".md", ".txt", ".pdf"):
            continue
        tekst = _lees_bestand(pad).strip()
        if tekst:
            bron = pad.relative_to(KENNISBANK).as_posix()  # bijv. pages/042_...md
            documenten.append((bron, tekst))
    return documenten


# --- in stukjes knippen ----------------------------------------------------

def _knip(tekst: str, bron: str):
    """Knipt tekst in stukjes van ~STUKJE_TEKENS tekens, op alinea-grenzen."""
    alineas = [a.strip() for a in tekst.split("\n\n") if a.strip()]
    stukjes, buffer = [], ""
    for alinea in alineas:
        if len(buffer) + len(alinea) + 1 <= STUKJE_TEKENS:
            buffer = (buffer + "\n" + alinea).strip()
        else:
            if buffer:
                stukjes.append(buffer)
            if len(alinea) <= STUKJE_TEKENS:
                buffer = alinea
            else:  # heel lange alinea: in stukken hakken
                for i in range(0, len(alinea), STUKJE_TEKENS):
                    stukjes.append(alinea[i:i + STUKJE_TEKENS])
                buffer = ""
    if buffer:
        stukjes.append(buffer)
    return [{"bron": bron, "tekst": s} for s in stukjes if s.strip()]


def _hash(documenten) -> str:
    """Vingerafdruk van de documenten, om te zien of de index nog actueel is."""
    h = hashlib.sha256()
    for bron, tekst in documenten:
        h.update(bron.encode("utf-8"))
        h.update(tekst.encode("utf-8"))
    return h.hexdigest()


# --- embeddings & index ----------------------------------------------------

def _embed(client: OpenAI, teksten):
    """Zet teksten om naar vectoren (in batches)."""
    vectoren = []
    for i in range(0, len(teksten), 100):
        antwoord = client.embeddings.create(model=EMBED_MODEL, input=teksten[i:i + 100])
        vectoren.extend(rij.embedding for rij in antwoord.data)
    return vectoren


def _lees_index():
    if not INDEX_BESTAND.exists():
        return None
    try:
        return json.loads(INDEX_BESTAND.read_text(encoding="utf-8"))
    except Exception:
        return None


def bouw_index(api_key: str):
    """Leest de kennisbank, knipt, embedt en bewaart de index. Geeft statistiek terug."""
    documenten = _lees_documenten()
    stukjes = []
    for bron, tekst in documenten:
        stukjes.extend(_knip(tekst, bron))

    if not stukjes:
        INDEX_BESTAND.write_text(
            json.dumps({"hash": "", "model": EMBED_MODEL, "stukjes": [], "vectoren": []}),
            encoding="utf-8",
        )
        return {"documenten": 0, "stukjes": 0}

    client = OpenAI(api_key=api_key)
    vectoren = _embed(client, [s["tekst"] for s in stukjes])
    INDEX_BESTAND.write_text(
        json.dumps({"hash": _hash(documenten), "model": EMBED_MODEL,
                    "stukjes": stukjes, "vectoren": vectoren}),
        encoding="utf-8",
    )
    return {"documenten": len(documenten), "stukjes": len(stukjes)}


def index_status():
    """Voor de UI: bestaat er een index, hoeveel stukjes, en is hij nog actueel?"""
    idx = _lees_index()
    if not idx:
        return {"bestaat": False, "stukjes": 0, "actueel": False}
    documenten = _lees_documenten()
    actueel = idx.get("hash", "") == (_hash(documenten) if documenten else "")
    return {"bestaat": True, "stukjes": len(idx.get("stukjes", [])), "actueel": actueel}


def zoek(api_key: str, vraag: str, k: int = 5):
    """Geeft de k best passende stukjes bij een vraag: [{bron, tekst, score}, ...]."""
    idx = _lees_index()
    if not idx or not idx.get("vectoren"):
        return []
    client = OpenAI(api_key=api_key)
    qvec = np.asarray(_embed(client, [vraag])[0], dtype="float32")
    matrix = np.asarray(idx["vectoren"], dtype="float32")

    qn = qvec / (np.linalg.norm(qvec) or 1.0)
    mn = matrix / (np.linalg.norm(matrix, axis=1, keepdims=True) + 1e-9)
    scores = mn @ qn
    volgorde = np.argsort(scores)[::-1][:k]
    return [
        {"bron": idx["stukjes"][i]["bron"],
         "tekst": idx["stukjes"][i]["tekst"],
         "score": round(float(scores[i]), 3)}
        for i in volgorde
    ]
