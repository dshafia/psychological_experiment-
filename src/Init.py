from flask import Flask, render_template, request, jsonify, redirect, url_for
from admin import admin
from student import student
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app, support_credentials=True)

app.register_blueprint(student, url_prefix="/")
app.register_blueprint(admin, url_prefix="/admin/")

if __name__ == "__main__":
    app.run(debug=True)
