
"""
Bootstrap-Modul für automatische Einrichtung und Start der App.
Dieses Modul stellt sicher, dass:
- eine .venv angelegt ist
- python -m pip install -r requirements.txt ausgeführt wurde
- das Skript in der .venv neu gestartet wird, falls nötig
"""

import os
import sys
import subprocess
from pathlib import Path

# Pfad zur virtuellen Umgebung im Projektverzeichnis
VENV_DIR = Path(__file__).resolve().parent.parent / ".venv"
# Pfad zum Python-Interpreter in der venv
PYTHON_EXE = VENV_DIR / ("Scripts" if os.name == "nt" else "bin") / "python"

def ensure_venv():
    """
    Prüft, ob die .venv existiert und ob das aktuelle Skript
    bereits innerhalb der venv ausgeführt wird.
    Falls nicht, wird:
    - die venv erstellt
    - requirements.txt installiert
    - das Skript in der venv neu gestartet
    """
    if os.environ.get("BOOTSTRAPPED") == "1":
        return  # Bereits innerhalb der .venv → nichts tun

    if not VENV_DIR.exists():
        _create_venv()

    if Path(sys.executable).resolve() != PYTHON_EXE.resolve():
        _relaunch()

def _create_venv():
    """
    Legt eine virtuelle Umgebung im Projektverzeichnis an
    und installiert alle Pakete aus requirements.txt.
    """
    print("[BOOTSTRAP] Erstelle virtuelle Umgebung...")
    subprocess.check_call([sys.executable, "-m", "venv", str(VENV_DIR)])

    print("[BOOTSTRAP] Installiere pip + requirements.txt...")
    subprocess.check_call([str(PYTHON_EXE), "-m", "pip", "install", "--upgrade", "pip"])

    req_file = Path(__file__).resolve().parent.parent / "requirements.txt"
    if req_file.exists():
        subprocess.check_call([str(PYTHON_EXE), "-m", "pip", "install", "-r", str(req_file)])
    else:
        print("[BOOTSTRAP] ⚠️  Keine requirements.txt gefunden – Installation übersprungen.")

def _relaunch():
    """
    Startet das Skript innerhalb der .venv neu.
    Verwendet os.execv(), um den Prozess vollständig zu ersetzen.
    """
    print("\n[BOOTSTRAP] Starte in virtueller Umgebung neu...")
    os.environ["BOOTSTRAPPED"] = "1"
    os.execv(str(PYTHON_EXE), [str(PYTHON_EXE)] + sys.argv)
