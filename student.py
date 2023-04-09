from flask import Flask, render_template, request, jsonify, redirect, url_for, Blueprint, flash
import random
import json
import pandas as pd

student = Blueprint("student", __name__)

#student = Flask(__name__)

def excel_login_inf(data):
    pass
    #print(student_info)
    #login_list = pd.read_json(student_info)
    #print(type(login_list))
    #print(login_list)

@student.route('/process_student_info', methods=['GET', 'POST'])
def process_student_info():
    data = "hello world"
    if (request.method == 'POST'):
        excel_login_inf(request.json)
        return redirect(url_for('student.consent_page'))
    else:
        return redirect(url_for('http://127.0.0.1:5000/consentpage'))


'''@student.route('/process_student_demographic_info', methods=['GET', 'POST'])
def process_student_demographic_info():
    data = "hello world"
    if (request.method == 'POST'):
        excel_login_inf(request.json)
        return {'data': data}
        #return redirect(url_for('consent_page'), code=307)'''


@student.route('/exp2')
def exp2():
    return render_template("exp2.html")

@student.route('/exp1')
def exp1():
    if request.method == "POST":
        print("In EXP1")
    return render_template("exp1.html")

@student.route('/game_placeholder')
def game1_placeholder():
    if request.method == "POST":
        print("In EXP2")
    return render_template("CG.html")

@student.route('/game_link')
def game_link():
    return redirect("https://playpager.com/embed/checkers/index.html")

@student.route('/personality', methods=['GET','POST'] )
def personality():
    results = ""
    num = 0
    if request.method == "POST":
        data = request.form.getlist("perqs1")
        results = results + data[0] + "$"
        data = request.form.getlist("perqs2")
        results = results + data[0] + "$"
        num = random.randint(1, 3)
        print(num)
        if (num == 1):
            return redirect(url_for('student.game1_placeholder'))
        elif(num == 2):
            return redirect(url_for('student.exp1'))
        else:
            return redirect(url_for('student.exp2'))
    return render_template("personality.html")

@student.route('/demographic_info', methods=['GET','POST'])
def demo_page():
    if request.method == "POST":
        data = request.form
        print(data)
        return redirect(url_for('student.personality'))
    return render_template("demographic.html")

@student.route('/consentpage', methods=['GET','POST'])
def consent_page():
    return render_template("consentpage.html")

@student.route('/', methods=['GET', 'POST'])
def loginpage():
    details = {}
    if request.method == "POST":
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        cls = request.form.get("class")
        if fname == "" and lname == "" and cls == "":
            flash('Please enter valid details', category='error')
        else:
            details["fname"] = fname
            details["lname"] = lname
            details["cls"] = cls
            print(details)
            excel_login_inf(details)
            return redirect(url_for('student.consent_page'))
    return render_template("Login.html")


'''if __name__ == '__main__':
    student.run(degu)

    "https://www.codespeedy.com/how-to-pass-javascript-variables-to-python-in-flask/"
    https://www.youtube.com/watch?v=dam0GPOAvVI&ab_channel=TechWithTim'''