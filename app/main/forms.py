from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateTimeLocalField, DateField, TimeField
from ..models import Service, User
from datetime import datetime, date
from wtforms import validators, ValidationError
from flask import flash

class FindClientServiceForm(FlaskForm):
    date_from = DateField('Alkaen')
    date_to = DateField('Saakka')
    submit = SubmitField('Valitse ajanjakso')

class BookTimeServiceForm(FlaskForm):
    date_from = DateField('Alkaen')
    date_to = DateField('Saakka')    
    service= SelectField(
        'Palvelut',
        #[DataRequired()],
        choices=[]
    )
    hairdresser = SelectField(
        'Osaajat',
        #[DataRequired()],
        choices=[]
    )    
    submit = SubmitField('Selaa aikatauluja') 

class FindAdminServiceForm(FlaskForm):
    date_from = DateField('Alkaen')
    date_to = DateField('Saakka')
    service = SelectField(
        'Palvelut',
        #[DataRequired()],
        choices=[]
    )
    hairdresser = SelectField(
        'Osaajat',
        #[DataRequired()],
        choices=[]
    )    
    submit = SubmitField('Selaa palvelujen aikatauluja') 

class AddAdminServiceForm(FlaskForm):
    #timetable_id = StringField('ID')    
    date = DateField('Päivämäärä',validators=[DataRequired()] )
    time = TimeField('Ajankohta',validators=[DataRequired()], format='%H:%M')
    service = SelectField(
        'Palvelu',
        validators=[DataRequired()],
        choices=[]
    )
    hairdresser = SelectField(
        'Osaaja',
        validators=[DataRequired()],
        choices=[]
    )
    #status = SelectField(
    #    'Tila',
    #    validators=[DataRequired()],
    #    choices=[
    #        ("", "---"),
    #        ('Done', 'Done'),
    #        ('Canceled', 'Canceled'),
    #        ('Future', 'Future')           
    #    ]
   # ) 
    submit = SubmitField('Lisää')    
   # def validate_date(self, field):
   #    if str(field.data) <= str(date.today()):
   #     raise ValidationError('Päivämäärä täyty olla myöhemmin kuin tänään.')
   # def validate_time(self, field):
   #     time_start = '08:00:00'
   #     time_finish ='22:00:00'
                             
    # if str(field.data) < str(time_start) and str(field.data) > str(time_finish)  :
    #        raise ValidationError('Aika täyty olla 8:00 ja 21:30 välillä.')  

class ChangeAdminServiceForm(FlaskForm):
    timetable_id = StringField('ID')    
    date = DateField('Päivämäärä',validators=[DataRequired()] )
    time = TimeField('Ajankohta',format='%H:%M',validators=[DataRequired()])
    service = SelectField(
        'Palvelu',
        validators=[DataRequired()],
        choices=[]
    )
    hairdresser = SelectField(
        'Osaaja',
        validators=[DataRequired()],
        choices=[]
    )
    status = SelectField(
        'Tila',
        validators=[DataRequired()],
        choices=[
            ("", "---"),
            ('Loppunut', 'Loppunut'),
            ('Peruutettu', 'Peruutettu'),
            ('Tuleva', 'Tuleva')           
        ]
    ) 
    submit = SubmitField('Muokaa')    
   # def validate_date(self, field):
   #    if str(field.data) <= str(date.today()):
   #     raise ValidationError('Päivämäärä täyty olla myöhemmin kuin tänään.')
   # def validate_time(self, field):
   #     time_start = '08:00:00'
   #     time_finish ='22:00:00'

    # if str(field.data) < str(time_start) and str(field.data) > str(time_finish)  :
    #        raise ValidationError('Aika täyty olla 8:00 ja 21:30 välillä.') 

class FeedbackForm(FlaskForm):
    username = StringField('Nimi', [validators.Required("Kirjoita nimesi.")]) 
    email = StringField('Sähköposti', [validators.Required("Kirjoita sähköpostisi."), validators.Email("Sähköpostiosoitteen muoto on virheellinen.")])
    subject = StringField('Aihe', [validators.Required("Kirjoita aihe.")])
    message = TextAreaField('Viesti', [validators.Required("Kirjoita viestisi.")])
    submit = SubmitField('Ota yhteyttä')     