"""
AI Sparringpartner voor Talentcoaches — Streamlit-versie van de sessie-3 mock-up.

Dit is een 1-op-1 omzetting van dist/index.html naar Streamlit: dezelfde vijf
schermen (Uitdaging, Aannames, Interactieve Demo, Wat kan er misgaan?, Next Steps),
dezelfde knoppen en velden. Bewust GEEN AI en GEEN externe verbindingen — de
"Interactieve Demo" gebruikt vaste dummy-antwoorden, net als de mock-up.

Starten:  streamlit run app.py
Alleen streamlit en pandas nodig.
"""

import os
from pathlib import Path

import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

import rag  # onze eigen zoek-motor voor de kennisbank

load_dotenv()  # leest OPENAI_API_KEY uit een .env-bestand, als dat er is

ALLOWED_MODELS = ["gpt-5-mini", "gpt-5-nano"]  # mini eerst: schrijft duidelijk netter

# ---------------------------------------------------------------------------
# DUMMY-GEGEVENS (overgenomen uit de mock-up / workshopcanvas)
# ---------------------------------------------------------------------------

ORGANISATIE = "Hanzehogeschool Groningen"
PROJECT = "AI Sparringpartner voor Talentcoaches"

GEBRUIKERSCONTEXT = (
    "Talentcoaches bij RTC's, bonden en opleidingsteams die dagelijks werken met "
    "jonge sporters (tot 18 jaar). Ze werken zowel op locatie als thuis, hebben "
    "weinig tijd en willen snel antwoord op trainings- en begeleidingsvragen."
)

HUIDIG_PROCES = [
    "Coaches overleggen ad hoc met collega's of leidinggevenden",
    "Kennis wordt opgedaan via opleidingen, maar snel vergeten",
    "Platforms zoals Smartabase bevatten data maar bieden geen coachingadvies",
    "Er is weinig structurele ondersteuning buiten vaste overlegmomenten",
]

PIJNPUNTEN = [
    "Coaches missen een klankbord buiten kantooruren",
    "Sportwetenschap is moeilijk toegankelijk voor drukbezette coaches",
    "Kennis over vrouwelijke sporters en jongeren (<18) is dunner en minder overdraagbaar",
    "Privacy-angst blokkeert digitale tools bij sommige coaches",
]

AI_KANSEN = [
    "Gesprekspartner die evidence-based overwegingen geeft zonder beslissing te nemen",
    "Vragen stellen om het denkproces van de coach te scherpen",
    "Bronnen benoemen zodat de coach zelf kan doorlezen",
    "Werkt 24/7 via smartphone of laptop met spraakondersteuning",
    "Vervolgadvies geven bij een signaal dat de coach zelf al heeft gezien",
]

PERSONAS = [
    ("RTC-coach", "Begeleidt 8–15 talenten, werkt 4–6 dagen/week op locatie"),
    ("Bondstrainer", "Reist veel, vraagt zich af of zijn kennis up-to-date is"),
    ("Opleidingscoach", "Weinig tijd voor literatuur, wil concrete handvatten"),
]

KRITISCHE_AANNAMES = [
    "Coaches vertrouwen een AI-sparringpartner genoeg om het echt te gebruiken",
    "De kennislaag is breed genoeg voor de meest gestelde coachingvragen",
    "Coaches begrijpen dat het systeem geen diagnoses stelt",
    "Spraakbediening werkt betrouwbaar op locatie",
    "Coaches gebruiken anonieme omschrijvingen in plaats van namen",
]

DATABRONNEN = [
    "Gecureerde kennislaag: monitoring, compliance, feedback, periodisering, coachpedagogie",
    "WP2-veldonderzoek: interviews coaches en experts 2024-2026",
    "Sportmonitor op Maat / Coach in Control onderzoekstraditie Hanze",
    "Wetenschappelijke literatuur: Saw et al. 2017, SRPE, TQR, wellness-schalen",
]

DATAKWALITEIT = [
    "Kennislaag is bewust afgebakend en gedocumenteerd",
    "Bronnen zijn geannoteerd op doelgroep (leeftijd, geslacht)",
    "Bewijs voor vrouwelijke sporters en jongeren apart gemarkeerd",
    "Coaches voeren geen identificeerbare persoonsgegevens in",
]

PRODUCTVORM = [
    "Chatinterface (tekst + spraak) voor coaches",
    "Werkt op smartphone en laptop",
    "Fase 1 MVP: conversatie + kennislaag",
    "Fase 2 (later): data-integratie met monitoringplatformen",
]

ETHIEK_PRIVACY = [
    "Hosting op AVG-conform platform zonder modeltraining op input",
    "Coaches worden geadviseerd om geen namen of medische gegevens in te voeren",
    "Sporters worden via coach en organisatie geïnformeerd",
    "Privacy-toets DPO is vereist vóór pilot",
]

WAARDECREATIE = [
    "Coach krijgt 24/7 een sparringpartner",
    "Beslissingen worden meer onderbouwd zonder meer tijd te kosten",
    "Vertrouwen groeit doordat beperkingen zichtbaar zijn",
    "Kennis blijft actueel zonder verplichte bijscholing",
]

TIJDLIJN = [
    "Week 1-3: kennislaag opbouwen en cureren",
    "Week 4-6: prototype bouwen en testen met coaches",
    "Week 7-10: pilot met 5-10 talentcoaches",
    "Week 11-12: evaluatie, doorontwikkeling en besluit Fase 2",
]

SUCCESMETINGEN = [
    "5-10 pilotcoaches gebruiken de tool 8-12 weken actief",
    "Coach geeft aan dat de kwaliteit van zijn beslissingen is verbeterd",
    "Geen gevallen van schadelijk advies dat door coach is opgevolgd",
    "NPS > 7 na pilotperiode",
]

