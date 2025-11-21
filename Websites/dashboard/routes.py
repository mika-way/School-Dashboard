#Import Flask
from flask import render_template
from . import dashboard_blueprint

#Erstellt die Verbindung zur HTML Datei her
@dashboard_blueprint.route('/')
def index():
    # Es gibt die Rollen (z.B. Admin, Teacher, Student) an die HTML Datei weiter.
    role = "guest" # Standart Rolle für nicht angemeldete Benutzer

    username = None  # Standardmäßig kein Benutzername

    return render_template('dashboard.html', 
                           role = role, 
                           username = username)