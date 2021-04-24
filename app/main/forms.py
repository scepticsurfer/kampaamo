from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateTimeLocalField, DateField, TimeField



class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class FindClientServiceForm(FlaskForm):
    date_from = DateField('Alkaen')
    date_to = DateField('Saakka')
    submit = SubmitField('Valitse ajanjakso')

class BookTimeServiceForm(FlaskForm):
    date_from = DateField('Alkaen')
    date_to = DateField('Saakka')    
    service_titles = SelectField(
        'Palvelut',
        [DataRequired()],
        choices=[
            ('Farmer', 'farmer'),
            ('Corrupt Politician', 'politician'),
            ('No-nonsense City Cop', 'cop'),
            ('Professional Rocket League Player', 'rocket'),
            ('Lonely Guy At A Diner', 'lonely'),
            ('Pokemon Trainer', 'pokemon')
        ]
    )
    hairdresser = SelectField(
        'Osaajat',
        [DataRequired()],
        choices=[
            ('Farmer', 'farmer'),
            ('Corrupt Politician', 'politician'),
            ('No-nonsense City Cop', 'cop'),
            ('Professional Rocket League Player', 'rocket'),
            ('Lonely Guy At A Diner', 'lonely'),
            ('Pokemon Trainer', 'pokemon')
        ]
    )    
    submit = SubmitField('Selaa aikatauluja') 

class FindAdminServiceForm(FlaskForm):
    date_from = DateField('Alkaen')
    date_to = DateField('Saakka')
    service_titles = SelectField(
        'Palvelut',
        [DataRequired()],
        choices=[
            ('Farmer', 'farmer'),
            ('Corrupt Politician', 'politician'),
            ('No-nonsense City Cop', 'cop'),
            ('Professional Rocket League Player', 'rocket'),
            ('Lonely Guy At A Diner', 'lonely'),
            ('Pokemon Trainer', 'pokemon')
        ]
    )
    hairdresser = SelectField(
        'Osaajat',
        [DataRequired()],
        choices=[
            ('Farmer', 'farmer'),
            ('Corrupt Politician', 'politician'),
            ('No-nonsense City Cop', 'cop'),
            ('Professional Rocket League Player', 'rocket'),
            ('Lonely Guy At A Diner', 'lonely'),
            ('Pokemon Trainer', 'pokemon')
        ]
    )    
    submit = SubmitField('Selaa palvelujen aikatauluja') 

class AddAdminServiceForm(FlaskForm):
    service_id = StringField('ID')    
    date = DateField('Päivämäärä')
    time = TimeField('Ajankohta')
    service_titles = SelectField(
        'Palvelu',
        [DataRequired()],
        choices=[
            ('Farmer', 'farmer'),
            ('Corrupt Politician', 'politician'),
            ('No-nonsense City Cop', 'cop'),
            ('Professional Rocket League Player', 'rocket'),
            ('Lonely Guy At A Diner', 'lonely'),
            ('Pokemon Trainer', 'pokemon')
        ]
    )
    hairdresser = SelectField(
        'Osaaja',
        [DataRequired()],
        choices=[
            ('Farmer', 'farmer'),
            ('Corrupt Politician', 'politician'),
            ('No-nonsense City Cop', 'cop'),
            ('Professional Rocket League Player', 'rocket'),
            ('Lonely Guy At A Diner', 'lonely'),
            ('Pokemon Trainer', 'pokemon')
        ]
    )
    status = SelectField(
        'Tila',
        [DataRequired()],
        choices=[
            ('Farmer', 'farmer'),
            ('Corrupt Politician', 'politician'),
            ('No-nonsense City Cop', 'cop')           
        ]
    ) 
    submit = SubmitField('Muokaa/Lisää')       