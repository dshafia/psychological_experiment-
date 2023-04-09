from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import pandas as pd

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'SWE_PSYCO_EXP'

    from student import student
    from admin import admin

    app.register_blueprint(student, url_prefix="/")
    app.register_blueprint(admin, url_prefix="/admin/")

    return app

