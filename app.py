"""Tiny dependency-free server for Syed Yasir Ali's portfolio.

Run with:
    python app.py
Then open http://localhost:8000/portfolio.html
"""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent
PORT = int(os.environ.get("PORT", "8000"))


class PortfolioHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self.path = "/portfolio.html"
        super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()


if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", PORT), PortfolioHandler)
    print(f"Portfolio running at http://0.0.0.0:{PORT}/portfolio.html")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping portfolio server.")
    finally:
        server.server_close()