# Chat-scenario's: vaste dummy-antwoorden (geen AI). label -> inhoud.
SCENARIOS = {
    "Trainingsbelasting na ziekte": {
        "question": "Mijn U17-speler was 5 dagen ziek met een luchtweginfectie en wil "
                    "maandag alweer meetrainen. Hoe pak ik dit aan?",
        "first": "Na een luchtweginfectie is het belangrijk om niet te snel te hervatten. "
                 "Vuistregel: de opbouwperiode is minimaal even lang als de uitvalperiode — "
                 "bij 5 dagen ziekte reken je op zo'n 5 dagen stapsgewijze opbouw.\n\n"
                 "Voordat ik verder ga: was er ook sprake van koorts of kortademigheid?",
        "replies": {
            "Ja, hij had koorts":
                "Dan is extra voorzichtigheid op zijn plaats. Bij koorts is de belastbaarheid "
                "langer verlaagd. Begin maandag met een korte, laag-intensieve individuele "
                "check-in en laat een TQR-score invullen. Bij twijfel over de longen: even "
                "langs de sportarts.",
            "Nee, alleen verkoudheid":
                "Oké, dat geeft wat meer ruimte. Laat hem maandag meetrainen op lage "
                "intensiteit — teamcontact ja, intensieve drills nog niet. Vraag vooraf en "
                "achteraf een TQR-score; ligt die boven de 14, dan kun je dinsdag opbouwen.",
            "Weet ik niet precies":
                "Begrijpelijk. Vraag de speler zelf hoe het ging: koorts, kortademigheid, "
                "bedrust? Op basis van zijn inschatting én een TQR-score op maandagochtend "
                "kun je een goede beslissing nemen. Twijfelt hij of hij fit is, dan is hij "
                "dat nog niet.",
        },
        "evidence": [
            "Saw et al. (2017) — subjectief welzijn als indicator voor trainingsrespons",
            "TQR-schaal (Total Quality Recovery) — dagelijkse zelfscore",
            "Principe belasting-belastbaarheid — opbouwtijd ≥ uitvaltijd",
        ],
        "disclaimer": "Algemene overwegingen, geen medisch advies. Bij twijfel een sportarts raadplegen.",
    },
    "Compliance monitoring vragenlijsten": {
        "question": "Drie spelers vullen hun welzijnsvragenlijst al weken niet in. Hoe zorg "
                    "ik dat ze het gaan doen zonder dat ik een politieagent word?",
        "first": "Dit is een veelgehoorde spanning: de coach wil data, de speler ervaart het "
                 "als verplichting. De oplossing zit bijna altijd in het 'waarom', niet in "
                 "meer druk.\n\nWeet je al waarom ze het niet invullen — vergeten, weerstand, "
                 "of zien ze het nut niet?",
        "replies": {
            "Ze vergeten het gewoon":
                "Dan: maak het makkelijker én zichtbaarder. Koppel het aan een vast moment "
                "(kleedkamer, einde training) en laat merken dat je de scores echt gebruikt.",
            "Ze zien het nut niet":
                "Vul eerst het 'waarom' in. Geef één keer concreet terug wat je met de data "
                "deed ('ik zag hoge vermoeidheid, daarom ging de intensiteit omlaag'). Zo "
                "wordt het ook hún instrument.",
            "Ze hebben weerstand":
                "Weerstand vraagt een ander gesprek. Bespreek het direct maar zonder "
                "aanklacht: 'ik merk dat je het niet invult — is er iets wat je tegenhoudt?' "
                "Zit er wantrouwen onder, dan lost meer druk niets op.",
        },
        "evidence": [
            "Coach in Control (Hanze) — autonomie en eigenaarschap bij jonge sporters",
            "Intrinsieke motivatie en monitoring-compliance — Ntoumanis et al. 2021",
            "Peer accountability als hefboom voor gedragsverandering",
        ],
        "disclaimer": "De beste aanpak hangt sterk af van de specifieke sporters en context.",
    },
    "Feedbackgesprek na tegenvallend toernooi": {
        "question": "Na een tegenvallend toernooi wil ik een feedbackgesprek houden met een "
                    "gevoelige 16-jarige. Wat moet ik in gedachten houden?",
        "first": "Een feedbackgesprek na een teleurstelling vraagt om goede timing. De eerste "
                 "24-48 uur zijn zelden het juiste moment voor analyse — de speler is nog aan "
                 "het verwerken.\n\nHoe lang geleden was het toernooi?",
        "replies": {
            "Gisteren pas":
                "Wacht nog even met de inhoudelijke analyse. Doe vandaag een korte check-in "
                "('hoe gaat het met je?') en plan het echte gesprek over 2-3 dagen.",
            "Een paar dagen geleden":
                "Goed moment. Begin met luisteren: vraag de speler eerst zelf wat goed ging "
                "en wat lastig was. Focus op procesgedrag, niet op uitkomst. Let op: veel "
                "feedbackliteratuur is op mannen onderzocht.",
            "Al een week geleden":
                "Maak de ingang vooruitgericht: 'ik wil terugkijken, niet om te herhalen wat "
                "misging, maar om mee te nemen naar de volgende keer.' Dat frame werkt goed "
                "bij gevoelige sporters.",
        },
        "evidence": [
            "Coachpedagogie — autonomie-ondersteunend klimaat (Mageau & Vallerand, 2003)",
            "Emotieregulatie bij adolescenten — 48-uurs reflectievenster",
            "Bias-kanttekening: feedbackliteratuur sterk gericht op mannelijke sporters",
        ],
        "disclaimer": "Algemene coachingprincipes. Elke speler is anders; vertrouw op je eigen inschatting.",
    },
    "Vervolgstap bij een dalende TQR-score": {
        "question": "Ik zie dat de TQR-score van een sporter al twee weken daalt. Wat doe ik "
                    "hiermee?",
        "first": "Een TQR die twee weken op rij daalt is een duidelijk signaal — goed dat je "
                 "het zag. Heeft deze sporter ook fysieke klachten, of komt hij vooral minder "
                 "fris over?",
        "replies": {
            "Klachtenvrij, lijkt vooral moe":
                "Past bij cumulatieve vermoeidheid. Bouw het volume 20-30% terug, houd korte "
                "prikkels overeind, en plan een kort 1-op-1 over slaap en belasting buiten de "
                "sport. Herstelt de score binnen 4-5 dagen, dan weer opbouwen.",
            "Hij heeft ook lichte pijnklachten":
                "Dat verandert het beeld. Loop het afwegingskader langs: hoe lang al, en is "
                "de pijn in rust of bij belasting? Bouw het volume terug én plan deze week "
                "een check bij de fysiotherapeut — niet als alarm, wel preventief.",
            "Ik weet het niet, alleen de cijfers":
                "Logisch — de cijfers geven het signaal, niet de context. Plan een kort "
                "gesprek met de grafiek erbij: 'ik zie je herstelscore dalen — herken je dat "
                "en weet je waardoor?' Stuur daarna gericht bij.",
        },
        "evidence": [
            "TQR-schaal — twee weken dalende trend als signaal voor cumulatieve vermoeidheid",
            "Rode-vlaggen-redenering — gesprek vs. training aanpassen vs. doorverwijzen",
            "Medische drempelkennis — afwegingskader bij pijnklachten + dalende scores",
        ],
        "disclaimer": "Algemene overwegingen op basis van je eigen waarneming — geen vervanging voor een gesprek of, bij twijfel, een sportarts.",
    },
    "Tapering voor een belangrijk toernooi": {
        "question": "We hebben over 10 dagen een belangrijk toernooi. Mijn speler traint nu "
                    "op hoog volume. Moet ik een tapering-week inlassen?",
        "first": "Ja, enige tapering is bij de meeste sporters zinvol. Vuistregel: verlaag het "
                 "volume (40-60%) maar houd de intensiteit hoog.\n\nHoe voelt de speler zich "
                 "de afgelopen week — zijn de scores normaal of zakken ze al?",
        "replies": {
            "Scores zijn normaal, voelt goed":
                "Dan kun je het moment zelf kiezen. Dag 1-5: volume -40%, intensiteit gelijk. "
                "Dag 6-8: korte pittige sessies, veel rust. Dag 9-10: lichte activering. "
                "Kanttekening: tapering-onderzoek is vooral bij senioren gedaan.",
            "Scores zakken al een beetje":
                "Dan is het al tijd om te beginnen. Verlaag het volume de komende 3-4 dagen "
                "fors (50-60%), houd 1-2 intensieve prikkels per week. Volg de scores dagelijks.",
            "Geen scores, ik schat het in":
                "Dan word jij het meetinstrument. Let op slaap, stemming, motivatie en "
                "herstelsnelheid. Begin nu al met volume verlagen, zodat je ruimte houdt om "
                "bij te sturen.",
        },
        "evidence": [
            "Mujika & Padilla (2003) — Tapering in competitive athletes: a critical review",
            "Monitoring belasting-belastbaarheid — RPE en TQR als prestatievoorspellers",
            "Bias-kanttekening: tapering-literatuur grotendeels op volwassen mannen",
        ],
        "disclaimer": "Algemene richtlijnen. De optimale taperingvorm is altijd individueel.",
    },
}

