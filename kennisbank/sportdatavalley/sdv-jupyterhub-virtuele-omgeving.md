# Een virtuele omgeving maken in JupyterHub

Voor: onderzoekers/Premium-research accounts. Onderdeel van SportData Valley: analyseren (JupyterHub).

Zo maak je een virtuele Python-omgeving aan:

1. **Open de terminal.** Klik op het grote plus-icoon linksboven en selecteer daarna het terminal-icoon.
2. **Maak de virtuele omgeving aan** met het commando:
   `python -m venv sample-project`
   Dit maakt een map "sample-project" met een nieuwe Python-omgeving.
3. **Activeer de omgeving:**
   `source sample-project/bin/activate`
4. **Installeer (optioneel) extra packages**, bijvoorbeeld:
   `pip install numpy pandas`
   Let op: het installeren van packages vanuit notebooks werkt niet met virtuele omgevingen.
5. **Registreer de omgeving als Jupyter-kernel.** Installeer eerst ipykernel:
   `pip install ipykernel`
   Voer daarna uit:
   `python -m ipykernel install --user --name=sample-project`
   De omgeving verschijnt nu als kerneloptie in notebooks.

Kernel verwijderen:
`jupyter kernelspec uninstall sample-project`

Bron: https://tutorial.sportdatavalley.nl/jupyter-hub/creeer-een-virtuele-omgeving-in-jupyter-hub/
