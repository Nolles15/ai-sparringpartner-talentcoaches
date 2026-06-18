# Features — AI Sparringpartner voor Talentcoaches

**Hanzehogeschool Groningen — Lectoraat Sportinnovator / AI Impact Lab**
Versie 1.1 — juni 2026 *(bijgewerkt na gebruikerstest Iteratie 1)*

---

## Leeswijzer

Elk feature-blok beschrijft wat het systeem doet, hoe het zich gedraagt (inclusief randgevallen), testbare acceptatiecriteria en wat expliciet buiten scope valt. Features zijn gekoppeld aan user stories en bouwen op de principes uit de constitutie.

Wijzigingen t.o.v. versie 1.0 zijn gemarkeerd met ⚠️ (aangepast op basis van gebruikerstest) of ➕ (nieuw toegevoegd).

---

## F-01 — Natural language Q&A interface ✅

**Gelinkt aan:** US-01, US-02, US-03, US-10, US-11
**Prioriteit:** Must-have (MVP)

### Beschrijving

De coach voert in gewone taal een vraag of situatiebeschrijving in. Het systeem reageert met een doordacht perspectief, een verhelderende tegenvraag of een overweging — geformuleerd als sparringpartner, niet als expert met een definitief oordeel. De interactie verloopt als een chat-conversatie.

### Gedrag

**Normale flow (tekst):**
- Coach typt een vraag of situatiebeschrijving in het tekstveld
- Systeem toont een laadindicator (max. 10 seconden)
- Systeem geeft een antwoord van 100–300 woorden; bij complexe vragen mag het langer, mits gestructureerd
- Antwoord eindigt met een concrete vervolgstap, vervolgvraag of expliciete constatering ("op basis hiervan is het verstandig om...")
- Coach kan doorvragen; systeem gebruikt eerdere context in de sessie

⚠️ **Gespreksopening — casus als startpunt:**
Gebruikerstest Iteratie 1 bevestigt dat coaches de tool effectiever vinden als het gesprek begint vanuit een concrete situatie. Het systeem opent daarom bij de eerste boodschap van de coach (als die geen expliciete vraag bevat) met een uitnodiging om een casus te beschrijven: *"Vertel me over de situatie waar je mee zit — dan denken we samen verder."*

**Spraak — invoer:**
- Coach tikt op de microfoonknop en spreekt zijn vraag in
- Gesproken invoer wordt omgezet naar tekst (spraakherkenning, Nederlands)
- Herkende tekst verschijnt in het invoerveld en is bewerkbaar vóór verzending
- Werkt op iOS en Android zonder extra installatie; bij ontbrekende microfoontoegang verschijnt een heldere melding

**Spraak — voorlezen:**
- Elk antwoord heeft een "Voorlezen"-knop
- Bij activering wordt het antwoord hardop voorgelezen in het Nederlands
- Coach kan pauzeren of stoppen via een tweede tik op de knop
- Nuttig op locatie: coach hoeft niet naar het scherm te kijken

**Gebruik per apparaat:**
- Smartphone: korte vragen, spraakbediening, compacte antwoorden — sessie typisch < 3 minuten
- Laptop: inhoudelijker gesprekken, links naar literatuur leesbaar, langere antwoorden — sessie typisch 5–15 minuten

**Context opbouwen:**
- Coach kan vroeg in de sessie sport, leeftijdscategorie of ploeggrootte noemen
- Systeem verwerkt deze context in latere antwoorden zonder dat de coach het hoeft te herhalen
- Systeem verwijst expliciet terug naar eerder genoemde context ("je noemde eerder dat...")

**Sessieafsluiting:**
- Coach kan op elk moment vragen om een samenvatting ("wat zijn mijn actiepunten?")
- Systeem genereert een overzicht van max. 5 punten: besproken situatie, kernoverweging(en), en concrete vervolgstap of -vraag
- Samenvatting is als tekst selecteerbaar voor kopiëren
- ⚠️ Systeem vraagt aan het einde van de sessie of de coach de context en conclusies van dit gesprek wil bewaren voor een volgende sessie over dezelfde sporter — ook als persistente opslag nog niet beschikbaar is in de MVP, wordt deze intentie vastgelegd als prioriteit voor fase 2

### Randgevallen

