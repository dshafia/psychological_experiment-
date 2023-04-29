from flask import Flask, render_template, request, jsonify, redirect, url_for, Blueprint
import json
import datetime
from database import db
from bson import json_util
admin = Blueprint('admin', __name__)


@admin.route("/login", methods=['POST'])
def admin_login():
    try:
        data = json.loads(request.data)
        """ Login an admin with the right admin credentials. Else throw an error """
        isExistingAdmin = db.admins.find_one({"userName" : data["userName"], "password" : data["password"]})
        if isExistingAdmin:
            return jsonify({"status": 200,"message": "Sucessfully logged in Admin " + str(data["userName"])})
        else:
            return jsonify({"status": 404,"message": "The username or password you entered was incorrect!"})
    except Exception as e:
        return jsonify({"status": 500, "message": "Internal server error" + str(e)})



@admin.route("/signup", methods=['POST'])
def admin_signup():
    try:
        data = json.loads(request.data)
        """ Create a new Admin entry in the admins collection. """
        isExistingAdmin = db.admins.find_one({"userName" : data["userName"]})
        if not isExistingAdmin:
            db.admins.insert_one({"userName" : data["userName"], "password" : data["password"]})
            return jsonify({"status": 200,"message": "Sucessfully signed up Admin " + str(data["userName"]), "admin" : data["userName"]})
        else:
            return jsonify({"status": 409,"message": "Admin already exists!"})
    except Exception as e:
        return jsonify({"status": 500, "message": "Internal server error" + str(e)})


@admin.route("/addCategory", methods=['POST'])
def add_category():
    try:
        data = json.loads(request.data)
        """ Add the category entered into the category collection and also each category would have a list of questions. """
        db.categories.update_one({"categoryName" : data["categoryName"]},{"$set" :{"questions" : data["questions"], "createdBy" : data["admin"], "createdAt" : datetime.datetime.now()}}, upsert=True)
        return jsonify({"status": 200,"message": "Sucessfully added Category " + str(data["categoryName"])})
        # else:
        #     return jsonify({"status": 409,"message": "Category already exists!"})
    except Exception as e:
        return jsonify({"status": 500, "message": "Internal server error" + str(e)})

@admin.route("/getCategory", methods=['POST'])
def get_category():
    try:
        data = json.loads(request.data)
        categoryDetails = db.categories.find_one({"categoryName" : data["categoryName"]})
        print("categoryDetails ", type(categoryDetails))
        if categoryDetails:
            del categoryDetails["_id"]
            return jsonify({"status": 200,"result":categoryDetails})
        else:
            return jsonify({"status": 404,"message": "Category doesn't exists!"})
    except Exception as e:
        return jsonify({"status": 500, "message": "Internal server error" + str(e)})

@admin.route("/addQuestions", methods=['POST'])
def add_questions():
    try:
        data = json.loads(request.data)
        """ Add the questions entered into the questions collection and also each question would have a tag and category under which it has to be created """
        isExistingCategory = db.categories.find_one({"categoryName" : data["categoryName"]})
        existingQuestions = isExistingCategory["questions"] + data["questions"]
        if isExistingCategory:
            db.categories.update_one({"categoryName" : data["categoryName"]}, {"$set" : {"questions" : existingQuestions}})
            return jsonify({"status": 200,"message": "Sucessfully added questions under" + str(data["categoryName"])})
        else:
            return jsonify({"status": 404,"message": "Category doesn't exist!"})
    except Exception as e:
        return jsonify({"status": 500, "message": "Internal server error" + str(e)})
