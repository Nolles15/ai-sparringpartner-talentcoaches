# RAG-aanpak — de chatbot gebruikt onze eigen kennisbank

**AI Sparringpartner voor Talentcoaches** — Hanzehogeschool Groningen / AI Impact Lab
Voor de voortgangspitch (o.a. NOC*NSF).

---

## Vóór → na

| | Vóór | Na (deze stap) |
|---|---|---|
| Kennis | Eén vast tekstblok in de code | Een **kennisbank** (map met documenten) die experts zelf vullen |
| Antwoorden | Gebaseerd op algemene kennis | **Gebaseerd op / in lijn met** onze eigen documenten |
| Bron | Niet zichtbaar | **Bronvermelding** per antwoord (zichtbaar in de app) |
| "Weet niet" | Soms gokken | Zegt eerlijk *"daar heb ik geen kennis over"* |

## Hoe het werkt (als een slimme bibliotheek)

```
documenten in kennisbank/  ->  in stukjes knippen  ->  doorzoekbaar maken
        (de plank)              (hapklare alinea's)     (op betekenis, 1x klaarzetten)
                                                              |
   vraag van de coach  ->  de 4-6 best passende stukjes pakken  ->  AI antwoordt hiermee
                                                                     + noemt de bron
```

## Demo-script (3 vragen, ~2 minuten)

1. **Goed gedekt** — bijv. *"Hoe ga ik om met een speler die zijn welzijnsvragenlijst al weken niet invult?"*
   → onderbouwd antwoord, met de bron zichtbaar onder "📚 Bronnen achter dit antwoord".
2. **Deels gedekt** — een vraag die maar half in de kennis staat
   → genuanceerd antwoord dat de onzekerheid benoemt.
3. **Buiten de kennis** — bijv. *"Wat is een goede voetbalschoen?"*
   → *"Daar heb ik geen kennis over"* in plaats van gokken. Dit toont de betrouwbaarheid.

## Waarom dit al goed bouwt (niet wegwerp)

De opzet *kennisbank → stukjes → doorzoeken → antwoord met bron* is het echte
productiepatroon. De zoek-motor staat los (`rag.py`), zodat de binnenkant later
vervangen kan worden zonder de app te herbouwen.

## Roadmap

1. **Nu (prototype/pitch):** werkende kennisbank-chatbot in de app, bronvermelding,
   "geen kennis"-gedrag, Hanze-huisstijl. Zoeken via OpenAI.
2. **Pilot:** kennisbank vullen met gecureerde bronnen (met domeinexperts, OB-03);
   evaluatie met de validatievragen; zoeken naar de EU/eigen omgeving verplaatsen (privacy, OB-01).
3. **Productie:** onderhoud van de kennislaag belegd, toegangscontrole, en pas dan eventueel
   echte (geanonimiseerde) gebruikssituaties.

## Wat bewust later komt

Lokaal/EU-zoeken (OB-01), gebruikersaccounts, spraak, en het bewaren van gesprekken —
staan op de roadmap, niet in deze stap.
