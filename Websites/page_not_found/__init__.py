#Import Blueprint
from flask import Blueprint

#Blueprint erstellen
page_not_found_blueprint = Blueprint("page_not_found", __name__, template_folder='templates', static_folder='static')

#Impotiert alles Wichtige von routes.py
from . import routes