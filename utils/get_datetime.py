from datetime import datetime

def get_current_datetime():
    #Gibt das aktuelle Datum und die Uhrzeit im Format 'YYYY-MM-DD HH:MM:SS' zurück.
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')