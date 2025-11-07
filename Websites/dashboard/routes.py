#Import Flask
from flask import render_template
from . import dashboard_blueprint

#Erstellt die Verbindung zur HTML Datei her
@dashboard_blueprint.route('/')
def index():
    return render_template('dashboard.html')