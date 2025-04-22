
"""
Hier beginnt deine eigentliche Anwendung.
Alle Konfigurationen aus .env sind jetzt über os.getenv() verfügbar.
"""

import os

def main():
    mode = os.getenv("APP_MODE", "development")
    print(f"[APP] Starte Anwendung im Modus: {mode}")
    print("[APP] Hello, world!")
