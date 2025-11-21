"""Modul: config_loader

Funktion: Dieses Modul ist für das sichere Laden kritischer Konfigurationsvariablen aus einer `.env`-Datei in die Laufzeitumgebung der Anwendung verantwortlich.

Prozess:
1.  Es importiert `load_dotenv` zur Aktivierung der `.env`-Datei.
2.  Es ruft anschließend spezifische Schlüssel wie `SECRET_KEY` und `MONGO_URI` über `os.getenv()` ab.

Zweck: Gewährleistung der Trennung von Code und sensiblen Konfigurationsdaten.
"""

#Import der notwendigen Module
import os
import json
from dotenv import load_dotenv

#Stellt sicher, dass die Umgebungsvariablen aus der .env-Datei geladen werden
load_dotenv() 

#Enthält den zentralen kryptografischen Schlüssel der Anwendung, geladen aus der Umgebungsvariable 'SECRET_KEY'.
secret_key = os.getenv("SECRET_KEY")

#Enthält die Verbindungszeichenkette für die MongoDB-Datenbank, geladen aus der Umgebungsvariable 'MONGO_URI'.
mongo_uri = os.getenv("MONGO_URI")

#Lädt die Debug-Einstellung aus der settings.json Datei
debug_mode = json.loads(open("configs/settings.json").read())["server"]["debug"]

def isConfig_loaded():
    """Überprüft, ob die kritischen Konfigurationsvariablen geladen wurden."""
    isKey_loaded()
    isJsonloaded()



#Eine Warnung falls ein Umgebungsschlüssel nicht geladen werden konnte.
def isKey_loaded():
    if not secret_key or not mongo_uri:
        print("WARNUNG: Mindestens ein kritischer Umgebungsschlüssel (SECRET_KEY oder MONGO_URI) konnte nicht geladen werden!")
    else:
        print("Alle kritischen Umgebungsschlüssel wurden erfolgreich geladen.")

def isJsonloaded():
    #Eine Warnung falls die settings.json Datei nicht geladen werden konnte.
    try:
        json.loads(open("configs/settings.json").read())
        print("Die settings.json Datei wurde erfolgreich geladen.")
    except:
        print("WARNUNG: Die settings.json Datei konnte nicht geladen werden oder ist fehlerhaft!")