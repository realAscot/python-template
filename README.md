# Python Bootstrap-Template mit `.venv` und `.env` Support

Dieses Projekt bietet ein portables Start-Template für Python-Anwendungen mit folgenden Features:  

- Automatische Erstellung einer virtuellen Umgebung (`.venv`)  
- Automatische Installation von Abhängigkeiten aus `requirements.txt`  
- Automatischer Neustart in der virtuellen Umgebung  
- Unterstützung von Umgebungsvariablen über eine `.env`-Datei  
- Sauberer Einstiegspunkt über `run.py`  
- Keine systemweiten Python-Pakete notwendig  

---

- [Python Bootstrap-Template mit `.venv` und `.env` Support](#python-bootstrap-template-mit-venv-und-env-support)
  - [🔧 Projektstruktur](#-projektstruktur)
  - [🚀 Erste Schritte](#-erste-schritte)
    - [Beim ersten Start passiert:](#beim-ersten-start-passiert)
  - [📦 Abhängigkeiten](#-abhängigkeiten)
  - [⚙️ .env-Datei (optional)](#️-env-datei-optional)
  - [📜 Beispielausgabe](#-beispielausgabe)
  - [🧼 Optional: `.env.example`](#-optional-envexample)
  - [🛠 Hinweise](#-hinweise)
  - [🧪 Getestet mit](#-getestet-mit)
  - [📁 Lizenz](#-lizenz)

---

## 🔧 Projektstruktur

```plaintext

template-root/
├── .env                # Projektkonfiguration (optional, wird automatisch geladen)
├── requirements.txt    # Abhängigkeiten (z. B. python-dotenv)
├── run.py              # Einstiegspunkt für die Anwendung
└── app/
    ├── __init__.py
    ├── main.py         # Hauptlogik der Anwendung
    └── bootstrap.py    # Setup- und Relaunch-Logik
```

---

## 🚀 Erste Schritte

```bash
python run.py
```

### Beim ersten Start passiert:

1. `.venv` wird erstellt (wenn noch nicht vorhanden)
2. `requirements.txt` wird installiert
3. Das Skript wird automatisch innerhalb der venv neu gestartet
4. `.env` wird geladen (falls vorhanden)
5. Die App startet

---

## 📦 Abhängigkeiten

Alle Abhängigkeiten werden aus `requirements.txt` installiert. Beispiel:

```text
python-dotenv
```

---

## ⚙️ .env-Datei (optional)

Wenn vorhanden, wird `.env` automatisch geladen. Beispiel:

```dotenv
APP_MODE=development
LOGLEVEL=debug
PORT=8080
```

Diese Werte sind im Code über `os.getenv("APP_MODE")` verfügbar.

---

## 📜 Beispielausgabe

```text
[BOOTSTRAP] Erstelle virtuelle Umgebung...
[BOOTSTRAP] Installiere pip + requirements.txt...
[BOOTSTRAP] Starte in virtueller Umgebung neu...
[RUN] Lade .env aus: ./cliqrcode/.env
[APP] Starte Anwendung im Modus: development
[APP] Hello, world!
```

---

## 🧼 Optional: `.env.example`

Erstelle eine `.env.example`, um deine Konfiguration zu dokumentieren:

```dotenv
APP_MODE=production
PORT=8000
LOGLEVEL=info
```

---

## 🛠 Hinweise

- Das Template ist portabel und benötigt keine global installierten Pakete.
- Du kannst es für jede neue App wiederverwenden.
- `run.py` ist der einzige Einstiegspunkt – keine direkten Aufrufe von `main.py`.

---

## 🧪 Getestet mit

- Python 3.11, 3.12, 3.13
- Windows & Linux
- VS Code, Terminal, PowerShell

---

## 📁 Lizenz

MIT – frei verwendbar in eigenen Projekten.