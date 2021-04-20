# Entry point for the application.
from . import app    # For application discovery by the 'flask' command.
#from . import views  # For import side-effects of setting up routes.

from datetime import datetime
from flask import Flask, render_template
from . import app

@app.route("/")
def index():
    return render_template("index.html")#у этого файла путь указан правильно

@app.route("/company/") #как прописать путь к папке???
def company():
    return render_template("company.html")

@app.route("/feedback/")#как прописать путь к папке???
def feedback():
    return render_template("feedback.html")