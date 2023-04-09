from flask import Flask, render_template, request, jsonify, redirect, url_for, Blueprint
import json
import pandas as pd

admin = Blueprint('admin', __name__)

@admin.route("/")
def login():
    pass