from flask import Flask, render_template, request, jsonify, redirect, url_for, Blueprint, flash
import random
import json
from flask_cors import CORS, cross_origin
from database import db

student = Blueprint("student", __name__)

results = {}

def excel_login_inf(data):
    pass

@student.route('/process_student_info', methods=['GET', 'POST'])
def process_student_info():
    data = "hello world"
    if (request.method == 'POST'):
        excel_login_inf(request.json)
        return redirect(url_for('student.consent_page'))
    else:
        return redirect(url_for('http://127.0.0.1:5000/consentpage'))


@student.route('/exp2')
def exp2():
    result = []
    if request.method == "Post":
        print("In EXP2")
        data = request.form.getlist("exp2qs1")
        result.append(data[0])
        data = request.form.getlist("exp2qs2")
        result.append(data[0])
        print(result)

    return render_template("exp2.html")

@student.route('/exp1')
def exp1():
    result = []
    if request.method == "POST":
        print("In EXP1")
        data = request.form.getlist("exp1qs1")
        result.append(data[0])
        data = request.form.getlist("exp1qs2")
        result.append(data[0])
        print(result)
    return render_template("exp1.html")

@student.route('/CG')
def game1_placeholder():
    if request.method == "POST":
        print("In CG")
    return render_template("CG.html")

@student.route('/game_link')
def game_link():
    return redirect("https://playpager.com/embed/checkers/index.html")

@student.route('/personality', methods=['POST'] )
def personality():
    try:
        num = random.randint(1, 3)
        data = json.loads(request.data)
        print(data)
        """ Check if the user exists already in the DB.
            If yes, add the demographic information to the user record.
            Else, return user doesn't exist error. """
        isExistingUser = db.users.find_one({"fname" : data["user"]})
        if isExistingUser:
            db.users.update_one({"fname" : data["user"]}, {"$set" : {"gender" : data["gender"], "age" : data["age"], "demo_cls":data["demo_cls"], "address" : data["address"]}})
            return jsonify({"status": 200,"message": "Sucessfully recieved DemoGraphic info for user " + str(data["user"])})
        else:
            return jsonify({"status": 404,"message": "User not found"})
    except Exception as e:
        return jsonify({"status": 500, "message": "Internal server error" + str(e)})

@student.route('/demographic_info', methods=['POST'])
@cross_origin(supports_credentials=True)
def demo_page():
    try:
        data = json.loads(request.data)
        """ Check if the user exists already in the DB.
            If yes, add the demographic information to the user record.
            Else, return user doesn't exist error. """
        isExistingUser = db.users.find_one({"fname" : data["user"]})
        if isExistingUser:
            db.users.update_one({"fname" : data["user"]}, {"$set" : {"gender" : data["gender"], "age" : data["age"], "demo_cls":data["demo_cls"], "address" : data["address"]}})
            return jsonify({"status": 200,"message": "Sucessfully recieved DemoGraphic info for user " + str(data["user"])})
        else:
            return jsonify({"status": 404,"message": "User not found"})
    except Exception as e:
        return jsonify({"status": 500, "message": "Internal server error" + str(e)})

@student.route('/consent', methods=['POST'])
@cross_origin(supports_credentials=True)
def consent_page():
    # Store the consent for this user
    return jsonify({"status": 200, "message": "Sucessfully logged in "})

@student.route('/login', methods=['POST'])
@cross_origin(supports_credentials=True)
def loginpage():
    try:
        data = json.loads(request.data)
        """ Check if the user exists already in the DB.
            If no, create a new user.
            Else, do nothing. """
        isExistingUser = db.users.find_one({"fname" : data["fname"]})
        if not isExistingUser:
            db.users.insert_one({"fname" : data["fname"], "lname" : data["lname"], "cls" : data["cls"]})
        return jsonify({"status": 200,"message": "Sucessfully logged in " + data["fname"], "loggedin_user" :  data["fname"]})
    except Exception as e:
        return jsonify({"status": 500, "message": "Internal server error" + str(e)})