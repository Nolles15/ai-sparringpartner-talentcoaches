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

ALLOWED_MODELS = ["gpt-5-nano", "gpt-5-mini"]

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
Je bent een AI-sparringpartner voor talentcoaches, ontwikkeld door de Hanzehogeschool Groningen (Lectoraat Sportinnovator / AI Impact Lab). Je ondersteunt het denkproces van de coach; je vervangt het niet. Je stelt geen diagnoses en neemt geen beslissingen — de coach blijft altijd de beslisser.

WIE IS DE GEBRUIKER
Een talentcoach die 10-20 jonge sporters (meestal <18) begeleidt in een RTC, talentteam of opleidingsploeg. Hij heeft domeinkennis en motivatie, maar geen data-analist of sportwetenschapper bij de hand. Hij gebruikt je ad hoc op smartphone of laptop, vaak tussen trainingen door en met weinig tijd.

WAT IS EEN GOED ANTWOORD
- Schrijf in het Nederlands en praat als een ervaren collega-coach die even meedenkt — niet als een medisch rapport of een stappenplan.
- Hou het kort en in spreektaal: meestal 80-150 woorden. Liever een paar korte alinea's dan een lange opsomming; gebruik hooguit één kort lijstje.
- Vermijd vakjargon en afkortingen (zoals SRPE, TQR, RPE). Moet je een term echt gebruiken, leg 'm dan in een paar woorden uit.
- Geef één of twee concrete, bruikbare tips — geen uitputtende checklist.
- Gaat de vraag over een praktische handeling in SportData Valley (vragenlijsten uitzetten, groepen, dashboards, data delen, apparaten koppelen) en staat die in de meegegeven kennis? Leg dan concreet uit hoe de coach dit in SportData Valley doet — hier mag een kort stappenlijstje wel.
- Reageer als sparringpartner: een perspectief of overweging, geen definitief oordeel.
- Is de vraag vaag of mist er context? Stel dan eerst één verhelderende tegenvraag voordat je inhoudelijk reageert.
- Sluit af met één concrete vervolgstap of vervolgvraag. 'Nog even afwachten' of 'dat weet ik niet zeker' mag — dring geen kunstmatige conclusie op.

GRONDING — BLIJF IN LIJN MET DE KENNIS
- Baseer je inhoudelijke antwoorden op (a) de kennis die hieronder is meegegeven en (b) de context die de coach in dit gesprek geeft.
- Je mag samenvatten, combineren en redeneren, maar blijf in lijn met de strekking van die kennis; voeg geen feiten, cijfers of richtlijnen toe die er niet uit volgen.
- Verwijs kort en leesbaar naar waar je je op baseert (het onderwerp of de bron), in gewone taal — niet met ruwe bestandsnamen of losse codes midden in de tekst.
- Vind je in de meegegeven kennis geen onderbouwing? Zeg dat dan eerlijk, bijvoorbeeld: "Daar heb ik geen kennis over." Gok of verzin nooit feiten of bronnen.
- Is bewijs dun, tegenstrijdig of niet van toepassing op de doelgroep (vrouwen, jongeren <18)? Benoem die onzekerheid in plaats van stelliger te klinken dan kan.

