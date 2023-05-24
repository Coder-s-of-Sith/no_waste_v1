from flask import current_app as app
from applications.models import *

@app.route("/home", methods=["GET","POST"])
def home():
    return "hello"