| Situatie | Gedrag |
|---|---|
| Vraag is te vaag om te beantwoorden | Systeem stelt een verduidelijkende tegenvraag voordat het inhoudelijk reageert |
| Coach vraagt om een diagnose of behandeladvies | Systeem legt uit dat het geen diagnoses stelt en verwijst door naar een sportarts of fysiotherapeut (zie F-04) |
| Antwoord duurt langer dan 10 seconden | Systeem toont voortgangsindicator; bij time-out toont het een foutmelding met de optie opnieuw te proberen |
| Coach typt in een andere taal dan Nederlands | Systeem reageert in de taal van de coach |
| Coach sluit de sessie zonder samenvatting | Context wordt niet bewaard; volgende sessie begint blanco |

### Acceptatiecriteria

- [ ] Antwoord verschijnt binnen 10 seconden voor een standaardvraag op een 4G/WiFi-verbinding
- [ ] Antwoord bevat geen definitieve conclusie zonder nuancering of doorverwijzing
- [ ] Context uit het begin van de sessie wordt aantoonbaar verwerkt in latere antwoorden
- [ ] Samenvatting past op één scherm op een 375px-breed schermformaat
- [ ] Interface werkt volledig via touchscreen (smartphone) en via toetsenbord/muis (laptop)
- [ ] Spraakherkenning zet een Nederlandse vraag van 20–60 woorden correct om naar tekst (>90% accuraatheid in stille omgeving)
- [ ] Text-to-speech leest een antwoord van 200 woorden voor in < 90 seconden, pauzeert en hervat op commando
- [ ] Spraakfunctionaliteit werkt zonder extra app-installatie op iOS 16+ en Android 12+
- [ ] ⚠️ Systeem opent het gesprek met een uitnodiging tot casusbeschrijving als de eerste boodschap van de coach geen expliciete vraag bevat

### Niet in scope (MVP)

- Persistente sessiegeschiedenis — gesprekken van vorige sessies worden niet bewaard in de MVP. ⚠️ **Verhoogde prioriteit voor fase 2:** gebruikerstest Iteratie 1 toont aan dat coaches dit als een bijna-basisverwachting ervaren, niet als een luxe feature. Zie US-12 en US-13.
- Opslaan of exporteren van gesprekken als bestand
- Proactieve meldingen of alerts vanuit het systeem
- Offline spraakherkenning (verbinding vereist)

---

## F-02 — Domein-gerichte kennislaag ✅

**Gelinkt aan:** US-04, US-05
**Prioriteit:** Must-have (MVP)

### Beschrijving

Het systeem heeft toegang tot een gecureerde kennisbasis over sportmonitoring, trainingsbelasting, welzijn, talentontwikkeling, vragenlijstmethodologie en coachingsaanpak. Deze kennislaag vormt de inhoudelijke basis voor alle antwoorden. De laag is samengesteld door het lectoraat en wordt onderhouden door domeinexperts (zie OB-03).

### Vereiste kennisdomeinen (input voor OB-03)

Op basis van veldonderzoek (interviews coaches/experts 2024–2026) en gebruikerstest Iteratie 1 moet de kennislaag de volgende domeinen dekken:

**1. Monitoring-methodologie**
- Saw et al. (2017) raamwerk voor monitoring-implementatie: van doelstelling → vragenlijstkeuze → feedbackmomenten
- SRPE, TQR, wellness-schalen, POMS-afgeleide instrumenten — wat ze meten en hoe je de scores interpreteert
- Individuele score-interpretatie: coaches moeten begrijpen dat een "6" voor de ene sporter iets heel anders betekent dan voor de andere; dit vraagt weken kalibratie
- Hoe vaak vragen stellen? Afweging dagelijks vs. wekelijks vs. maandag/vrijdag

**2. Compliance en sporter-commitment**
- Onboarding-aanpak: gezamenlijk bespreken wat gemonitoord wordt, waarom, en wat de sporter eraan heeft (buy-in vóór eerste invulmoment)
- Eigenaarschap: sporter mede laten kiezen wat gemonitord wordt verhoogt commitment
- Differentiatie per sporter-type (gebaseerd op praktijkonderzoek):
  - *Trouwe invuller*: belonen met meer informatie; verdieping aanbieden
  - *"Als het doel maar duidelijk is"*: altijd de "waarom" uitleggen voordat om invulling gevraagd wordt
  - *"Wat heb ik hieraan?"*: focus op wat de sporter zelf terugkrijgt, niet wat de coach ermee doet
  - *"Niks voor mij"*: durven besluiten te stoppen ipv half doorgaan
