from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user import User

# Routes go here
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    data = {
        "name": request.form['name'],
        "email": request.form['email']
    }
    session['user_id'] = User.create(data)
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    data = {
        "id": session['user_id']
    }
    return render_template("dashboard.html", user = User.get_one_with_cards(data))
