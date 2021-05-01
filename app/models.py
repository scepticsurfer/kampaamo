from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from . import db, login_manager


#class Role(db.Model):
#    __tablename__ = 'roles'
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(64), unique=True)
#    users = db.relationship('User', backref='role', lazy='dynamic')

#    def __repr__(self):
#        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    phone_number=db.Column(db.String(15))
    password_hash = db.Column(db.String(128))
    admin = db.Column(db.Boolean, default=False)
    hairdresser = db.Column(db.Boolean, default=False)
    confirmed = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id}).decode('utf-8')

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id}).decode('utf-8')

    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        user = User.query.get(data.get('reset'))
        if user is None:
            return False
        user.password = new_password
        db.session.add(user)
        return True

    def generate_email_change_token(self, new_email, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps(
            {'change_email': self.id, 'new_email': new_email}).decode('utf-8')

    def change_email(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        db.session.add(self)
        return True

    def __repr__(self):
        return '<User %r>' % self.username


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(64), unique=True, index=True)
    price = db.Column(db.DECIMAL(5, 2))
    description = db.Column(db.String(256))

    def __repr__(self):
       return '<Service %r>' % self.service_name

class ServiceTimetable(db.Model):
    __tablename__ = 'service_timetable'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    time = db.Column(db.DateTime)
    service_id = db.Column(db.Integer)
    hairdresser_id =db.Column(db.Integer)
    status = db.Column(db.Enum('Done', 'Canceled','Future'))

    def __repr__(self):
        return '<ServiceTimetable %r>' % self.service_id     
class ServiceRegistration(db.Model):
    __tablename__ = 'service_registration'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    time = db.Column(db.DateTime)
    timetable_id = db.Column(db.Integer)
    service_id = db.Column(db.Integer)
    client_id = db.Column(db.Integer)
    hairdresser_id = db.Column(db.Integer)

    def __repr__(self):
        return '<ServiceRegistration %r>' % self.service_id

class HairdresserService(db.Model):
    __tablename__ = 'hairdresser_service'
    id = db.Column(db.Integer, primary_key=True)
    hairdresser_id= (db.Integer)
    service_id = db.Column(db.Integer)
    

    def __repr__(self):
        return '<ServiceRegistration %r>' % self.hairdresser_id 
class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    service_id = db.Column(db.Integer)
    client_id  =db.Column(db.Integer)
    hairdresser_id = db.Column(db.Integer)

    def __repr__(self):
        return '<ServiceRegistration %r>' % self.service_id


