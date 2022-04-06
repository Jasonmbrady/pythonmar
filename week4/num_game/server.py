# IMPORTS
from flask import Flask, redirect, render_template, session, request
import random
app = Flask(__name__)
app.secret_key="Insert Song Lyrics Here"

# ROUTES
@app.route("/")
def index():
    if 'number' not in session:
        session['number'] = random.randint(1,100)
    if 'count' not in session:
        session['count'] = 0
    return render_template("index.html")

@app.route("/process_guess", methods=["POST"])
def process_guess():
    session['guess'] = int(request.form['guess'])
    session['count'] += 1
    return redirect("/")

@app.route("/clear")
def clear():
    session.clear()
    return "You are on the Clear route"

# ACTIVATE SERVER
if __name__ == "__main__":
    app.run(debug=True)