- Compliance-strategieën die werken: peer accountability (captain-model), vaste invulmomenten koppelen aan bestaande routine (voor het ijs, direct na training), zo min mogelijk vragen dat je ook echt kunt verwerken

**3. Feedback geven aan sporters**
- Mismatch verwachtingen: sporters vullen dagelijks in en verwachten dagelijkse feedback; dit is niet realistisch — verwachtingen vooraf helder maken
- Feedbackvormen: individueel gesprek met data erbij ("hier zie je je cijfers, wat zie jij?"), groepsfeedback in kleine groepjes, wekelijks journal/logboek
- Frequentie: tweewekelijks individueel als ondergrens; ook de "stabiele invullers" terugkoppeling geven, niet alleen de uitschieters
- Rode-vlaggen-redenering: een lage score is een aanleiding voor een gesprek, geen automatische trainingsaanpassing — "het is geen alarmsysteem"
- Niet reageren is dodelijk voor compliance: één atleet die zegt "hij doet er toch niks mee" ondermijnt het hele team

**4. Periodisering en trainingsplanning**
- Belasting-belastbaarheidmodel: hoe sluit de geplande trainingsload aan op hoe sporters het ervaren (RPE als communicatiemiddel)
- Werken met hypotheses: vergelijk een normale trainingsweek met een trainingskamp op load-indicatoren — gebruik data om planning te onderbouwen, niet te vervangen
- Rode vlaggen terugkijken bij blessures: waren er signalen die over het hoofd werden gezien?
- Periodiseren richting piekmomenten: wanneer geef je feedbackmomenten? Ruim voor of vlak na een piekwedstrijd, nooit erop

**5. Coachpedagogie en relatie coach-sporter**
- Pygmalion-effect: hoge verwachtingen van coach stuwt sporter-ontwikkeling
- Autonomie van de sporter: jongere sporters frequent overleg, oudere sporters zelf laten kiezen hoe vaak en hoe ze feedback willen
- Sporters leren zichzelf te uiten: monitoring als oefening in zelfreflectie en eigenaarschap, niet als controlemiddel
- Mentor mindset (Yeager): hoe motiveer je jongeren, hoe stel je ze aan?

**6. ➕ Medische drempelkennis (toegevoegd op basis van gebruikerstest Iteratie 1)**
- Wanneer is een klacht van een sporter aanleiding om door te sturen naar een fysiotherapeut of sportarts?
- Rode vlaggen in welzijns- en belastingsdata die medische evaluatie indiceren
- Verschil tussen trainingsvermoeidheid (normaal) en signalen die buiten het coachingdomein vallen
- Toon: de AI helpt de coach een afwegingskader te vormen — geen diagnose, wél concrete handvatten voor de beslissing om te verwijzen

**7. ➕ Praktijkvoorbeelden uit andere sporten (toegevoegd op basis van gebruikerstest Iteratie 1)**
- Monitoringaanpakken en coachingpraktijken uit andere sportdisciplines die overdraagbare lessen bevatten
- Expliciet labelen als "voorbeeld uit andere context" — coach bepaalt zelf de relevantie

**8. Veelgestelde coachvragen die de chatbot moet aankunnen**

De volgende vraagtypen komen structureel voor in de praktijk en moeten binnen de kennislaag worden gedekt:

| Vraagtype | Voorbeeldvraag |
|---|---|
| Vóór de training | "Hoe weet ik of een sporter klaar is voor de training van vandaag?" |
| Trendanalyse | "Waarom zijn mijn sporters elke november moe? Hoe kijk ik naar trends?" |
| Score-interpretatie | "Een sporter geeft altijd een 4–7, wat doe ik daarmee?" |
| Compliance-probleem | "Hoe zorg ik dat mijn sporters beter invullen zonder politieagent te zijn?" |
| Feedbackmoment voorbereiden | "Hoe bereid ik een goed 1-op-1 gesprek voor met de data erbij?" |
| Rode vlag beoordelen | "Een sporter scoort laag op welzijn — wanneer pas ik de training aan en wanneer ga ik het gesprek aan?" |
| Onboarding sporter | "Hoe leg ik aan nieuwe sporters uit waarom we monitoren?" |
| Sporter die niet invult | "Wat doe ik met een sporter die structureel niet invult?" |
| Periodisering | "Klopt de load van deze trainingsweek met wat ik had gepland?" |
| Intervisie-dilemma | "Hoe ga ik om met een sporter die zegt dat het goed gaat maar er moe uitziet?" |
| ➕ Medische drempel | "Mijn sporter heeft al drie weken rugpijn na de training — wanneer stuur ik hem naar de sportarts?" |

