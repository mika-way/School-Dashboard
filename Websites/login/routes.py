#Import Flask
from flask import render_template
from . import login_blueprint

#Importiere das Formular
from forms.Login_Form import LoginForm

#Erstellt die Verbindung zur HTML Datei her
@login_blueprint.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    return render_template('login.html', 
                           form=form)