# ---------------------------------------------------------------------------
# SYSTEEM-PROMPT  (zie agent-docs/SYSTEEM-PROMPT.md voor de gemaakte keuzes)
# ---------------------------------------------------------------------------

# Vaste kennisdomeinen — terugval als er nog geen kennisbank-index of API-sleutel is.
# Normaal komt de kennis uit de map kennisbank/ via rag.py (zie bouw_systeemprompt).
KENNISDOMEINEN = """\
1. MONITORING-METHODOLOGIE
- Saw et al. (2017): subjectieve monitoring (welzijn/RPE) voorspelt trainingsrespons vaak beter dan objectieve maten; bouw monitoring op van doel -> vragenlijstkeuze -> feedbackmoment.
- SRPE (sessie-RPE = RPE x duur) meet interne trainingsbelasting; TQR (Total Quality Recovery) en wellness-schalen meten herstel/welzijn.
- Score-interpretatie is individueel: een '6' betekent per sporter iets anders en vraagt weken kalibratie. Kijk naar trends en afwijkingen van iemands eigen baseline, niet naar absolute waarden.
- Frequentie is een afweging (dagelijks vs. wekelijks vs. vaste momenten); minder vragen die je echt verwerkt is beter dan veel die je laat liggen.

2. COMPLIANCE EN COMMITMENT
- Buy-in vooraf: bespreek samen wat, waarom en wat de sporter eraan heeft, voor het eerste invulmoment. Eigenaarschap (sporter laten meekiezen) verhoogt commitment.
- Sporter-archetypes: 'trouwe invuller' (beloon met verdieping); 'als het doel maar duidelijk is' (leg altijd het waarom uit); 'wat heb ik eraan?' (focus op wat de sporter terugkrijgt); 'niks voor mij' (durf te stoppen i.p.v. half door te gaan).
- Werkende strategieen: invulmomenten aan bestaande routine koppelen, peer accountability (captain-model), en zichtbaar iets met de data doen.
- Niet reageren op ingevulde data ondermijnt de compliance van het hele team.

3. FEEDBACK GEVEN AAN SPORTERS
- Managen van verwachtingen: dagelijks invullen betekent niet dagelijks feedback; maak dat vooraf helder.
- Vormen: 1-op-1 met de data erbij ('hier zie je je cijfers, wat zie jij?'), kleine groepjes, of een wekelijks logboek. Ondergrens: tweewekelijks individueel, ook voor stabiele invullers (niet alleen de uitschieters).
- Rode-vlag-redenering: een lage score is aanleiding voor een gesprek, geen automatische trainingsaanpassing — het is geen alarmsysteem.

4. PERIODISERING EN BELASTING
- Belasting-belastbaarheid: stem geplande load af op hoe sporters het ervaren (RPE als communicatiemiddel). Onderbouw planning met data i.p.v. die te vervangen.
- Bij blessures: kijk terug of er signalen over het hoofd zijn gezien. Plan feedback- en piekmomenten ruim voor of vlak na een piek, nooit erop.
- Tapering: verlaag het volume (40-60%) maar houd de intensiteit hoog; te vroeg of te veel volume reduceren vermindert het effect.

5. COACHPEDAGOGIE EN RELATIE
- Pygmalion-effect: hoge, realistische verwachtingen stuwen ontwikkeling. Schaal autonomie met leeftijd: jongere sporters frequenter overleg, oudere sporters meer zelf laten kiezen.
- Monitoring is een oefening in zelfreflectie en eigenaarschap, geen controlemiddel. Mentor mindset: hoge verwachtingen samen met hoge steun.

6. MEDISCHE DREMPELKENNIS
- Afwegingskader voor doorverwijzen: welke signalen, hoe lang al, pijn in rust of alleen bij belasting, wordt het erger? Onderscheid normale trainingsvermoeidheid van signalen buiten het coachdomein.
- Aanhoudende klachten (>1-2 weken), pijn in rust, of verergering bij belasting: verwijs naar fysiotherapeut of sportarts. Geef zelf nooit diagnose of behandeladvies.

7. VOORBEELDEN UIT ANDERE SPORTEN
- Je mag een overdraagbare aanpak uit een andere sport aanhalen, maar label dat expliciet als 'voorbeeld uit een andere context'; de coach bepaalt zelf de relevantie.

BIAS-KANTTEKENING (geldt overal)
- Veel sportwetenschap is gebaseerd op volwassen mannelijke topsporters. Bij vrouwelijke sporters en jongeren (<18) is bewijs dunner en niet altijd overdraagbaar; benoem dat expliciet.
"""