### Gedrag

**Gebruik van de kennislaag:**
- Het systeem baseert antwoorden op de kennislaag en benoemt het type redenering ("op basis van onderzoek naar trainingsbelasting bij adolescenten...")
- ⚠️ Het systeem voegt waar relevant een bronverwijzing of toelichting op de redenering toe — gebruikerstest Iteratie 1 bevestigt dat coaches dit prettig vinden
- Het systeem hallucineert niet: als een vraag buiten de kennislaag valt, zegt het dat expliciet
- Het systeem markeert wanneer bewijs dun of niet direct van toepassing is op de doelgroep (vrouwen, jongeren onder 18)
- ➕ Het systeem kan op verzoek een voorbeeld uit een andere sport aanhalen, gelabeld als "voorbeeld uit een andere context"

**Doorverwijzing:**
- Bij vragen over blessures, medische klachten of behandelingen: doorverwijzing naar sportarts of fysiotherapeut
- ⚠️ Bij medische drempelkennis: systeem helpt de coach het afwegingskader te doorlopen ("wat zie je, hoe lang al, heeft de sporter pijn of ongemak?") vóór het een doorverwijzing doet — niet meteen verwijzen, maar ook niet te lang wachten
- Bij vragen die Niveau 2-integratie vereisen: uitleg dat dit buiten de MVP-scope valt, met suggestie voor alternatieve aanpak
- Doorverwijzing is altijd vriendelijk, met reden en alternatief pad

### Randgevallen

| Situatie | Gedrag |
|---|---|
| Vraag valt volledig buiten de kennislaag | Systeem zegt: "Dit valt buiten wat ik betrouwbaar kan beantwoorden" en biedt een alternatief (doorverwijzing of herformulering) |
| Bewijs is aanwezig maar tegenstrijdig | Systeem beschrijft de tegenstrijdigheid en adviseert de coach zelf een afweging te maken |
| Coach vraagt naar een specifiek monitoringplatform (bijv. "hoe gebruik ik Smartabase voor X?") | Systeem antwoordt op de onderliggende coachvraag, niet op platformtechniek; verwijst voor platformvragen naar de leverancier |
| Coach stelt een vraag over vrouwelijke sporters of jongeren | Systeem voegt expliciet een kanttekening toe over bewijskwaliteit voor deze doelgroep |
| ➕ Coach vraagt naar een voorbeeld uit een andere sport | Systeem biedt een relevant voorbeeld aan, gelabeld als "voorbeeld uit [sport]" |

### Acceptatiecriteria

- [ ] Kennislaag omvat minimaal: trainingsbelasting, welzijn/RPE, slaap en herstel, talentontwikkeling, vragenlijstmethodologie (SRPE, TQR, POMS-afgeleide schalen), medische drempelkennis, voorbeelden uit andere sporten
- [ ] Systeem geeft bij elk antwoord aan op welk type kennis het zich baseert
- [ ] ⚠️ Systeem voegt bij minimaal 80% van de inhoudelijke antwoorden een bronverwijzing of redenering-toelichting toe
- [ ] Systeem hallucineert niet aantoonbaar in een set van 20 validatievragen (prompttest vóór pilot)
- [ ] Systeem geeft bij minimaal 5 van de 5 testscenario's met doelgroep vrouwen/jongeren een expliciete kanttekening
- [ ] Doorverwijzing naar specialist treedt op in 100% van de testscenario's met medische vragen
- [ ] ➕ Systeem doorloopt een afwegingskader bij medische drempelkwesties vóór het doorverwijst

### Niet in scope (MVP)

- Automatische update van de kennislaag op basis van nieuwe publicaties
- Koppeling met externe literatuurdatabases (PubMed, Google Scholar)
- Niveau 2: analyse van sportersdata uit Smartabase of SportDataValley
- ➕ Kennislaag gevoed door vragen van andere coaches (community-input) — bevestigd als wenselijk in gebruikerstest Iteratie 1, maar vereist moderatie en infrastructuur; fase 2

