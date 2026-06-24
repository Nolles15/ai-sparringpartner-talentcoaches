# SOM-huisstijl (toegepast in de app)

Bron: officiële stylegids "Sportmonitor op Maat" (Phanatique).

## Kleuren
| Rol | HEX |
|---|---|
| Primair oranje (accent) | `#ED7C00` |
| Primair blauw (tekst/koppen) | `#2E276C` |
| Secundair teal | `#0089A8` |
| Secundair mint | `#66D4A1` |

Tinten: 80/60/40/20% van de primaire kleuren.

## Typografie
- Merkfont: **Gilroy** (koppen bij voorkeur dikgedrukt en in KAPITALEN).
- Tagline: *Powered by Coach in Control*.
- **Systeemfont/fallback (officieel): Helvetica.** → In de webapp gebruiken we Helvetica/Arial
  voor de tekst en een geometrische webfont (Poppins) voor de koppen, omdat Gilroy niet
  vrij op het web beschikbaar is. Heb je de Gilroy-fontbestanden, dan kunnen we die laden.

## Logo's in de app
- **Thialf Innovatielab** — prominent in de kop (thuisbasis van het project).
- **Hanze** en **Fontys** — subtiel onderaan als partners ("in samenwerking met").
- Bestanden staan in `assets/` (`thialf-innovatielab.png`, `hanze.png`, `fontys.jpg`).

## Toepassing in Streamlit
- Thema in `.streamlit/config.toml` (primair oranje, blauw, teal/mint).
- Eigen CSS in `app.py` (`HUISSTIJL_CSS`): vette caps-koppen, oranje accent-balk,
  afgeronde knoppen/kaarten, Streamlit-rommel verborgen.
- Lay-out is **chat-first**: de demo staat centraal; instellingen (API-key) zitten in de
  ingeklapte zijbalk; het projectverhaal staat secundair onder "Over dit prototype".
