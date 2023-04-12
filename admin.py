from flask import Flask, render_template, request, jsonify, redirect, url_for, Blueprint
import json
import pandas as pd
from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email
from  email_validator import validate_email

from flask_wtf import FlaskForm

admin = Blueprint('admin', __name__)


class Signform(FlaskForm):
    username = StringField('User name:', validators=[DataRequired(message='Please enter your email address'), Email(message='Invalid email address')])
    password = PasswordField('Password:', validators=[DataRequired(message='Please enter your password')])
    confirm = PasswordField('Re-enter password:', validators=[DataRequired(message='Please enter your password'), EqualTo('password', message='Please match your password')])
    signup = SubmitField('Signup')

class Loginform(FlaskForm):
    username = StringField('User name:', validators=[DataRequired(message='Please enter your email address'), Email(message='Invalid email address')])
    password = PasswordField('Password:', validators=[DataRequired(message='Please enter your password')])
    login = SubmitField('Login')

@admin.route("/login", methods= ['GET','POST'])
def admin_login():
    form = Loginform()
    if request.method == "POST" and form.validate():
        user = form.username.data
        password = form.password.data
        print(user, password)
    return render_template("admin_login.html", form=form)


@admin.route("/signup", methods= ['GET','POST'])
def admin_signup():
    form = Signform()
    if request.method == "POST" and form.validate():
        user = form.username.data
        password = form.password.data
        re_password = form.confirm.data
        if (re_password == password):
            print(user, password, True)
    return render_template("admin_signup.html", form=form)