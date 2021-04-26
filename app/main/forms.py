from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateTimeLocalField, DateField, TimeField
from ..models import Service, User

class FindClientServiceForm(FlaskForm):
    date_from = DateField('Alkaen')
    date_to = DateField('Saakka')
    submit = SubmitField('Valitse ajanjakso')

class BookTimeServiceForm(FlaskForm):
    date_from = DateField('Alkaen')
    date_to = DateField('Saakka')    
    service= SelectField(
        'Palvelut',
        [DataRequired()],
        choices=[]
    )
    hairdresser = SelectField(
        'Osaajat',
        [DataRequired()],
        choices=[]
    )    
    submit = SubmitField('Selaa aikatauluja') 

class FindAdminServiceForm(FlaskForm):
    date_from = DateField('Alkaen')
    date_to = DateField('Saakka')
    service = SelectField(
        'Palvelut',
        [DataRequired()],
        choices=[]
    )
    hairdresser = SelectField(
        'Osaajat',
        [DataRequired()],
        choices=[]
    )    
    submit = SubmitField('Selaa palvelujen aikatauluja') 

class AddAdminServiceForm(FlaskForm):
    service_id = StringField('ID')    
    date = DateField('Päivämäärä')
    time = TimeField('Ajankohta')
    service = SelectField(
        'Palvelu',
        [DataRequired()],
        choices=[]
    )
    hairdresser = SelectField(
        'Osaaja',
        [DataRequired()],
        choices=[]
    )
    status = SelectField(
        'Tila',
        [DataRequired()],
        choices=[
            ('1', 'Future'),
            ('2', 'Done'),
            ('3', 'Canceled')           
        ]
    ) 
    submit = SubmitField('Muokaa/Lisää')    