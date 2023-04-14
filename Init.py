from flask import Flask, render_template, request, jsonify, redirect, url_for
from Extension import db
from admin import admin
from student import student

from flask_cors import CORS, cross_origin

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SWE_PSYCO_EXP'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Admin.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app, support_credentials=True)

with app.app_context():
    db.init_app(app)

app.register_blueprint(student, url_prefix="/")
app.register_blueprint(admin, url_prefix="/admin/")

"https://www.youtube.com/watch?v=WhwU1-DLeVw&ab_channel=PrettyPrinted"

if __name__ == "__main__":
    app.run(debug=True)
