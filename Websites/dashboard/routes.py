#Import Flask
from flask import render_template
from flask_login import current_user
from . import dashboard_blueprint

#Erstellt die Verbindung zur HTML Datei her
@dashboard_blueprint.route('/')
def index():
    # Überprüft, ob der Benutzer eingeloggt ist und holt den Benutzernamen
    if current_user.is_authenticated:
        username = current_user.username
    else:
        username = None # Standardmäßig kein Benutzername

    return render_template('dashboard.html', 
                           username = username)