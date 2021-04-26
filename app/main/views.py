from flask import render_template
from . import main
from flask import jsonify
from ..models import User, Service, ServiceTimetable, ServiceRegistration, HairdresserService
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
from .forms import FindClientServiceForm, BookTimeServiceForm, FindAdminServiceForm, AddAdminServiceForm
from flask_login import current_user
from flask import request
from ..email import send_email
from flask import current_app

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

    app = current_app._get_current_object()
    send_email(app.config['HIUSMAGIA_ADMIN'], 'Client canceled reservation',
               'auth/email/client_cancel', date=date, time=time, master=request.args.get('master'), username=current_user.username)
                  
    return (jsonify(result_1))

@main.route("/customers/reservation/")
def reservation():
    form = BookTimeServiceForm ()
    choices_s = [("", "---")]
    choices_u = [("", "---")]
    for s in Service.query.all():
        choices_s.append((str(s.id), s.service_name))
    form.service.choices = choices_s
    for u in User.query.filter_by(hairdresser='1').all():
        choices_u.append((str(u.id), u.username))
    form.hairdresser.choices = choices_u

    #form.service.choices=[(service.id, service.service_name)for service in Service.query(Service.id, Service.service_name).all()]
    return render_template("customers/reservation.html", form=form) 

# dynamic select field - hairdresser in form. When you choose service, 
# in the list of hairdressers are only haidressers, who can provide this service.

#@main.route('/customers/reservation/hairdresser/<service>')
#def hairdresser(service):
#    db = SQLAlchemy()
#    sql_hairdressers = text("SELECT users.id, sername FROM hairdresser_service \
#                         LEFT JOIN users ON hairdresser_service.hairdresser_id = users.id \
#                        WHERE service_id='"+ str(service)+"' AND users.hairdresser = '1' " )
#    result_hairdressers = db.engine.execute(sql_hairdressers)       
#    response = []

#    for row in result:
#        response.append({
#            "id": str(row.id),
#            "username": str(row.username),
#         })
#    return (jsonify(response))

# clients can search all aviables services and for serching can choose period, hairdresser or service, like filter    

@main.route("/customers/reservation/servicesAvailable.json") 
def servicesAvailable(): 
    date_from=request.args.get('date_from')
    date_to=request.args.get('date_to')
    service_id=request.args.get('service_id')
    hairdresser_id=request.args.get('hairdresser_id')
    query_part=""
    db = SQLAlchemy()
    if(hairdresser_id!="" and service_id!=""):
        query_part=" AND ((hairdresser_id='"+ str(hairdresser_id) + "') AND (service_id='"+ str(service_id) +"')) "
    elif (service_id!="" ):
           query_part=" AND (service_id='"+ str(service_id) +"') "
    else: 
        if (hairdresser_id!=""):
            query_part=" AND (hairdresser_id='"+ str(hairdresser_id) + "')"
     
    sql = text("SELECT `date`,`time`,service_name,`username`, service_timetable.id, price\
                FROM service_timetable\
                LEFT JOIN services ON service_timetable.service_id=services.id\
                LEFT JOIN users ON service_timetable.hairdresser_id=users.id\
                WHERE (`date`>='" + str(date_from) +"' AND `date`<= '" + str(date_to) +"') AND\
                 `status`='future'" + str(query_part))
    result = db.engine.execute(sql)

    response = []
    for row in result:
        response.append({
            "timetable_id": str(row.id),
            "date": str(row.date),
            "time": str(row.time),
            "service_name":str(row.service_name),
            "username":str(row.username),
            "price":str(row.price)
        })

    return (jsonify(response))
@main.route("/customers/reservation/makeReservation.json") 
def makeReservation(): 
    result_1 = "true" 
    id_in_timetable=request.args.get('id_in_timetable')
    if current_user:
        client_id=current_user.id
    db = SQLAlchemy()
    sql = text("SELECT `date`,`time`,service_id,hairdresser_id FROM service_timetable\
                WHERE id='" +id_in_timetable + "'")
    result = db.engine.execute(sql)
    
    for row in result:
        date=str(row.date)  
        time=str(row.time)
        service_id=str(row.service_id)
        hairdresser_id=str(row.hairdresser_id)   

    sql_delete = text("DELETE FROM service_timetable\
                WHERE id='" +id_in_timetable + "'")
    result_delete = db.engine.execute(sql_delete)  

    sql_insert = text("INSERT INTO service_registration (`date`,`time`,timetable_id,service_id,client_id,hairdresser_id)\
                       VALUES ('" + str(date) +"','"+ str(time) + "','"+ str(id_in_timetable) +"','"\
                        +str(service_id) +"','" + str(client_id)+"','"+ str(hairdresser_id) + "')")
    result_insert = db.engine.execute(sql_insert) 

    #delete_str=ServiceTimetable.query.filter_by(id=id_in_timetable).first()
    #db.session.commit()
    #current_db_sessions = db.session.object_session(delete_str)
    # current_db_sessions.add(delete_str)
    #current_db_sessions.delete(delete_str)
    #db.session.commit()
    # insert_str=ServiceRegistration(date=date, time=time,service_id=service_id,client_id=client_id, timetable_id=id_in_timetable, hairdresser_id=hairdresser_id, )
    # db.session.add(insert_str)
    # db.session.commit()
    return (jsonify(result_1)) 
   
    
# admin page

@main.route("/admins/admin_page/")
def admin_page():
    form = FindAdminServiceForm ()
    return render_template("admins/admin_page.html", form=form)

@main.route("/admins/new_change_workout/")
def new_change_workout():
    form = AddAdminServiceForm ()
    return render_template("admins/new_change_workout.html", form=form)  

@main.route("/test")
def test():
    db = SQLAlchemy()
    me = HairdresserService(hairdresser_id=99, service_id=100)
    db.session.add(me)
    db.session.commit()
    db.session.delete(me)
    db.session.commit()
    return jsonify(True)