---

## F-03 — Privacyframing en onboarding ✅

**Gelinkt aan:** US-06, US-08, US-09
**Prioriteit:** Must-have (MVP)

### Beschrijving

Bij eerste gebruik ziet de coach een beknopte introductie: wat de tool doet, wat het niet doet, en hoe het verantwoord gebruikt wordt. De onboarding verlaagt de drempel, stelt verwachtingen bij en informeert coaches over privacyverantwoordelijkheden.

### Gedrag

**Introductietekst (bij eerste login):**
- Max. 3 zinnen over het doel van de tool ("sparringpartner, geen orakel")
- 1 zin over privacygebruik: geen namen of identificeerbare gegevens invoeren
- 2–4 voorbeeldvragen waarmee coaches direct kunnen starten. Voorbeelden gebaseerd op veldonderzoek (te gebruiken als startset of inspiratie):
  - *"Mijn sporter geeft altijd een score tussen 4 en 7. Hoe interpreteer ik dat?"*
  - *"Hoe zorg ik dat sporters goed blijven invullen zonder dat ik de politieagent hoef te spelen?"*
  - *"Ik heb morgen een 1-op-1 met een sporter. Welke vragen stel ik als de welzijnsscore de laatste twee weken dalende is?"*
  - *"Hoe begin ik een goed gesprek over monitoring bij de start van het seizoen?"*
- "Aan de slag"-knop om de chat te openen

**Privacytoelichting:**
- Beschikbaar via een persistent "?" of "Info"-knop in de interface
- Bevat: welk AI-model wordt gebruikt, waar data wordt verwerkt, wat de retentietermijn is, en dat input niet gebruikt wordt voor modeltraining (conform OB-01)
- Geschreven in begrijpelijke taal, zonder juridisch jargon

**Systeemprompt-gedrag bij persoonsgegevens:**
- Als de coach een naam invult (bijv. "Emma heeft een RPE van 8 gehad") attendeert het systeem de coach eenmalig per sessie op het gebruik van anonieme beschrijvingen
- Systeem stopt het gesprek niet — het attendeert vriendelijk en gaat door

### Randgevallen

| Situatie | Gedrag |
|---|---|
| Coach slaat de introductie over | Introductie is opnieuw bereikbaar via "Info"-knop; systeem werkt ook zonder introductie gelezen te hebben |
| Coach vraagt wat er met zijn gespreksdata gebeurt | Systeem verwijst naar de privacytoelichting met directe link |
| Coach typt meerdere keren persoonsgegevens | Systeem attendeert maximaal één keer per sessie — niet bij elke bericht |

### Acceptatiecriteria

- [ ] Introductietekst is zichtbaar bij eerste login en bevat alle verplichte onderdelen (doel, privacyinstructie, voorbeeldvragen)
- [ ] Coach kan binnen 60 seconden na inloggen een eerste vraag stellen
- [ ] Privacytoelichting is bereikbaar via een persistente knop in de interface
- [ ] Privacytoelichting bevat: AI-model, verwerkingslocatie, retentietermijn, trainingsbeleid
- [ ] Systeemprompt attendeert de coach bij invoer van een naam — aantoonbaar in prompttest

### Niet in scope (MVP)

- Uitgebreide registratiewizard of configuratiestap
- Gepersonaliseerde onboarding op basis van sport of organisatie
- In-app handleiding of video-tutorial

---

## F-04 — Fallback & doorverwijzing ✅

**Gelinkt aan:** US-05
**Prioriteit:** Must-have (MVP)

### Beschrijving

Wanneer het systeem een vraag niet kan of mag beantwoorden, geeft het altijd een heldere uitleg en een alternatief pad. Het systeem weigert nooit zonder reden en laat de coach nooit met een dood einde achter.

### Gedrag

**Type 1 — Buiten kennislaag:**
- Systeem zegt expliciet dat de vraag buiten zijn kennisbasis valt
- Systeem stelt een alternatieve herformulering voor of vraagt wat de coach eigenlijk wil weten

