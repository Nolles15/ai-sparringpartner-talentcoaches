# Systeem-prompt — gemaakte keuzes

**AI Sparringpartner voor Talentcoaches** — Hanzehogeschool Groningen / AI Impact Lab
Vastgelegd: juni 2026

Dit document beschrijft de keuzes achter de systeem-prompt van de live AI in de app.
De vaste regels staan als `PROMPT_REGELS` in `app.py`; de kennis wordt er per vraag onder
geplakt door `bouw_systeemprompt()` — uit de kennisbank (via `rag.py`) of, als terugval,
de vaste domeinen `KENNISDOMEINEN`.

> **Update (RAG):** de kennis komt nu uit de **kennisbank** (`kennisbank/`, doorzocht door
> `rag.py`) in plaats van één vast blok. De gronding is verzacht naar **"gebaseerd op /
> in lijn met"**: de AI mag samenvatten en redeneren, zolang dat in lijn blijft met de
> opgehaalde stukken. De "geen kennis"-uitkomst blijft.

---

## Bron van de prompt

De prompt is volledig afgeleid uit de bestaande casus-documentatie — niets is verzonnen:

| Onderdeel van de prompt | Herkomst |
|---|---|
| Rol & doel (sparringpartner, geen beslisser) | CONSTITUTION P-01, P-02 |
| Wie de gebruiker is (talentcoach, <18, weinig tijd) | USER-STORIES "Actoren" |
| Wat een goed antwoord is (NL, 100-300 w, tegenvraag, vervolgstap) | FEATURES F-01 |
| Strikte gronding / niet verzinnen | CONSTITUTION P-04 + opdracht |
| Doorverwijzen + medisch afwegingskader | FEATURES F-02 / F-04, P-01 |
| Bias-kanttekening vrouwen & jongeren | CONSTITUTION P-05 |
| Privacy-attendering | FEATURES F-03, P-03 |
| Niveau 2 buiten scope | CONSTITUTION P-06 |
| Kennisdomeinen (de kennislaag) | FEATURES F-02 (de 7 vereiste domeinen) |
| Noembare bronnen (citaten) | scenario-`evidence` in `dist/index.html` |

## Bewuste keuzes

1. **Gronding op de kennisbank.** De AI baseert zich op (a) de stukken die `rag.py` bij de
   vraag ophaalt uit `kennisbank/` en (b) de context die de coach in het gesprek geeft.
   De gronding is "gebaseerd op / in lijn met": samenvatten en redeneren mag, mits in lijn
   met de opgehaalde stukken. Is er nog geen index of API-sleutel, dan vallen we terug op
   de F-02-samenvatting (`KENNISDOMEINEN`). De definitieve kennisbank hoort bij OB-03.

2. **Expliciete "geen kennis"-uitkomst.** Vindt de AI in de opgehaalde stukken geen
   onderbouwing, dan zegt hij "Daar heb ik geen kennis over" en gokt niet. Een afwijzing
   bevat altijd een reden + alternatief pad (doorverwijzing of herformulering).

3. **Bronnen alleen indien aanwezig.** De AI mag alleen referenties noemen die in de
   kennislaag staan; nieuwe referenties verzinnen is verboden.

4. **Plek in het prototype.** De canonieke prompt staat in `app.py` (de actieve
   Streamlit-app). `dist/index.html` heeft een eigen, kortere variant; die kan later
   met deze versie gelijkgetrokken worden als de HTML weer leidend wordt.

## Te herzien bij OB-03

Zodra de definitieve kennislaag is samengesteld (OB-03), komt die als documenten in
`kennisbank/` (de F-02-samenvatting is dan alleen nog terugval). De grondingsregels en de
"geen kennis"-uitkomst blijven gelijk.