# De vaste regels van de systeeminstructie. De kennis zelf wordt er per vraag onder
# geplakt door bouw_systeemprompt(): de opgehaalde stukjes uit de kennisbank, of
# (als terugval) de vaste domeinen hierboven.
PROMPT_REGELS = """\
ROL
Je bent een AI-sparringpartner voor talentcoaches, ontwikkeld door de Hanzehogeschool Groningen (Lectoraat Sportinnovator / AI Impact Lab). Je helpt de coach vooral om zélf tot een goede afweging te komen: de juiste vraag scherp krijgen, de juiste informatie opzoeken (in SportData Valley) en die goed interpreteren. Dát zijn je belangrijkste rollen. Een concreet advies mag erbij, maar staat op de tweede plaats — je neemt het denken en de beslissing niet over. Je stelt geen diagnoses; de coach blijft altijd de beslisser.

WIE IS DE GEBRUIKER
Een talentcoach die 10-20 jonge sporters (meestal <18) begeleidt in een RTC, talentteam of opleidingsploeg. Hij heeft domeinkennis en motivatie, maar geen data-analist of sportwetenschapper bij de hand. Hij gebruikt je ad hoc op smartphone of laptop, vaak tussen trainingen door en met weinig tijd.

ANTWOORDPATROON (volg dit elke keer)
- Begin met één meelevende of meedenkende zin. Open NOOIT met een disclaimer zoals "daar heb ik geen kennis over".
- Help daarna het denken van de coach, in lopende zinnen (geen opsomming): benoem waar het eigenlijk om draait, of welke ene factor nu belangrijk is.
- Wijs naar de juiste informatie en waar de coach die in SportData Valley ziet (dashboard, grafiek, tabel).
- Geef interpretatiehulp in plaats van een oordeel: "als je X ziet, kan dat Y betekenen; zie je het andersom, dan eerder Z."
- Een concreet advies mag erbij ("ik zou overwegen om..."), maar kort en bescheiden — niet de hoofdmoot en geen kant-en-klaar lijstje.
- Stel zelf hooguit ÉÉN vraag áán de coach; som geen rij check-vragen op.
- Gaat het over een sporter? Sluit dan af met een kort kopje "Vragen die je aan de sporter kunt stellen:" en daaronder 2-4 open, uitnodigende vragen die de coach in het gesprek met de sporter kan gebruiken. Maak het vragen waarop de sporter zelf kan vertellen — geen kruisverhoor en geen ja/nee-vragen. Bij puur technische of SDV-hoe-vragen laat je dit weg.
- Verdeel je antwoord in 2 tot 4 alinea's met een witregel ertussen. Belangrijk: een alinea bestaat uit MEERDERE zinnen samen — zet niet elke zin op een eigen regel (dat oogt hakkelig). Lopende zinnen, geen bullets (behalve het korte vragenlijstje voor de sporter aan het eind).
- Wees gerust wat uitgebreider als de informatie écht nuttig is: extra toelichting, een tweede invalshoek of wat meer interpretatie is welkom. Richtlijn 150-280 woorden, en diepgang mag voorgaan op een woordenlimiet. Vermijd wel opvulling en herhaling, en blijf concreet en leesbaar.

TAAL (de coach is geen techneut)
- Schrijf korte, heldere zinnen (richtlijn: hooguit ~18 woorden per zin). Plak niet veel dingen met komma's aan elkaar tot één lange dreunzin.
- Vlotte, gewone spreektaal. Ga spaarzaam om met vakjargon; een enkele bekende term (rustpols, RPE, herstelscore) mag, leg 'm zo nodig kort uit. Vermijd vooral stapelingen van afkortingen en klinische woorden.
- Ga NIET uit van een geslacht. Noemt de coach zelf "hij" of "zij", neem dat over; zegt de coach niets over geslacht, schrijf dan neutraal ("de sporter", "diegene") en vermijd standaard "zij/haar" of "hij/hem".
- Geef advies, geen college: één of twee bruikbare punten, geen uitputtende checklist.
- Reageer als sparringpartner: een perspectief of overweging, geen definitief oordeel.
- Is de vraag echt te vaag? Stel dan eerst één verhelderende tegenvraag voordat je inhoudelijk reageert.

SPORTDATA VALLEY OP COACH-NIVEAU
- Gaat je advies over iets dat een coach in SportData Valley kan volgen (welzijn, herstel, slaap, rustpols, RPE, stemming, vragenlijsten, belasting)? Sluit dan af met een korte, natuurlijke brug naar SDV in de trant van: "Houd X de komende dagen in de gaten — dat zie je in SDV op plek Y." Doe dit standaard waar het past, maar forceer het niet als het echt niet relevant is.
- Houd die brug op coach-niveau en feitelijk: in SDV volgt een coach zijn groep via het Dashboard (grafieken/trends per sporter); dezelfde cijfers zijn er ook als tabel te bekijken; vragenlijsten zet hij uit via zijn groep; en gekoppelde apps/wearables (Strava, Polar, Fitbit) laten die data binnenkomen.
- Wijs naar wat de coach zélf ziet en aanklikt (dashboard, grafiek, tabel). Noem GEEN technische dingen als API, tokens, dataset-ID's, URL's, code, export of JupyterHub — tenzij hij daar zelf expliciet om vraagt.

VERBONDENHEID (de coach staat er niet alleen voor)
- Verweef waar het past een korte quote of praktijkvoorbeeld van een ándere coach uit de meegegeven kennis, zodat het herkenbaar wordt en de coach voelt dat anderen hier ook mee worstelen ("zo pakte een waterpolocoach dit aan: ...").
- Gebruik UITSLUITEND quotes, namen en voorbeelden die letterlijk in de meegegeven kennis staan. Verzin NOOIT een quote en leg nooit woorden in de mond van een coach.
- Zet een letterlijke quote op een eigen regel als blockquote (begin die regel met "> "), met ervoor of erna wie het zei. Zo valt de quote visueel op.

VOORBEELDEN VAN DE GEWENSTE STIJL (zo klinkt een goed antwoord; niet letterlijk overnemen)

Vraag: De rusthartslag van mijn sporter is al vijf dagen zo'n tien slagen hoger dan normaal. Wat kan ik daaraan doen?
Antwoord:
Goed dat je dit ziet. De vraag is eigenlijk of dit gewone vermoeidheid van de training is, of dat er iets anders speelt. Dat hangt vooral af van of er meerdere signalen tegelijk veranderen.

Kijk daarom in SportData Valley op het groepsdashboard, als grafiek of tabel, naar de slaap, het welbevinden en de rustpols van deze sporter. Gaan die de laatste dagen samen achteruit, dan past het meer bij oplopende vermoeidheid of een opkomend griepje; is alleen de rustpols hoog en de rest normaal, dan is het meestal minder zorgelijk.

Het helpt ook om de context erbij te pakken. Was er net een zware trainingsweek of wedstrijd, of speelt er iets buiten de sport, zoals tentamens of slecht slapen? In SDV zie je aan de trainingsbelasting of er recent een piek was; valt die samen met de klachten, dan is herstel waarschijnlijk gewoon nodig.

Bij dat beeld zou ik de training een paar dagen rustiger maken en een extra hersteldag inplannen, en het kort blijven volgen. Komt er koorts of pijn bij, of zakt het na een week niet, dan is het tijd voor de sportarts.

Vragen die je aan de sporter kunt stellen:
- Hoe voel je je de laatste dagen vergeleken met normaal, in en buiten de training?
- Hoe slaap je op dit moment, en word je uitgerust wakker?
- Is er buiten de sport iets veranderd, zoals school, drukte of spanning?

Vraag: Ik monitor mijn sporters via SDV. Is er gewoon een tabel of grafiek waar ik dit zie?
Antwoord: Ja, allebei kan. Ga naar het dashboard van je groep; daar zie je de cijfers als grafiek over de tijd. Wil je liever de losse getallen per dag, dan bekijk je dezelfde data als tabel. Zo zie je in één oogopslag of de rustpols stijgt of weer zakt. Over welke sporter wil je het precies hebben?

Vraag: Een paar sporters vullen hun vragenlijst al weken niet in. Hoe pak ik dat aan?
Antwoord:
Vervelend, en je bent zeker niet de enige — bijna elke coach loopt hier tegenaan. Het helpt vaak om niet de politieagent te spelen, maar de "waarom" centraal te zetten: snapt de sporter wat hij er zelf aan heeft?

Een waterpolocoach pakte het praktisch aan:

> "Als iemand drie keer niet invult, bel ik even in plaats van te blijven appen — ik vraag dan hoe dat komt."

Sporters vullen ook beter in als ze merken dat jij echt iets met hun antwoorden doet; zonder reactie verdwijnt de motivatie snel.

In SportData Valley zie je op het groepsdashboard in één oogopslag wie er achterloopt, zodat je gericht het gesprek kunt aangaan in plaats van iedereen te herinneren.

Vragen die je aan de sporter kunt stellen:
- Wat maakt dat het invullen er de laatste tijd bij inschiet?
- Wat zou jij ervan terug willen zien, zodat het de moeite waard voelt?
- Op welk moment in je dag zou invullen het makkelijkst passen?

GRONDING — BLIJF IN LIJN MET DE KENNIS
- Baseer je inhoudelijke antwoorden op (a) de kennis die hieronder is meegegeven en (b) de context die de coach in dit gesprek geeft.
- Je mag samenvatten, combineren en redeneren, maar blijf in lijn met de strekking van die kennis; voeg geen feiten, cijfers of richtlijnen toe die er niet uit volgen.
- Verwijs kort en leesbaar naar waar je je op baseert (het onderwerp of de bron), in gewone taal — niet met ruwe bestandsnamen of losse codes midden in de tekst.
- Vind je in de meegegeven kennis geen onderbouwing? Geef dan eerlijk aan dat je het niet zeker weet — kort en terloops in de tekst, niet als openingszin — en gok of verzin nooit feiten of bronnen.
- Is bewijs dun, tegenstrijdig of niet van toepassing op de doelgroep (vrouwen, jongeren <18)? Benoem die onzekerheid in plaats van stelliger te klinken dan kan.

GRENZEN
- Medisch: bij klachten, blessures of symptomen loop je eerst het afwegingskader langs (welke signalen, hoe lang al, pijn in rust of bij belasting?) en verwijs je daarna door naar sportarts of fysiotherapeut. Geen medisch advies.
- SportData Valley (SDV) is het systeem dat deze coaches gebruiken. Je hebt zelf geen toegang tot hun eigen data en analyseert die niet. Hoe je een coach over SDV uitleg geeft, staat onder 'SPORTDATA VALLEY OP COACH-NIVEAU'.
- Privacy: typt de coach een naam of herleidbare persoonsgegevens? Attendeer hem dan een keer vriendelijk op anonieme omschrijvingen en ga gewoon door.
- Laat de coach nooit met een leeg antwoord achter: een afwijzing bevat altijd een reden en een alternatief pad (doorverwijzing of herformulering).
"""


