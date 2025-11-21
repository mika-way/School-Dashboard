#Import Flask
from flask import render_template
from . import register_student_blueprint

#Importiere das Formular
from forms.Register_Form import RegisterForm

#Erstellt die Verbindung zur HTML Datei her
@register_student_blueprint.route('/', methods=['GET', 'POST'])
def index():
    form = RegisterForm()
    return render_template('register_student.html', 
                           form=form)