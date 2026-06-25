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
# De index wordt compact bewaard: vectoren als float32-binair (klein + snel laadbaar),
# en de tekst/metadata apart als JSON. Beide worden meegeleverd in de repo.
VECTOR_BESTAND = KENNISBANK / "index_vectors.npy"
META_BESTAND = KENNISBANK / "index_meta.json"
EMBED_MODEL = "text-embedding-3-small"
STUKJE_TEKENS = 800  # streefgrootte van een stukje (in tekens)

# Hulp-/metadatabestanden die geen kennis zijn en dus niet ingelezen worden.
NIET_INLEZEN = {"readme.md", "unique_urls.txt", "url_filename_map.tsv"}


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
        if pad.name.startswith(".") or pad.name.lower() in NIET_INLEZEN:
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


def _lees_meta():
    """Leest de metadata (hash, model, stukjes). Vectoren worden apart geladen."""
    if not META_BESTAND.exists():
        return None
    try:
        return json.loads(META_BESTAND.read_text(encoding="utf-8"))
    except Exception:
        return None


def bouw_index(api_key: str):
    """Leest de kennisbank, knipt, embedt en bewaart de index. Geeft statistiek terug."""
    documenten = _lees_documenten()
    stukjes = []
    for bron, tekst in documenten:
        stukjes.extend(_knip(tekst, bron))

    if not stukjes:
        META_BESTAND.write_text(
            json.dumps({"hash": "", "model": EMBED_MODEL, "stukjes": []}),
            encoding="utf-8",
        )
        np.save(VECTOR_BESTAND, np.zeros((0, 0), dtype="float32"))
        return {"documenten": 0, "stukjes": 0}

    client = OpenAI(api_key=api_key)
    vectoren = _embed(client, [s["tekst"] for s in stukjes])
    np.save(VECTOR_BESTAND, np.asarray(vectoren, dtype="float32"))
    META_BESTAND.write_text(
        json.dumps({"hash": _hash(documenten), "model": EMBED_MODEL, "stukjes": stukjes},
                   ensure_ascii=False),
        encoding="utf-8",
    )
    return {"documenten": len(documenten), "stukjes": len(stukjes)}


def index_status():
    """Voor de UI: bestaat er een index, hoeveel stukjes, en is hij nog actueel?"""
    meta = _lees_meta()
    if not meta or not VECTOR_BESTAND.exists():
        return {"bestaat": False, "stukjes": 0, "actueel": False}
    documenten = _lees_documenten()
    actueel = meta.get("hash", "") == (_hash(documenten) if documenten else "")
    return {"bestaat": True, "stukjes": len(meta.get("stukjes", [])), "actueel": actueel}


# --- originele bron (titel + URL) bij een kennisbankbestand --------------

_URL_MAP = None
_BRON_META = {}


def _url_map():
    """Laadt (eenmalig) de map van bestandsnaam -> originele URL uit de .tsv (fallback)."""
    global _URL_MAP
    if _URL_MAP is None:
        _URL_MAP = {}
        tsv = KENNISBANK / "url_filename_map.tsv"
        if tsv.exists():
            for regel in tsv.read_text(encoding="utf-8", errors="ignore").splitlines():
                delen = regel.split("\t")
                if len(delen) >= 2 and delen[0].strip().startswith("http"):
                    _URL_MAP[Path(delen[1].strip()).name] = delen[0].strip()
    return _URL_MAP


def bron_info(bron: str):
    """Geeft (titel, originele_url) voor een kennisbankbestand.

    Titel uit de eerste '# '-kop, URL uit de 'Bron:'-regel in het document, met
    de .tsv als terugval. URL kan None zijn.
    """
    if bron in _BRON_META:
        return _BRON_META[bron]
    titel, url = Path(bron).stem, None
    pad = KENNISBANK / bron
    if pad.exists():
        gevonden_titel = False
        for regel in pad.read_text(encoding="utf-8", errors="ignore").splitlines():
            rs = regel.strip()
            if not gevonden_titel and rs.startswith("# "):
                titel, gevonden_titel = rs[2:].strip(), True
            if url is None and rs.lower().startswith("bron:") and "http" in rs.lower():
                url = rs.split(":", 1)[1].strip()
    if url is None:
        url = _url_map().get(Path(bron).name)
    _BRON_META[bron] = (titel, url)
    return _BRON_META[bron]


def zoek(api_key: str, vraag: str, k: int = 5):
    """Geeft de k best passende stukjes bij een vraag: [{bron, tekst, score}, ...]."""
    meta = _lees_meta()
    if not meta or not VECTOR_BESTAND.exists():
        return []
    stukjes = meta.get("stukjes", [])
    matrix = np.load(VECTOR_BESTAND).astype("float32")
    if not stukjes or matrix.shape[0] == 0:
        return []

    client = OpenAI(api_key=api_key)
    qvec = np.asarray(_embed(client, [vraag])[0], dtype="float32")
    qn = qvec / (np.linalg.norm(qvec) or 1.0)
    mn = matrix / (np.linalg.norm(matrix, axis=1, keepdims=True) + 1e-9)
    scores = mn @ qn
    volgorde = np.argsort(scores)[::-1][:k]
    return [
        {"bron": stukjes[i]["bron"],
         "tekst": stukjes[i]["tekst"],
         "score": round(float(scores[i]), 3)}
        for i in volgorde
    ]


def zoek_meervoudig(api_key: str, vragen, k: int = 6):
    """Zoekt voor meerdere zoektermen en combineert + ontdubbelt de resultaten."""
    samen = {}
    for v in vragen:
        if not v:
            continue
        for h in zoek(api_key, v, k=5):
            sleutel = (h["bron"], h["tekst"][:80])
            if sleutel not in samen or h["score"] > samen[sleutel]["score"]:
                samen[sleutel] = h
    return sorted(samen.values(), key=lambda x: x["score"], reverse=True)[:k]
