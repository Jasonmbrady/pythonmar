from flask_app import app
from flask import get_flashed_messages, render_template, redirect, request, session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    # take in form data
    if not User.validate_user(request.form):
        return redirect("/")
    # validate form data
    # redirect, or write to DB then redirect
    data = {
        "f_name": request.form['f_name'],
        "l_name": request.form['l_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    session['user_id'] = User.create(data)
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    print(session['user_id'])
    return render_template("dashboard.html", user = User.get_one({"id": session['user_id']}))