GRENZEN
- Medisch: bij klachten, blessures of symptomen loop je eerst het afwegingskader langs (welke signalen, hoe lang al, pijn in rust of bij belasting?) en verwijs je daarna door naar sportarts of fysiotherapeut. Geen medisch advies.
- SportData Valley (SDV) is het systeem dat deze coaches gebruiken. Je hebt zelf geen toegang tot hun eigen data in SDV en analyseert die niet — maar als de meegegeven kennis SDV-instructies bevat, leg dan concreet uit hoe de coach iets in SportData Valley doet (de juiste stappen, menu's en knoppen). Benoem dat het uit de SDV-tutorial komt.
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


def sidebar_config():
    """Zijbalk: API key (met .env-fallback), modelkeuze en gespreksbeheer."""
    st.sidebar.header("AI-instellingen")
    key_veld = st.sidebar.text_input(
        "OpenAI API key", type="password",
        help="Wordt niet opgeslagen. Laat leeg om OPENAI_API_KEY uit .env te gebruiken.",
    )
    model = st.sidebar.selectbox("Model", ALLOWED_MODELS, index=1)  # standaard gpt-5-mini

    # Key uit het veld; valt terug op .env (OPENAI_API_KEY). Nooit hardcoded.
    api_key = key_veld or os.getenv("OPENAI_API_KEY", "")
    if api_key and key_veld:
        st.sidebar.caption("✅ API key uit het veld")
    elif api_key:
        st.sidebar.caption("✅ API key uit .env")
    else:
        st.sidebar.caption("⚠️ Nog geen API key — vul er een in of zet OPENAI_API_KEY in .env")

    st.sidebar.divider()
    st.sidebar.subheader("Kennisbank")
    kb = rag.index_status()
    if kb["bestaat"]:
        extra = "" if kb["actueel"] else " · gewijzigd, herindexeer"
        st.sidebar.caption(f"📚 {kb['stukjes']} stukjes geïndexeerd{extra}")
    else:
        st.sidebar.caption("📚 Nog niet geïndexeerd")
    if st.sidebar.button("🔄 Herindexeer kennisbank"):
        if not api_key:
            st.sidebar.warning("Een API-key is nodig om te indexeren.")
        else:
            with st.spinner("Kennisbank indexeren..."):
                try:
                    stats = rag.bouw_index(api_key)
                    st.sidebar.success(
                        f"Klaar: {stats['documenten']} documenten, {stats['stukjes']} stukjes.")
                except Exception as fout:
                    st.sidebar.error(f"Indexeren mislukt: {fout}")

    st.sidebar.divider()
    if st.sidebar.button("🗑️ Nieuw gesprek"):
        st.session_state.messages = []
        st.rerun()
    st.sidebar.caption("Privacy: typ geen namen of herleidbare gegevens van sporters in.")
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


def toon_bronnen(stukjes):
    """Laat zien welke stukjes uit de kennisbank achter een antwoord zaten."""
    if not stukjes:
        return
    with st.expander(f"📚 Bronnen achter dit antwoord ({len(stukjes)})"):
        for s in stukjes:
            st.markdown(f"**{s['bron']}**  ·  _relevantie {s['score']}_")
            fragment = s["tekst"][:300] + ("…" if len(s["tekst"]) > 300 else "")
            st.caption(fragment)


def scherm_demo(api_key, model):
    st.subheader("Interactieve Demo")
    st.caption("live AI — gebaseerd op jullie eigen kennisbank")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    kb = rag.index_status()
    if not kb["bestaat"]:
        st.info("De kennisbank is nog niet geïndexeerd. Klik links op 'Herindexeer "
                "kennisbank' (API-key nodig). Tot die tijd gebruikt de AI de vaste "
                "kennisdomeinen als terugval.")
    elif not kb["actueel"]:
        st.warning("De kennisbank is gewijzigd sinds de laatste indexering. Klik links op "
                   "'Herindexeer kennisbank' om de nieuwste documenten mee te nemen.")

    # Lege chat: voorbeeldsituaties om te starten, alleen als er nog geen gesprek loopt.
    if not st.session_state.messages and "_pending" not in st.session_state:
        st.caption("Stel je eigen vraag hieronder, of kies een voorbeeldsituatie om te starten:")
        kolommen = st.columns(len(SCENARIOS))
        for kol, (label, sc) in zip(kolommen, SCENARIOS.items()):
            if kol.button(label, key=f"voorbeeld::{label}"):
                st.session_state._pending = sc["question"]
                st.rerun()

    # Gespreksgeschiedenis tonen (met bronnen onder de AI-antwoorden).
    for bericht in st.session_state.messages:
        with st.chat_message(bericht["role"]):
            st.write(bericht["content"])
            toon_bronnen(bericht.get("bronnen"))

    # Nieuwe vraag: uit het invoerveld of uit een aangeklikte voorbeeldknop.
    vraag = st.chat_input("Beschrijf je situatie of stel je vraag...")
    vraag = vraag or st.session_state.pop("_pending", None)

    if vraag:
        if not api_key:
            st.warning("Vul links in de zijbalk eerst je OpenAI API key in.")
            return
        st.session_state.messages.append({"role": "user", "content": vraag})
        with st.chat_message("user"):
            st.write(vraag)
        with st.chat_message("assistant"):
            with st.spinner("De sparringpartner zoekt in de kennisbank en denkt na..."):
                try:
                    stukjes = rag.zoek(api_key, vraag, k=5)
                except Exception:
                    stukjes = []  # bij een zoekfout vallen we terug op de vaste domeinen
                systeemprompt = bouw_systeemprompt(stukjes)
                antwoord, foutmelding = vraag_llm(
                    api_key, model, st.session_state.messages, systeemprompt)
            if foutmelding:
                st.error(foutmelding)
            else:
                st.write(antwoord)
                toon_bronnen(stukjes)
                st.session_state.messages.append(
                    {"role": "assistant", "content": antwoord, "bronnen": stukjes})


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
  #MainMenu, footer {visibility: hidden;}
  [data-testid="stToolbar"], [data-testid="stDecoration"] {display: none;}
  html, body, [class*="css"] { font-family: "Trebuchet MS", "Segoe UI", sans-serif; }
  h1, h2, h3, h4 { color: #2E276C; }
  .hz-band { border-bottom: 3px solid #ED7C00; padding-bottom: .4rem; margin-bottom: 1rem; }
  .stTabs [aria-selected="true"] { color: #ED7C00 !important; }
  .stTabs [data-baseweb="tab-highlight"] { background-color: #ED7C00 !important; }
  .stButton > button { border-radius: 8px; }
  section[data-testid="stSidebar"] { border-right: 1px solid #e6e3f0; }
</style>
"""

st.set_page_config(page_title=PROJECT, page_icon="🧭", layout="wide",
                   initial_sidebar_state="expanded")

_LOGO = Path(__file__).resolve().parent / "assets" / "sportinnovator-ai-lab-logo.png"
if _LOGO.exists():
    st.logo(str(_LOGO))

st.markdown(HUISSTIJL_CSS, unsafe_allow_html=True)

api_key, model = sidebar_config()

st.markdown(
    f"<div class='hz-band'><h1 style='margin:0'>{PROJECT}</h1>"
    f"<p style='color:#0089a8; margin:.2rem 0 0; font-weight:600'>"
    f"{ORGANISATIE} · AI Impact Lab</p></div>",
    unsafe_allow_html=True,
)

tab_uitdaging, tab_aannames, tab_demo, tab_risicos, tab_next = st.tabs(NAV)

with tab_uitdaging:
    scherm_uitdaging()
with tab_aannames:
    scherm_aannames()
with tab_demo:
    scherm_demo(api_key, model)
with tab_risicos:
    scherm_risicos()
with tab_next:
    scherm_next()
