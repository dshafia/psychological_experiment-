from flask import Flask, render_template, request, jsonify, redirect, url_for, Blueprint
from Admin_val import Loginform, Signform
from admin_model import Admin

admin = Blueprint('admin', __name__)


@admin.route("/login", methods=['GET', 'POST'])
def admin_login():
    form = Loginform()
    if request.method == "POST" and form.validate():
        user = form.username.data
        password = form.password.data
        print(user, password)
    return render_template("admin_login.html", form =form)


@admin.route("/signup", methods=['GET', 'POST'])
def admin_signup():
    re_password = ""
    form = Signform()
    if request.method == "POST" and form.validate():
        user = form.username.data
        password = form.password.data
        re_password = form.confirm.data
        if re_password == password:
            print(user, password, True)
            #data = Admin(user, password)
    return render_template("admin_signup.html", form = form)
