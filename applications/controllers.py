from flask import current_app as app
from applications.models import *
from .database import db
from flask import render_template, request, redirect, flash



@app.route("/", methods=["GET","POST"])
def home():
    return render_template("landingpage.html")

@app.route("/customer_login",methods=["GET","POST"])
def customer_login():
    if request.method == "GET":
        page = "customer"
        input_boxes = [{"label":"Email", "type": "email", "name" : "c_mail", "required" : "True"},{"label":"Password", "type": "password", "name" : "password", "required" : "True"}]
        submit_button = "Sign In"
        action = "customer_login"
        return render_template("layout_login.html",page=page, input_boxes = input_boxes,action = action, submit_button = submit_button)
    if request.method == "POST":
        c_mail = request.form["c_mail"]
        password = request.form['password']
        customer_data = Customer.query.filter_by(c_mail = c_mail).first()
        print(customer_data)
        if customer_data:
            if customer_data.c_password == password:
                return render_template("user.html")
            else:
                flash("wrong password")
                return redirect("customer_login")
        else:
            flash("email not registered please register")
            return redirect("customer_register")
        return "hello"


@app.route("/customer_register", methods=["GET","POST"])
def customer_register():   
    if request.method == "GET":
        page = "customer"
        input_boxes = [{"label":"Name", "type": "text", "name" : "c_name", "required" : "True"},{"label":"Email", "type": "email", "name" : "email", "required" : "True"},{"label":"Password", "type": "password", "name" : "password", "required" : "True"}]
        submit_button = "Sign Up"
        action = "customer_register"
        return render_template("layout_login.html",page = page ,input_boxes = input_boxes,action = action, submit_button = submit_button)
    if request.method == "POST":
        c_name = request.form["c_name"]
        email = request.form["email"]
        password = request.form["password"]
        new_Customer= Customer(c_name = c_name,c_mail=email,c_password = password,address="NA",daily_collection=False,daily_collection_reward_points=0)
        db.session.add(new_Customer)
        db.session.commit()
        flash("you are now register please login")
        return redirect("customer_login")

@app.route("/vendor_login",methods=["GET","POST"])
def vendor_login():
    if request.method == "GET":
        page = "vendor"
        input_boxes = [{"label":"Bussiness Email", "type": "email", "name" : "vmail", "required" : "True"},{"label":"Password", "type": "password", "name" : "password", "required" : "True"}]
        submit_button = "Sign In"
        action = "vendor_login"
        return render_template("layout_login.html",action=action ,page = page,input_boxes = input_boxes, submit_button = submit_button)

@app.route("/vendor_register", methods=["GET","POST"])
def vendor_register():
    if request.method == "GET":
        page = "vendor"
        action = "vendor_register"
        input_boxes = [{"label":"Bussiness Name", "type": "text", "name" : "v_name", "required" : "True"},{"label":"Bussiness Email", "type": "email", "name" : "vmail", "required" : "True"},{"label":"Password", "type": "password", "name" : "password", "required" : "True"}]
        submit_button = "Sign Up"
        return render_template("layout_login.html",action = action,page = page,input_boxes=input_boxes, submit_button = submit_button)


@app.route("/place_order",methods=["GET","POST"])
def place_order():
    return render_template("placeorder.html")

@app.route("/user",methods=["GET","POST"])
def user():
    return render_template("user.html")

@app.route("/user_profile", methods=["GET","POST"])
def user_profile():
    return render_template("profile.html")

@app.route("/daily_collection", methods=["GET","POST"])
def daily_collection():
    return render_template("dailycollection.html")