def bouw_systeemprompt(stukjes):
    """Plakt de opgehaalde kennisstukjes (of de vaste domeinen als terugval) onder de regels."""
    if stukjes:
        kennis = "\n\n".join(f"[Bron: {s['bron']}]\n{s['tekst']}" for s in stukjes)
    else:
        kennis = KENNISDOMEINEN
    return f"{PROMPT_REGELS}\nKENNIS (jouw inhoudelijke bron — baseer je hierop)\n{kennis}\n"

# Risico's: (titel, niveau, bullets). niveau bepaalt de kleur (error/warning/info).
RISKS = [
    ("Hallucinatie & onjuist advies", "error", [
        "AI kan zelfverzekerd klinken ook als het antwoord onjuist is",
        "Coaches kunnen onjuiste informatie overnemen zonder te controleren",
        "Mitigatie: kennislaag afgebakend, onzekerheid expliciet benoemd",
    ]),
    ("Privacy & persoonsgegevens", "warning", ETHIEK_PRIVACY),
    ("Bias voor vrouwen & jongeren", "warning", [
        "Sportwetenschap is sterk gericht op mannelijke volwassen topsporters",
        "Bevindingen zijn niet altijd overdraagbaar naar meisjes <18 jaar",
        "Mitigatie: kennislaag annoteert per bron op doelgroep",
    ]),
    ("Over-afhankelijkheid coach", "info", [
        "Coach kan eigen oordeel te snel vervangen door AI-advies",
        "Principe P-01: coach blijft altijd beslisser — afdwingbaar via prompt",
        "Evaluatie pilot let op dit gedrag",
    ]),
    ("Adoptie & compliance", "info", [
        "Coaches moeten vertrouwen hebben in het systeem om het te gebruiken",
        "Eerste pilots bepalen of de tool de gewenste gesprekskwaliteit heeft",
        "Spraakondersteuning is cruciaal voor gebruik op locatie",
    ]),
    ("Waardecreatie onzeker", "error", [
        "Het is nog niet bewezen dat gesprekskwaliteit met de tool verbetert",
        "Pilotevaluatie na 8-12 weken is de eerste echte toets",
    ]),
]

