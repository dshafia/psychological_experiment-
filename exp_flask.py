from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import pandas as pd

app = Flask(__name__)

def excel_login_inf(student_info):
    print(student_info)
    #login_list = pd.read_json(student_info)
    #print(type(login_list))
    #print(login_list)

@app.route('/process_student_info', methods=['GET', 'POST'])
def process_student_info():
    data = "hello world"
    if (request.method == 'POST'):
        excel_login_inf(request.json)
    return redirect(url_for('consent_page'), code=307)


@app.route('/process_student_demographic_info', methods=['GET', 'POST'])
def process_student_demographic_info():
    data = "hello world"
    if (request.method == 'POST'):
        excel_login_inf(request.json)
        return {'data': data}
        #return redirect(url_for('consent_page'), code=307)


@app.route('/consentpage', methods = ['GET', 'POST'])
def consent_page():
    return render_template("consentpage.html")

@app.route('/demographic_info')
def demograph():
    return render_template("demographic.html")

@app.route('/')
def loginpage():
    return render_template("Login.html")


if __name__ == "__main__":
    app.run(debug=True)


    "https://www.codespeedy.com/how-to-pass-javascript-variables-to-python-in-flask/"