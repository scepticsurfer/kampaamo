from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('index.html')

@main.route("/company/company/") 
def company():
    return render_template("company/company.html")

@main.route("/trainers/trainers/") 
def trainers():
    return render_template("trainers/trainers.html")

@main.route("/contacts/feedback/")#как прописать путь к папке???
def feedback():
    return render_template("contacts/feedback.html")