ROADMAP = [
    ("Kennislaag cureren",
     "Stel met domeinexperts de definitieve bronnen vast en annoteer elke bron op doelgroep."),
    ("Privacy-toets DPO",
     "Laat de AVG-conformiteit bevestigen vóór de pilot. Kies het hostingplatform op dit advies."),
    ("Pilot 5–10 coaches (week 7–10)",
     "Test met echte coachingvragen. Meet adoptie, gesprekskwaliteit en vertrouwen."),
    ("Evaluatie & besluit Fase 2",
     "Bepaal op basis van de pilot of data-integratie (Niveau 2) toegevoegde waarde heeft."),
]

FEEDBACK_PROMPT = "Helpt dit prototype om sneller te bepalen wat er gebouwd moet worden?"

NAV = ["Uitdaging", "Aannames", "Interactieve Demo", "Wat kan er misgaan?", "Next Steps"]


# ---------------------------------------------------------------------------
# HULPFUNCTIE
# ---------------------------------------------------------------------------

def bullets(items):
    st.markdown("\n".join(f"- {item}" for item in items))


# ---------------------------------------------------------------------------
# SCHERMEN
# ---------------------------------------------------------------------------

def scherm_uitdaging():
    st.subheader("De uitdaging")
    st.write(
        "Talentcoaches hebben dagelijks complexe begeleidingsvragen maar weinig toegang "
        "tot evidence-based kennis op het moment dat het er toe doet — op locatie, buiten "
        "kantooruren, in de drukte van de dag."
    )
    rij1 = st.columns(2)
    with rij1[0]:
        st.markdown("**Voor wie**")
        st.write(GEBRUIKERSCONTEXT)
    with rij1[1]:
        st.markdown("**Huidig proces**")
        bullets(HUIDIG_PROCES)
    rij2 = st.columns(2)
    with rij2[0]:
        st.markdown("**Pijnpunten**")
        bullets(PIJNPUNTEN)
    with rij2[1]:
        st.markdown("**AI-kansen**")
        bullets(AI_KANSEN)

    st.markdown("##### Persona's")
    for naam, omschrijving in PERSONAS:
        col = st.columns([1, 4])
        col[0].markdown(f"**{naam}**")
        col[1].caption(omschrijving)


def scherm_aannames():
    st.subheader("Aannames")
    st.caption("te toetsen")
    st.write(
        "Dit zijn de aannames waarop het prototype rust. Ze moeten worden gevalideerd "
        "voordat er een functionele app wordt gebouwd."
    )
    rij1 = st.columns(2)
    with rij1[0]:
        st.markdown("**Kritische aannames**")
        bullets(KRITISCHE_AANNAMES)
    with rij1[1]:
        st.markdown("**Kennislaag & databronnen**")
        bullets(DATABRONNEN)
    rij2 = st.columns(2)
    with rij2[0]:
        st.markdown("**Datakwaliteit & scope**")
        bullets(DATAKWALITEIT)
    with rij2[1]:
        st.markdown("**Productvorm**")
        bullets(PRODUCTVORM)


# Voorbeeldvragen om de demo te starten (mix van coaching + SportData Valley).
STARTERS = [
    ("Speler net ziek geweest",
     "Mijn U17-speler was 5 dagen ziek en wil maandag weer meetrainen. Hoe pak ik dit aan?"),
    ("Sporters vullen niet in",
     "Een paar sporters vullen hun welzijnsvragenlijst al weken niet in. Wat kan ik doen?"),
    ("Vragenlijst uitzetten in SDV",
     "Hoe zet ik in SportData Valley een wekelijkse vragenlijst uit naar mijn groep?"),
    ("Dalende herstelscore",
     "Ik zie dat de herstelscore van een sporter twee weken daalt. Wat doe ik daarmee?"),
]


def instellingen():
    """Verstopt instellingenblok op de pagina zelf (ingeklapt): API key, model, beheer."""
    with st.expander("⚙️ Instellingen (API-sleutel & model)", expanded=False):
        key_veld = st.text_input(
            "OpenAI API key", type="password",
            help="Wordt niet opgeslagen. Laat leeg om OPENAI_API_KEY uit .env te gebruiken.",
        )
        model = st.selectbox("Model", ALLOWED_MODELS, index=0)  # standaard gpt-5-mini (beste tekst)

        # Key uit het veld; valt terug op .env (OPENAI_API_KEY). Nooit hardcoded.
        api_key = key_veld or os.getenv("OPENAI_API_KEY", "")
        if api_key and key_veld:
            st.caption("✅ API key uit het veld")
        elif api_key:
            st.caption("✅ API key uit .env")
        else:
            st.caption("⚠️ Nog geen API key — vul er een in of zet OPENAI_API_KEY in .env")

        kol1, kol2 = st.columns(2)
        with kol1:
            if st.button("🔄 Herindexeer kennisbank"):
                if not api_key:
                    st.warning("Een API-key is nodig om te indexeren.")
                else:
                    with st.spinner("Kennisbank indexeren..."):
                        try:
                            stats = rag.bouw_index(api_key)
                            st.success(f"Klaar: {stats['documenten']} documenten, "
                                       f"{stats['stukjes']} stukjes.")
                        except Exception as fout:
                            st.error(f"Indexeren mislukt: {fout}")
        with kol2:
            if st.button("🗑️ Nieuw gesprek"):
                st.session_state.messages = []
                st.rerun()

        kb = rag.index_status()
        status = (f"📚 {kb['stukjes']} stukjes geïndexeerd" if kb["bestaat"]
                  else "📚 nog niet geïndexeerd")
        st.caption(status + " · Privacy: typ geen herleidbare gegevens van sporters in.")
    return api_key, model


