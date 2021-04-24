from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateTimeLocalField, DateField



class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class FindClientServiceForm(FlaskForm):
    date_from = DateField('Alkaen')
    date_to = DateField('Saakka')
    submit = SubmitField('Valitse ajanjakso')
