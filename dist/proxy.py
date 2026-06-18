"""
Mini-proxy voor de live AI-demo (index.html).

Waarom: OpenAI staat geen rechtstreekse browser-aanroepen toe (CORS). Deze proxy
serveert index.html EN stuurt alle /v1/...-aanroepen server-naar-server door naar
OpenAI. De browser praat dus alleen met localhost (zelfde origin, geen CORS).

Je API-key blijft in de pagina: hij wordt per request in de Authorization-header
meegestuurd en hier alleen doorgegeven. Niets wordt opgeslagen of gelogd.

Gebruik:
    cd dist
    python proxy.py
Open daarna in je browser:  http://localhost:8000

Alleen de Python-standaardbibliotheek nodig — niets te installeren.
"""

import http.server
import socketserver
import urllib.request
import urllib.error
from pathlib import Path

PORT = 8000
OPENAI_BASE = "https://api.openai.com"
DIST_DIR = Path(__file__).resolve().parent


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Serveer de bestanden uit de map waar proxy.py staat (dist/).
        super().__init__(*args, directory=str(DIST_DIR), **kwargs)

    def do_OPTIONS(self):
        # Defensief: CORS-preflight netjes beantwoorden (zelfde origin heeft dit
        # meestal niet nodig, maar het kan geen kwaad).
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "authorization, content-type")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.end_headers()

    def do_POST(self):
        if not self.path.startswith("/v1/"):
            self.send_error(404, "Alleen /v1/... wordt doorgestuurd")
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length) if length else b""

        upstream = urllib.request.Request(
            OPENAI_BASE + self.path,
            data=body,
            method="POST",
        )
        upstream.add_header("Content-Type", self.headers.get("Content-Type", "application/json"))
        auth = self.headers.get("Authorization")
        if auth:
            upstream.add_header("Authorization", auth)

        try:
            with urllib.request.urlopen(upstream, timeout=60) as resp:
                status, data = resp.status, resp.read()
        except urllib.error.HTTPError as e:
            # Fouten van OpenAI (bv. 401, 429) onveranderd doorgeven aan de pagina.
            status, data = e.code, e.read()
        except Exception as e:
            status, data = 502, str(e).encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args):
        pass  # stil houden; geen request-logging (privacy)


if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"Demo draait op http://localhost:{PORT}  (Ctrl+C om te stoppen)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nGestopt.")
