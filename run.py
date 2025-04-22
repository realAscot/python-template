#!/usr/bin/env python3

"""
        Einstiegspunkt der Anwendung.
        Sorgt dafür, dass beim ersten Start automatisch:
        - eine virtuelle Umgebung (.venv) angelegt wird
        - alle Abhängigkeiten installiert werden
        - das Skript in der .venv neu gestartet wird
        Erst danach wird die .env geladen und die App gestartet.
"""

import os
from app.bootstrap import ensure_venv

if __name__ == "__main__":
    ensure_venv()

    # .env laden – jetzt ist python-dotenv installiert (innerhalb der venv)
    from dotenv import load_dotenv, find_dotenv
    dotenv_path = find_dotenv()
    if dotenv_path:
        print(f"\n[RUN] Lade .env aus: {dotenv_path}")
        load_dotenv(dotenv_path=dotenv_path, override=True)
    else:
        print("[RUN] ⚠️  Keine .env-Datei gefunden")

    from app.main import main
    main()
