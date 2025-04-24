# CHANGELOG - Python Template

- [CHANGELOG - Python Template](#changelog---python-template)
  - [2025-04-24 - Commit v1.0.1](#2025-04-24---commit-v101)
  - [2025-04-22 - Release v1.0.0](#2025-04-22---release-v100)

## 2025-04-24 - Commit v1.0.1  

- **Geändert:**  
  - [X] `README.md` stilistisch überarbeitet.
  - [x] `.json` in `.jsonc` umbenannt wenn sie Kommentare enthalten. Betrifft nur den .vscode teil und hat mit dem Template nicht direkt etwas zutun.  
  - [x] Im zentralen Logging-Modul `logging_utils.py` wird bei aktiviertem `DEBUG`-Level nun der Pfad zur Logdatei (`LOGFILE`) im Log ausgegeben. Die Ausgabe erfolgt nur, wenn `logger.isEnabledFor(logging.DEBUG)` zutrifft. Fehler bei der Pfadauflösung (`resolve()`) werden dabei abgefangen und blockieren das Logging nicht.  
  - [x] Standardpfad für Logdatei eingeführt: Wird `LOGFILE` nicht über die `.env` gesetzt, wird nun automatisch `"log/app.log"` verwendet. Damit funktioniert das Logging-Modul auch ohne `.env`-Konfiguration direkt nach dem Klonen oder bei lokalen Tests.  
  - [x] `CHANGELOG.md` erstellt.  

## 2025-04-22 - Release v1.0.0  

- **Release 1.0.0** 🚀  
