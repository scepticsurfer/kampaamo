# Entry point for the application.
import os
from threading import Thread
from . import app    # For application discovery by the 'flask' command.
# from . import views  # For import side-effects of setting up routes.
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms.fields.html5 import EmailField
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message
from dotenv import load_dotenv
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for,flash

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

# app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://'+os.environ.get('MYSQL_USER')+':'+os.environ.get('MYSQL_PASSWORD')+'@'+os.environ.get('MYSQL_HOST')+'/'+os.environ.get('MYSQL_DB')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(128))
    name = db.Column(db.String(64), unique=True, index=True)
    password_hash= db.Column(db.String(128))
    is_active=db.Column(db.Enum)
    admin=db.Column(db.Enum)
    hairdresser=db.Column(db.Enum)
    #role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                               Email()])
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Usernames must have only letters, numbers, dots or '
               'underscores')])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('Username already in use.')

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
                 
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)#, Role=Role)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route("/")
def index():
    return render_template("app/index.html")#у этого файла путь указан правильно

#@app.route('/', methods=['GET', 'POST'])
#def index():
#    form = RegistrationForm()
#    if form.validate_on_submit():
#        user = User.query.filter_by(name=form.username.data).first()
        
#        if user is None:
#            user = User(name=form.username.data)
#            db.session.add(user)
#            db.session.commit()
#            session['known'] = False
#            # if app.config['FLASKY_ADMIN']:
#            send_email(form.email.data, 'New User',
#                           'mail/new_user', user=user)
#        else:
#            session['known'] = True
#        session['name'] = form.name.data
#        return redirect(url_for('index'))
#    return render_template('index.html', form=form, name=session.get('name'),
#                           known=session.get('known', False))


@app.route("/company/company/") 
def company():
    return render_template("company/company.html")

@app.route("/trainers/trainers/") 
def trainers():
    return render_template("trainers/trainers.html")

@app.route("/contacts/feedback/")#как прописать путь к папке???
def feedback():
    return render_template("contacts/feedback.html")

@app.route("/auth/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                        name=form.username.data,
                        password_hash=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You can now login.')
        return redirect(url_for('templates/auth.login'))
    return render_template("auth/register.html", form=form)
    