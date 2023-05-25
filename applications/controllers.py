from flask import current_app as app
from applications.models import *

from flask import render_template, request

@app.route("/", methods=["GET","POST"])
def home():
    return render_template("landingpage.html")

@app.route("/customer_login",methods=["GET","POST"])
def customer_login():
    if request.method == "GET":
        page = "customer"
        input_boxes = [{"label":"Name", "type": "text", "name" : "c_name", "required" : "True"},{"label":"Email", "type": "email", "name" : "c_mail", "required" : "True"},{"label":"Password", "type": "password", "name" : "password", "required" : "True"}]
        submit_button = "Sign In"
        return render_template("layout_login.html",page=page, input_boxes = input_boxes, submit_button = submit_button)
    if request.method == "POST":
        request.form


@app.route("/customer_register", methods=["GET","POST"])
def customer_register():   
    if request.method == "GET":
        page = "customer"
        input_boxes = [{"label":"Name", "type": "text", "name" : "c_name", "required" : "True"},{"label":"Email", "type": "email", "name" : "email", "required" : "True"},{"label":"Password", "type": "password", "name" : "password", "required" : "True"}]
        submit_button = "Sign Up"
        return render_template("layout_login.html",page = page ,input_boxes = input_boxes, submit_button = submit_button)

@app.route("/vendor_login",methods=["GET","POST"])
def vendor_login():
    if request.method == "GET":
        page = "vendor"
        input_boxes = [{"label":"Bussiness Email", "type": "email", "name" : "vmail", "required" : "True"},{"label":"Password", "type": "password", "name" : "password", "required" : "True"}]
        submit_button = "Sign In"
        return render_template("layout_login.html", page = page,input_boxes = input_boxes, submit_button = submit_button)

@app.route("/vendor_register", methods=["GET","POST"])
def vendor_register():
    if request.method == "GET":
        page = "vendor"
        input_boxes = [{"label":"Bussiness Name", "type": "text", "name" : "v_name", "required" : "True"},{"label":"Bussiness Email", "type": "email", "name" : "vmail", "required" : "True"},{"label":"Password", "type": "password", "name" : "password", "required" : "True"}]
        submit_button = "Sign Up"
        return render_template("layout_login.html",page = page,input_boxes=input_boxes, submit_button = submit_button)


@app.route("/place_order",methods=["GET","POST"])
def place_order():
    return render_template("placeOrder.html")
