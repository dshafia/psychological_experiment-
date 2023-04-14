from flask import Flask, render_template, request, jsonify, redirect, url_for, Blueprint, flash
import random
import json
from flask_cors import CORS, cross_origin

student = Blueprint("student", __name__)

results = {}

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
        "store it in CSV"
        return jsonify({"status": 200, "message": "Sucessfully logged in " + str(num)})
    except Exception as e:
        return jsonify({"status": 500, "message": "Internal server error" + str(e)})



@student.route('/demographic_info', methods=['POST'])
@cross_origin(supports_credentials=True)
def demo_page():
    try:
        data = json.loads(request.data)
        "store it in CSV"
        return jsonify({"status": 200,"message": "Sucessfully recieved DemoGraphic info "})
    except Exception as e:
        return jsonify({"status": 500, "message": "Internal server error" + str(e)})

@student.route('/consent', methods=['POST'])
@cross_origin(supports_credentials=True)
def consent_page():
    return jsonify({"status": 200, "message": "Sucessfully logged in "})

@student.route('/login', methods=['POST'])
@cross_origin(supports_credentials=True)
def loginpage():
    try:
        data = json.loads(request.data)
        "store it in CSV"
        return jsonify({"status": 200,"message": "Sucessfully logged in " + data["fname"]})
    except Exception as e:
        return jsonify({"status": 500, "message": "Internal server error" + str(e)})


'''if __name__ == '__main__':
    student.run(degu)

    "https://www.codespeedy.com/how-to-pass-javascript-variables-to-python-in-flask/"
    https://www.youtube.com/watch?v=dam0GPOAvVI&ab_channel=TechWithTim'''