#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
./app/main.py

Hier beginnt deine eigentliche Anwendung.
Alle Konfigurationen aus .env sind jetzt über os.getenv() verfügbar.
"""

import os

from app.logging_utils import get_logger

log = get_logger(__name__)


def main():
    """
    Hier liegen die Dateien für die primäre Logik der Anwendung
    Diese Information hier stammt aus der datei ./app/__init__.py
    """
    # Hole APP_MODE aus der .env
    mode = os.getenv("APP_MODE", "DEVEL")

    # Testausgabe:
    print(f"[APP] 🚀 Starte Anwendung im Modus: {mode}")
    print("[APP] 📦 -= Hello, world! =-")


def logtest():
    """
    wirft testweise alle Logvarianten aus.
    """

    print(f"\n[IFO] 📰 Loglevel: aus .env: {os.getenv('LOGFILE')}\n")
    log.info("Template ready.")
    log.debug("Dies ist eine Debug-Meldung.")
    log.warning("Dies ist eine Warnung.")
    log.error("Dies ist eine Fehlermeldung.")
    log.critical("Dies ist eine kritische Meldung.")
