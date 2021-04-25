from flask import render_template
from . import main
from flask import jsonify
from ..models import User#, Service,
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
from .forms import FindClientServiceForm, BookTimeServiceForm, FindAdminServiceForm, AddAdminServiceForm
from flask_login import current_user
from flask import request
from ..email import send_email
from flask import current_app
#import os
#from dotenv import load_dotenv
#basedir = os.path.abspath(os.path.dirname(__file__))
#load_dotenv(os.path.join(basedir, '.env'))
#app = current_app 
#app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')
 
# class Empty(object):
    # pass

@main.route('/')
def index():
    return render_template('index.html')

@main.route("/company/company/") 
def company():
    return render_template("company/company.html")

@main.route("/trainers/trainers/") 
def trainers():
    return render_template("trainers/trainers.html")

@main.route("/contacts/feedback/")
def feedback():
    return render_template("contacts/feedback.html")
    
@main.route("/customers/client_page/")
def client_page():
    form = FindClientServiceForm ()
    return render_template("customers/client_page.html", form=form)    

@main.route("/customers/client_page/getClientServices.json") 
def getClientServices():
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    if current_user:
        user_id=current_user.id
        # return jsonify(user_id)
    db = SQLAlchemy()
    sql = text("SELECT `date`,`time`,service_name,`username`, service_registration.id FROM service_registration \
                LEFT JOIN services ON service_registration.service_id=services.id \
                LEFT JOIN users ON service_registration.hairdresser_id=users.id \
                WHERE client_id=" + str(user_id) + " AND `date`>='" + date_from + "' AND `date`<= '" + date_to +  "'")
    result = db.engine.execute(sql)

    response = []
    for row in result:
        response.append({
            "id": str(row.id),
            "date": str(row.date),
            "time": str(row.time),
            "service_name":str(row.service_name),
            "username":str(row.username)
        })
    return (jsonify(response))
    # return jsonify([(dict(row.items())) for row in result])


@main.route("/customers/client_page/cancelReservation.json") 
def cancelReservation():
    result_1 = "true"
    db = SQLAlchemy()
    cancel_id= request.args.get('cancel_id')
    master_name= request.args.get('master')
    sql_get="SELECT *  FROM service_registration WHERE `id`='" + str(cancel_id) + "'"
    result = db.engine.execute(sql_get)

    for row in result:
        date=row.date
        time=row.time
        service_id=row.service_id
        hairdresser_id=row.hairdresser_id

    sql_insert = "INSERT INTO service_timetable(`date`, `time`, service_id, hairdresser_id  ) VALUES ('" + str(date) + "','" + str(time) + "','" + str(service_id) + "','" + str(hairdresser_id) + "')"
    result_insert = db.engine.execute(sql_insert) 

    sql_delete="DELETE FROM service_registration WHERE `id`='" + str(cancel_id) + "'"
    result_delete = db.engine.execute(sql_delete)
    # app = current_app 
   # send_email(app.config['FLASKY_ADMIN'], 'Client canceled reservation',
   
    send_email('carie@mail.ru', 'Client canceled reservation',
                   'auth/email/client_cancel', date=date, time=time, master=request.args.get('master'), username=current_user.username)
               
    return (jsonify(result_1))
   

    
    
    
    
@main.route("/customers/reservation/")
def reservation():
    form = BookTimeServiceForm ()
    return render_template("customers/reservation.html", form=form) 

@main.route("/admins/admin_page/")
def admin_page():
    form = FindAdminServiceForm ()
    return render_template("admins/admin_page.html", form=form)

@main.route("/admins/new_change_workout/")
def new_change_workout():
    form = AddAdminServiceForm ()
    return render_template("admins/new_change_workout.html", form=form)  
