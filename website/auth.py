from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/resume')
def resume():
    return render_template("resume.html")

@auth.route('/projects')
def projects():
    return render_template("projects.html")

