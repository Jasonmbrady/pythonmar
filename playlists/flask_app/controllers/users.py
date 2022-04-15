from flask_app import app
from flask import get_flashed_messages, render_template, redirect, request, session, flash
from flask_app.models.user import User
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)

# ROUTES
@app.route("/")
def index():
    return render_template("index.html", message = get_flashed_messages())

@app.route("/register", methods=["POST"])
def register():
    #validate submission
    if not User.validate_user(request.form):
        return redirect("/")
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        # "password": bcrypt.generate_password_hash(request.form['password']
        "password": request.form['password']
    }
    session['user_id'] = User.create(data)
    return redirect("/dashboard")

@app.route("/login", methods=["POST"])
def login():
    this_user = User.get_one_email({'email': request.form['email']})
    if this_user:
        # if bcrypt.check_password_hash(this_user.password, request.form['password']):
        if this_user.password == request.form['password']:
            session['user_id'] = this_user.id
            return redirect("/dashboard")
    flash("Invalid Email/Password combination")
    return redirect("/")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", user = User.get_one_with_playlists({"id": session['user_id']}))