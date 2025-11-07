#Import Flask
from flask import render_template
from . import page_not_found_blueprint

#Erstellt die Verbindung zur HTML Datei her
@page_not_found_blueprint.route('/')
def index():
    return render_template('page_not_found.html')