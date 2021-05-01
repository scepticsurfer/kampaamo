from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User
from wtforms.fields.html5 import TelField

class LoginForm(FlaskForm):    
    email = StringField('Sähköposti', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('Salasana', validators=[DataRequired()])
    remember_me = BooleanField('Muista minut')
    submit = SubmitField('Kirjaudu')

class RegistrationForm(FlaskForm):
    email = StringField('Sähköposti', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Etunimi Sukunimi', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Käyttäjänimissä pitää olla vain kirjaimet, numerot, pisteet tai '
               'alaviivat')]) 
    phone_number=TelField('Puhelinnumero',validators=[Regexp(r"[0-9]{3}\-[0-9]{3}\-[0-9]{4}")], render_kw={"placeholder": "123-456-7890"})

    password = PasswordField('Salasana', validators=[Regexp( r"^(?=.{8,32}$)(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*", message='Salasanassa täytyy olla 8-32 merkkiä, yksi tai useampia isoja ja pieniä kirjaimia, yksi tai useampi numero.'),
        DataRequired(), EqualTo('password2', message='Salasanojen täytyy täsmätä.')])
    password2 = PasswordField('Vahvista salasana', validators=[DataRequired()])
    submit = SubmitField('Luo tili')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Sähköposti on jo olemassa.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Käyttäjänimi on jo olemassa.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Vanha salasana', validators=[DataRequired()])
    password = PasswordField('Uusi salasana', validators=[
        DataRequired(), EqualTo('password2', message='Salasanojen täytyy täsmätä.')])
    password2 = PasswordField('Vahvista uusi salasana',
                              validators=[DataRequired()])
    submit = SubmitField('Vaihda salasana')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('Sähköposti', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Nollaa salasana')


class PasswordResetForm(FlaskForm):
    password = PasswordField('Uusi salasana', validators=[
        DataRequired(), EqualTo('password2', message='Salasanojen täytyy täsmätä')])
    password2 = PasswordField('Vahvista salasana', validators=[DataRequired()])
    submit = SubmitField('Päivitä salasana')


class ChangeEmailForm(FlaskForm):
    email = StringField('Uusi sähköposti', validators=[DataRequired(), Length(1, 64),
                                                 Email()])
    password = PasswordField('Salasana', validators=[DataRequired()])
    submit = SubmitField('Vaihda sähköposti')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Sähköposti on jo olemassa.')