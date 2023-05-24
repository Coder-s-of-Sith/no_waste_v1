from flask import current_app as app
from applications.models import *

from flask import render_template

@app.route("/", methods=["GET","POST"])
def home():
    return render_template("landingpage.html")