def vraag_llm(api_key, model, gesprek, systeemprompt):
    """De LLM-call. Retourneert (antwoord, foutmelding) — één van beide is None."""
    try:
        client = OpenAI(api_key=api_key)                          # de sleutel
        antwoord = client.chat.completions.create(                # de LLM-call
            model=model,
            messages=[{"role": "system", "content": systeemprompt}, *gesprek],
            max_completion_tokens=8000,
        ).choices[0].message.content
    except Exception as fout:
        return None, f"Kon het taalmodel niet bereiken: {fout}"
    if not antwoord:
        return None, ("Geen tekst ontvangen — mogelijk ging het tokenbudget op aan "
                      "redeneren. Probeer het opnieuw of kies gpt-5-mini.")
    return antwoord, None


def bedenk_zoektermen(api_key, model, gesprek):
    """Lichte agentic stap: laat het model 1-3 zoektermen bedenken bij de laatste vraag.

    Splitst samengestelde vragen op (bijv. coaching-kant + SportData Valley-kant) en
    gebruikt de eerdere berichten om verwijzingen ('dat', 'dit') te begrijpen.
    """
    instructie = (
        "Je bent een zoekhulp voor een kennisbank over talentcoaching, trainingsmonitoring "
        "en zelfrapportage (en het systeem SportData Valley). Zet de LAATSTE vraag van de coach "
        "om in 1 tot 3 korte zoektermen die aansluiten op vakdocumenten. Splits een "
        "samengestelde vraag op in losse termen. Voeg ALLEEN een SportData Valley-term toe als "
        "de vraag echt over dat systeem gaat (dashboard, grafiek, tabel, vragenlijst uitzetten). "
        "Gebruik de eerdere berichten alleen om verwijzingen te begrijpen. Antwoord met enkel de "
        "zoektermen, elk op een eigen regel, zonder nummering."
    )
    recent = [{"role": m["role"], "content": m["content"]}
              for m in gesprek if m.get("role") in ("user", "assistant")][-4:]
    ruw = ""
    try:
        client = OpenAI(api_key=api_key)
        ruw = client.chat.completions.create(
            model=model,
            messages=[{"role": "system", "content": instructie}, *recent],
            max_completion_tokens=600,  # ruim: reasoning-modellen gebruiken een deel aan 'denken'
        ).choices[0].message.content or ""
    except Exception:
        ruw = ""
    termen = [r.strip(" -•\t0123456789.\"") for r in ruw.splitlines() if r.strip()]
    termen = [t for t in termen if len(t) > 1][:3]
    laatste = next((m["content"] for m in reversed(gesprek) if m.get("role") == "user"), "")
    return termen or [laatste]


def toon_bronnen(stukjes, zoektermen=None):
    """Toont een opgeschoonde, ontdubbelde lijst met links naar de originele bronnen."""
    if not stukjes:
        return
    # Ontdubbel op bestand, hoogste relevantie eerst.
    beste = {}
    for s in stukjes:
        if s["bron"] not in beste or s["score"] > beste[s["bron"]]:
            beste[s["bron"]] = s["score"]
    bronnen = sorted(beste, key=lambda b: beste[b], reverse=True)

    with st.expander(f"📚 Bronnen ({len(bronnen)})"):
        if zoektermen:
            st.caption("🔎 Zelf gezocht op: " + " · ".join(zoektermen))
        for bron in bronnen:
            titel, url = rag.bron_info(bron)
            st.markdown(f"- [{titel}]({url})" if url else f"- {titel}")


def scherm_demo(api_key, model):
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Lege chat: korte intro + voorbeeldvragen om te starten.
    if not st.session_state.messages and "_pending" not in st.session_state:
        st.markdown("#### Stel je vraag aan de sparringpartner")
        st.caption("Een meedenkende collega op basis van sportwetenschap en SportData Valley. "
                   "Typ je vraag hieronder, of kies een voorbeeld om te starten.")
        if not api_key:
            st.info("⚙️ Open **Instellingen** hierboven en vul je OpenAI-sleutel in om te starten.")
        kolommen = st.columns(len(STARTERS))
        for kol, (label, vraagtekst) in zip(kolommen, STARTERS):
            if kol.button(label, key=f"start::{label}"):
                st.session_state._pending = vraagtekst
                st.rerun()

    # Gespreksgeschiedenis tonen (met bronnen onder de AI-antwoorden).
    for bericht in st.session_state.messages:
        with st.chat_message(bericht["role"]):
            st.write(bericht["content"])
            toon_bronnen(bericht.get("bronnen"), bericht.get("zoektermen"))

    # Invoerveld onderaan de chat. st.chat_input zit vast aan de onderkant en blijft
    # altijd bereikbaar; Streamlit regelt het scrollen van het gesprek zelf.
    vraag = st.chat_input("Beschrijf je situatie of stel je vraag...")
    vraag = vraag or st.session_state.pop("_pending", None)

    if vraag:
        if not api_key:
            st.warning("Open **Instellingen** bovenaan en vul eerst je OpenAI API key in.")
            return
        st.session_state.messages.append({"role": "user", "content": vraag})
        with st.chat_message("user"):
            st.write(vraag)
        with st.chat_message("assistant"):
            with st.spinner("De sparringpartner zoekt in de kennisbank en denkt na..."):
                try:
                    termen = bedenk_zoektermen(api_key, model, st.session_state.messages)
                    stukjes = rag.zoek_meervoudig(api_key, termen, k=6)
                except Exception:
                    termen = []
                    try:
                        stukjes = rag.zoek(api_key, vraag, k=5)
                    except Exception:
                        stukjes = []
                systeemprompt = bouw_systeemprompt(stukjes)
                antwoord, foutmelding = vraag_llm(
                    api_key, model, st.session_state.messages, systeemprompt)
            if foutmelding:
                st.error(foutmelding)
            else:
                st.write(antwoord)
                toon_bronnen(stukjes, termen)
                st.session_state.messages.append(
                    {"role": "assistant", "content": antwoord,
                     "bronnen": stukjes, "zoektermen": termen})


def scherm_risicos():
    st.subheader("Wat kan er misgaan?")
    st.write(
        "Dit zijn de belangrijkste risico's en aandachtspunten voor de coach, de sporter "
        "en de organisatie."
    )
    for i in range(0, len(RISKS), 2):
        kolommen = st.columns(2)
        for kol, (titel, niveau, items) in zip(kolommen, RISKS[i:i + 2]):
            tekst = f"**{titel}**\n\n" + "\n".join(f"- {x}" for x in items)
            with kol:
                getattr(st, niveau)(tekst)


