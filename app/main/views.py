from flask import render_template
from . import main
from flask import jsonify
from ..models import User#, Service,
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
from .forms import FindClientServiceForm
from .forms import BookTimeServiceForm
from flask_login import current_user
from flask import request

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
    print('user_id')
    db = SQLAlchemy()
    sql = text("SELECT `date`,`time`,service_name,`username` FROM service_registration \
                LEFT JOIN services ON service_registration.service_id=services.id \
                LEFT JOIN users ON service_registration.hairdresser_id=users.id \
                WHERE client_id=" + str(user_id) + " AND `date`>='" + date_from + "' AND `date`<= '" + date_to +  "'")
    result = db.engine.execute(sql)

    response = []
    for row in result:
        # record = Empty()
        # record.date = row.date
        # record.time = row.time
        response.append({
            "date": str(row.date),
            "time": str(row.time),
            "service_name":str(row.service_name),
            "username":str(row.username)
        })
    return (jsonify(response))
    # return jsonify([(dict(row.items())) for row in result])


@main.route("/customers/reservation/aviableServises.json") 
def trainersJson():
    db = SQLAlchemy()
    sql = text('select id, username from users')
    result = db.engine.execute(sql)
    return jsonify([(dict(row.items())) for row in result])
    
    # or
    user = User.query.get(3)
    return jsonify(
        user.id,
        user.username
        # User.query.all()
    )

@main.route("/customers/reservation/")
def reservation():
    form = BookTimeServiceForm ()
    return render_template("customers/reservation.html", form=form) 