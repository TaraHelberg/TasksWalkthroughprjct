"""
Flask import to render templates & taskmanager import app
"""
from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    """
    Render template base.html
    """
    return render_template("base.html")
