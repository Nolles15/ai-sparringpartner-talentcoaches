# Data ophalen uit het SDV-platform (via code)

Voor: onderzoekers/ontwikkelaars. Onderdeel van SportData Valley: analyseren (JupyterHub / API).

Hiermee haal je via Python of R data uit een dataset op met behulp van de SDV-API.

Vooraf nodig: het ID-nummer van je dataset. Ga in het SDV-platform naar de **Data**-pagina, klik op de gewenste dataset en lees het ID-nummer uit de URL.

**Via Python:**
1. Importeer de bibliotheken `os`, `requests` en `pandas`.
2. Definieer de basis-URL: `https://app.sportdatavalley.nl/api/v1/`.
3. Haal je API-token op via `os.environ['SDV_AUTH_TOKEN']`.
4. Voer een GET-verzoek uit naar `base_url+'data/'+str(dataset_id)` met je authenticatie-header.
5. Controleer of het verzoek lukte met `response.raise_for_status()`.
6. Parse de respons naar JSON.

Het resultaat is een geneste lijst met alle data uit je dataset.

**Via R:**
1. Laad de bibliotheken `sdvclient` en `httr`.
2. Definieer dezelfde basis-URL en haal je `SDV_AUTH_TOKEN` op.
3. Gebruik de functie `get_metadata()` voor metagegevens.
4. Gebruik de functie `get_data()` om je data op te halen.

Bron: https://tutorial.sportdatavalley.nl/analyse/data-retrieval-from-the-sdv-platform/