**Type 2 — Medische/diagnostische vraag:**
- ⚠️ Systeem helpt de coach eerst het afwegingskader te doorlopen: wat zijn de signalen, hoe lang al, is er pijn of ongemak? Dit sluit aan op de concrete coachingbehoefte die in gebruikerstest Iteratie 1 naar voren kwam
- Systeem legt uit dat het geen medische adviezen geeft
- Systeem verwijst door naar sportarts, fysiotherapeut of sportgeneeskundig centrum
- Toon: vriendelijk, niet-beschuldigend

**Type 3 — Niveau 2-vraag (data-analyse):**
- Systeem legt uit dat directe data-analyse van monitoringsystemen buiten de MVP-scope valt
- Systeem biedt aan de coach te helpen met de onderliggende coachvraag op basis van wat de coach zelf beschrijft

**Type 4 — Technische fout:**
- Bij time-out of serverfout toont het systeem een foutmelding in begrijpelijke taal ("Het duurt even langer dan verwacht. Probeer het opnieuw.")
- Geen technische foutcodes zichtbaar voor de coach

### Randgevallen

| Situatie | Gedrag |
|---|---|
| Coach is gefrustreerd door een "weet niet"-antwoord | Systeem erkent de frustratie en biedt actief een alternatieve ingang |
| Systeem geeft onterecht een "buiten scope"-melding | Dit is een kwaliteitsdefect — te signaleren via gesprekslogs en diepte-interviews |
| Coach herhaalt dezelfde buiten-scope-vraag meerdere keren | Systeem blijft consistent in zijn grens, maar varieert de formulering |

### Acceptatiecriteria

- [ ] Systeem geeft nooit een leeg antwoord of een antwoord dat alleen bestaat uit een weigering
- [ ] Elke fallback bevat een reden én een alternatief pad (doorverwijzing of herformulering)
- [ ] Medische doorverwijzing treedt op in 100% van de testscenario's met symptoom- of blessurevragen
- [ ] ⚠️ Bij medische drempelkwesties doorloopt het systeem aantoonbaar een afwegingskader vóór het doorverwijst
- [ ] Technische foutmeldingen zijn in begrijpelijke taal — geen stacktraces of HTTP-codes zichtbaar

### Niet in scope (MVP)

- Automatische escalatie naar een menselijke expert
- Geïntegreerde zoekfunctie naar externe bronnen of websites

---

## F-05 — Gesprekslogs voor kwaliteitsmonitoring ✅

**Gelinkt aan:** US-07
**Prioriteit:** Should-have (MVP indien OB-06 is besloten vóór start pilot)

### Beschrijving

Sessies worden geanonimiseerd gelogd zodat het projectteam na de pilot gebruikspatronen en inhoudskwaliteit kan analyseren. Coaches zijn hierover geïnformeerd bij onboarding.

### Gedrag

- Elke sessie wordt opgeslagen met: tijdstip, duur, aantal berichten, gespreksonderwerpen (automatisch gelabeld of handmatig geclassificeerd)
- Logs bevatten geen namen van coaches of sporters
- Toegang is beperkt tot geautoriseerde projectteamleden
- Logs worden bewaard tot einde evaluatieperiode (conform OB-06), daarna verwijderd

### Randgevallen

| Situatie | Gedrag |
|---|---|
| Coach heeft persoonsgegevens ingetypt (ondanks instructie) | Log bevat de tekst; projectteam hanteert een protocol voor signalering en verwijdering (te bepalen in OB-06) |
| OB-06 is niet besloten vóór start pilot | Feature wordt uitgeschakeld; pilot draait zonder logs |

### Acceptatiecriteria

- [ ] Logs worden opgeslagen conform OB-06 (retentietermijn, toegangsrecht)
- [ ] Coaches zijn bij onboarding geïnformeerd over logbeleid
- [ ] Toegang tot logs is beperkt tot geautoriseerde projectteamleden — aantoonbaar via toegangscontrole
- [ ] Logs bevatten geen direct identificeerbare persoonsgegevens van coaches of sporters

### Niet in scope (MVP)

- Automatische kwaliteitsscoring van antwoorden
- Real-time dashboard voor projectteam op gespreksdata

---

## ➕ F-06 — Sporterprofiel en contextpersistentie (fase 2, hoge prioriteit)

**Gelinkt aan:** US-12, US-13
**Prioriteit:** Must-have fase 2 *(geprioriteerd op basis van gebruikerstest Iteratie 1)*

### Beschrijving

