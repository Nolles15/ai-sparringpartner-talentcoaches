# Overzicht: AI Sparring Kennisbasis – downloadresultaten

143 unieke URL's verwerkt. Bestanden staan in de map `pages/` (3-cijferige index + URL-slug als bestandsnaam).

## Resultaat
- 135 pagina's volledig beschikbaar en leesbaar als Markdown.
- 8 pagina's niet beschikbaar; elk bestand bevat een specifieke, geverifieerde reden (geen generieke foutmelding).

## Correctiegeschiedenis

**Ronde 1 (topsporttopics.nl-migratie):** een gebruiker wees erop dat pagina 103 ten onrechte als 404 was gemarkeerd. Topsporttopics.nl had zijn paralympische content verplaatst naar een nieuw zusterdomein, **paralympicsciencesupport.nl**, met identieke URL-paden. Alle 25 in eerste instantie als "404" of "afgeschermd" gemarkeerde topsporttopics.nl-pagina's zijn herverifieerd op dit nieuwe domein: 20 van de 25 zijn volledig gerecupereerd, 5 bleven genuine fails. Totaal mislukt: 50 → 30.

**Ronde 2 (16 door gebruiker aangeleverde PDF's):** de gebruiker plaatste PDF's in de uploads-map van artikelen die via DOI-links niet ophaalbaar waren (paywalls / JavaScript-only uitgeverspagina's). Elke PDF is via DOI-extractie gekoppeld aan de juiste mislukte pagina en de volledige artikeltekst (abstract, hoofdtekst, referenties) is erin verwerkt. 15 pagina's zijn hierdoor volledig opgelost: 012, 013, 019, 021, 022, 023, 024, 025, 028, 029, 030, 032, 036, 037, 039. Totaal mislukt: 30 → 15.

**Ronde 3 (2 extra PDF's):** nog 2 PDF's aangeleverd ("3659607.pdf" = BreathPro-artikel; "EBSCO-FullText-06_21_2026 (4).pdf"). Opgelost: 018 (ACM, BreathPro: Monitoring Breathing Mode during Running with Earables) en 034 (IJSPP, Developing Athlete Monitoring Systems in Team Sports). Totaal mislukt: 15 → 13.

**Ronde 4 (10 PDF's van de Beek-reeks "Motorisch leren, een update"):** de gebruiker leverde alle 10 delen van Peter Beek's Sportgericht-reeks aan. 5 daarvan (delen 7-10 en deel 1) waren al via de oorspronkelijke fetch gelukt; de overige 5 PDF's matchten precies de nog mislukte sport-gericht.nl- en ResearchGate-pagina's voor deze reeks: 002 (Deel 2, externe focus van aandacht), 003 (Deel 3, impliciet leren), 004 (Deel 4, variabel oefenen/schematheorie), 005 (Deel 5, contextuele interferentie) en 006 (Deel 6, dynamische systeemtheorie). Alle 5 volledig verwerkt incl. referenties. Totaal mislukt: 13 → 8.

## Redenen voor de 8 nog niet-beschikbare pagina's

**Topsporttopics.nl – pagina écht verwijderd (HTTP 404), ook niet op paralympicsciencesupport.nl, 2 stuks**
117, 122 — gecontroleerd op zowel topsporttopics.nl als het zusterdomein paralympicsciencesupport.nl (zelfde pad); beide gaven een lege/404 response. Onderwerpen (hardlopen in de warmte; persoonlijk contact zorg-en-sport) zijn niet paralympisch-specifiek, dus geen migratiekandidaat.

**Topsporttopics.nl – afgeschermd met inlog, ook niet op paralympicsciencesupport.nl, 3 stuks**
133, 139, 140 — tonen "Ho, deze pagina is niet voor iedereen toegankelijk" (alleen voor NOC*NSF-erkende topsportprofessionals); ook op het zusterdomein niet teruggevonden. Onderwerpen (levensgebeurtenissen, esports, technologische innovaties) zijn niet paralympisch-specifiek.

**DOI-link naar uitgeverssite, nog geen PDF ontvangen, 1 stuk**
038 (Wiley, Scandinavian Journal of Medicine & Science in Sports) — fetch geeft een volledig lege response; voor dit artikel is (nog) geen PDF aangeleverd.

**Academische paywall, geen abstract beschikbaar, 1 stuk**
017 (Springer Link) — alleen metadata en referentielijst, geen abstract, geen PDF aangeleverd.

**app.sportdatavalley.nl, 1 stuk**
035 — JavaScript-app die inlog vereist; alleen een technische waarschuwing zonder inhoud.

(2 + 3 + 1 + 1 + 1 = 8. Zie `url_filename_map.tsv` voor de exacte bestandsnamen per code.)

## Methodenotitie
Voor elk van deze 8 is de oorzaak persoonlijk herverifieerd — paywalls zijn bevestigd door de live pagina te bekijken, 404's en inlogschermen op topsporttopics.nl zijn bevestigd via de browser (inclusief controle op het zusterdomein paralympicsciencesupport.nl), en lege responses van uitgeverssites zijn minstens tweemaal opnieuw geprobeerd voor ze als definitief faalpunt zijn vastgelegd. Voor 22 eerder mislukte pagina's (academische artikelen + de Beek-artikelenreeks) is de volledige tekst alsnog verwerkt op basis van door de gebruiker aangeleverde PDF's; deze bestanden zijn gemarkeerd met `STATUS: OPGELOST` in plaats van `STATUS: MISLUKT` zodat duidelijk blijft dat de oorspronkelijke webfetch faalde maar het artikel via een andere weg alsnog compleet is.

Voor de resterende DOI-link (038) en 017 zou eenzelfde aanpak (PDF aanleveren) tot volledige dekking kunnen leiden. De overige 6 (035, 117, 122, 133, 139, 140) zijn van een andere aard (login-vereiste apps/portalen, niet bestaande pagina's) en niet via een PDF op te lossen.
