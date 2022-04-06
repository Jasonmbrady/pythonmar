from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)
app.secret_key = "We assume session"

# Routes
@app.route('/')
def index():
    # Go to the DB and grab all users
    return render_template("index.html", users = User.get_all())

@app.route("/user/new")
def new_user():
    return render_template("new_user.html")
    
@app.route("/user/create", methods=['POST'])
def create_user():
    # collect form data
    data = {
        "f_name": request.form['f_name'],
        "l_name": request.form['l_name'],
        "email": request.form['email']
    }
    # send data to db
    User.create(data)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)