Coach kan een profiel aanmaken per sporter of groep, met standaard kenmerken die bij elk gesprek over die sporter automatisch beschikbaar zijn. Hierdoor hoeft de coach niet bij elke sessie dezelfde achtergrond opnieuw aan te leveren.

### Rationale

Gebruikerstest Iteratie 1 toont aan dat de contextlast (steeds opnieuw uitleggen wie de sporter is, in welke sport, wat de monitoring-aanpak is) een significante drempel vormt voor herhaald gebruik. Dit is geen luxe feature maar een basisvereiste voor duurzame adoptie.

### Gedrag (ontwerp richting fase 2)

- Coach legt bij aanmaken van een sporter-profiel vast: sport, leeftijdscategorie, ploeggrootte, gebruikte monitoringsysteem, lopende aandachtspunten
- Bij openen van een gesprek over een bekende sporter laadt het systeem het profiel als achtergrondcontext
- Coach kan het profiel bijwerken na een gesprek
- Aan het einde van elke sessie biedt het systeem aan conclusies en actiepunten toe te voegen aan het profiel

### Afhankelijkheden

- OB-07: besluit over contextpersistentie (AVG-conformiteit, retentiebeleid)
- OB-01: platformkeuze moet opslag per coach ondersteunen
- OB-04: privacytoets inclusief profiel-retentie

### Niet in scope (fase 2)

- Automatische inlees van sporterdata uit Smartabase/SDV in het profiel (Niveau 2)
- Delen van profielen tussen coaches

---

## Technische Afhankelijkheden

| Feature | Afhankelijkheid | Risico | Mitigatie |
|---|---|---|---|
| F-01 (Q&A interface) | LLM-platform en hosting (OB-01) | Hoog — geen MVP zonder platformkeuze | OB-01 beslissen in Week 1 |
| F-01 (Q&A interface) | Authenticatie (OB-02) | Hoog — zonder login geen toegangscontrole | OB-02 beslissen in Week 1 |
| F-02 (Kennislaag) | Curatie kennisbronnen (OB-03) | Hoog — kwaliteit van antwoorden staat of valt hiermee | Start kennislaagselectie in Week 1, klaar voor Week 4 |
| F-02 (Kennislaag) | Promptengineering | Middel — kennislaag moet correct worden aangestuurd via systeemprompt | Iteratief testen in Week 4–6 |
| F-03 (Onboarding) | Privacytoets DPO (OB-04) | Hoog — privacytekst en logbeleid moeten AVG-conform zijn | OB-04 afronden vóór Week 7 |
| F-05 (Gesprekslogs) | Logbeleid (OB-06) | Middel — feature valt weg als OB-06 niet op tijd is besloten | OB-06 parallel aan OB-04 |
| F-06 (Sporterprofiel) | Contextpersistentie-besluit (OB-07) | Hoog voor fase 2 — AVG-conformiteit retentie | OB-07 besluiten na pilot |

---

## MVP Releasecriteria

De pilot mag niet starten totdat aan het volgende is voldaan:

- [ ] OB-01 besloten: LLM-platform en hostinglocatie vastgesteld en geconfigureerd
- [ ] OB-02 besloten: Authenticatiemethode geïmplementeerd en getest
- [ ] OB-03 afgerond: Kennislaag samengesteld (incl. medische drempelkennis en voorbeelden andere sporten), gevalideerd door domeinexperts en ingericht in het systeem
- [ ] OB-04 afgerond: Privacytoets door DPO of juridisch adviseur succesvol doorlopen
- [ ] Prompttests geslaagd: minimaal 20 validatievragen zonder hallucinaties, doorverwijzing werkt correct bij medische vragen, afwegingskader medische drempel werkt aantoonbaar
- [ ] Mobiele UX gevalideerd: interface werkt op 375px-scherm, sessietijd < 10 seconden reactietijd
- [ ] Onboardingmateriaal gereed: introductietekst, privacytoelichting en demo-sessieformat beschikbaar
- [ ] Pilotcoaches geworven en geïnformeerd: minimaal 5 coaches committed, demo-sessie ingepland
- [ ] OB-05 besloten: evaluatiestrategie vastgesteld (groepsgrootte, interviewformat, loganalyse)
- [ ] OB-06 besloten of F-05 uitgeschakeld: logbeleid klaar of feature bewust uitgesteld
