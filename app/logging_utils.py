#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Zentrales Logging-Modul
→ Unterstützt LOGLEVEL und LOGFILE aus der .env
→ Plattformunabhängig (Windows/Linux)
→ Erstellt automatisch das Log-Verzeichnis bei Bedarf
→ Fällt bei ungültigem Log-Level sicher auf INFO zurück
"""

import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path


def safe_log_level(level_str: str) -> int:
    """Wandelt einen Level-String in einen gültigen Logging-Level um."""
    levels = {
        "CRITICAL": logging.CRITICAL,
        "ERROR": logging.ERROR,
        "WARNING": logging.WARNING,
        "INFO": logging.INFO,
        "DEBUG": logging.DEBUG,
        "NOTSET": logging.NOTSET,
    }
    return levels.get(level_str.upper(), logging.INFO)


LOGLEVEL = safe_log_level(os.getenv("LOGLEVEL", "INFO"))
LOGFILE = os.getenv("LOGFILE", "log/app.log")  # z. B. logs/app.log


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger  # Logger bereits konfiguriert

    logger.setLevel(LOGLEVEL)

    formatter = logging.Formatter("[%(asctime)s] %(levelname)s %(name)s: %(message)s")

    # Konsole
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Datei (optional)
    if LOGFILE:
        logfile_path = Path(LOGFILE)

        # Debug: Logpfad anzeigen (nur bei DEBUG)
        if logger.isEnabledFor(logging.DEBUG):
            try:
                logger.debug(f"Logdatei: {logfile_path.resolve()}")
            except Exception:
                pass  # Debug-Ausgabe darf nicht blockieren

        try:
            logfile_path.parent.mkdir(parents=True, exist_ok=True)
            file_handler = RotatingFileHandler(
                logfile_path, maxBytes=1_000_000, backupCount=3, encoding="utf-8"
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except Exception as e:
            logger.warning(f"Konnte Logdatei nicht schreiben: {e}")

    return logger