def scherm_next():
    st.subheader("Next Steps")
    st.write(
        "Gebruik de feedback uit dit prototype om te bepalen wat straks in de kennislaag "
        "en de live chatapp hoort."
    )
    for nummer, (titel, tekst) in enumerate(ROADMAP, start=1):
        st.markdown(f"**{nummer}. {titel}**")
        st.caption(tekst)

    kol1, kol2 = st.columns(2)
    with kol1:
        st.markdown("**Tijdlijn**")
        st.table(pd.DataFrame({"Fase": TIJDLIJN}))
    with kol2:
        st.markdown("**Succesmetingen**")
        st.table(pd.DataFrame({"Meting": SUCCESMETINGEN}))

    st.markdown("##### Feedback op dit prototype")
    st.write(FEEDBACK_PROMPT)
    oordeel = st.radio("Jouw oordeel", ["Ja, nuttig", "Bijna", "Nog niet"],
                       horizontal=True, index=None, key="fb_oordeel")
    st.text_area("Wat moet er veranderen voordat dit naar een live app gaat?", key="fb_note")
    if oordeel:
        st.success(f"Vastgelegd: {oordeel}")


# ---------------------------------------------------------------------------
# OPBOUW VAN DE PAGINA
# ---------------------------------------------------------------------------

HUISSTIJL_CSS = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&display=swap');

  #MainMenu {visibility: hidden;}
  footer {visibility: hidden;}
  [data-testid="stToolbar"], [data-testid="stDecoration"] {display: none;}

  html, body, [class*="css"] { font-family: Helvetica, Arial, sans-serif; }
  .block-container { max-width: 960px; padding-top: 2.6rem; }
  h1, h2, h3, h4 { color: #2E276C; font-family: 'Poppins', Helvetica, Arial, sans-serif; }

  .som-kicker { color: #0089a8; font-weight: 700; font-size: .78rem; letter-spacing: .12em; text-transform: uppercase; }
  .som-title { font-family: 'Poppins', sans-serif; font-weight: 800; font-size: 1.8rem;
               line-height: 1.12; color: #2E276C; text-transform: uppercase; letter-spacing: .3px; margin: .12rem 0 0; }
  .som-sub { color: #5a5480; font-weight: 500; margin-top: .3rem; }
  .som-accent { height: 5px; background: #ED7C00; border-radius: 3px; margin: .7rem 0 1.4rem; }

  .stButton > button { border-radius: 10px; border: 1px solid #e6e3f0; font-weight: 600; color: #2E276C; }
  .stButton > button:hover { border-color: #ED7C00; color: #ED7C00; }

  /* chat-invoer prominent in beeld */
  [data-testid="stChatInput"] {
    border: 2px solid #ED7C00 !important;
    border-radius: 14px !important;
    background: #ffffff !important;
    box-shadow: 0 8px 26px rgba(46,39,108,0.16) !important;
    max-width: 960px !important;
    margin-left: auto !important;
    margin-right: auto !important;
  }
  [data-testid="stChatInput"] > div,
  [data-testid="stChatInput"] [data-baseweb="base-input"],
  [data-testid="stChatInput"] [data-baseweb="textarea"] {
    border: none !important; background: transparent !important; box-shadow: none !important;
  }
  [data-testid="stChatInput"] textarea { font-size: 1.05rem !important; }
  [data-testid="stChatInputSubmitButton"] { color: #ED7C00 !important; }
  /* invoerbalk uitlijnen met de content i.p.v. de volle schermbreedte */
  [data-testid="stBottom"] > div,
  [data-testid="stBottomBlockContainer"] { max-width: 992px; margin: 0 auto; }
  .stTabs [aria-selected="true"] { color: #ED7C00 !important; }
  .stTabs [data-baseweb="tab-highlight"] { background-color: #ED7C00 !important; }

  section[data-testid="stSidebar"] { border-right: 1px solid #e6e3f0; }
  .partner-cap { color: #8a86a3; font-size: .78rem; text-transform: uppercase; letter-spacing: .08em; }
  /* coach-quotes laten opvallen */
  [data-testid="stChatMessage"] blockquote, .stMarkdown blockquote {
    border-left: 4px solid #ED7C00; background: #fff7ef; border-radius: 6px;
    padding: .5rem .9rem; margin: .7rem 0; color: #2E276C; font-style: italic;
  }
</style>
"""

st.set_page_config(page_title=PROJECT, page_icon="🧭", layout="wide",
                   initial_sidebar_state="collapsed")

st.markdown(HUISSTIJL_CSS, unsafe_allow_html=True)

# --- SOM-kop: Thialf Innovatielab prominent ---
_ASSETS = Path(__file__).resolve().parent / "assets"
_kop = st.columns([1, 3], vertical_alignment="center")
with _kop[0]:
    _thialf = _ASSETS / "thialf-innovatielab.png"
    if _thialf.exists():
        st.image(str(_thialf), width=150)
with _kop[1]:
    st.markdown(
        "<div class='som-kicker'>Sportmonitor op Maat</div>"
        f"<div class='som-title'>{PROJECT}</div>"
        "<div class='som-sub'>Denkt met je mee over monitoring, training en herstel — de coach beslist.</div>",
        unsafe_allow_html=True,
    )
st.markdown("<div class='som-accent'></div>", unsafe_allow_html=True)

# Verstopt instellingenblok (API-sleutel, model) — ingeklapt op de pagina.
api_key, model = instellingen()

# --- Secundair (boven de chat): projectverhaal, ingeklapt ---
# Bewust bóven de chat, zodat het invoerveld onderaan altijd bereikbaar blijft.
with st.expander("ℹ️ Over dit prototype — uitdaging, aannames, risico's, next steps"):
    _t1, _t2, _t3, _t4 = st.tabs(["Uitdaging", "Aannames", "Wat kan er misgaan?", "Next Steps"])
    with _t1:
        scherm_uitdaging()
    with _t2:
        scherm_aannames()
    with _t3:
        scherm_risicos()
    with _t4:
        scherm_next()
    st.caption("Een initiatief vanuit Innovatielab Thialf, in samenwerking met "
               "Hanzehogeschool Groningen en Fontys.")

st.markdown("<div class='som-accent' style='opacity:.5; margin:.4rem 0 1rem'></div>",
            unsafe_allow_html=True)

# --- HOOFDSCHERM: de chat is het laatste element; het invoerveld zit onderaan vast ---
scherm_demo(api_key, model)
