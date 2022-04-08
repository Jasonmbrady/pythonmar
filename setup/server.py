from flask import Flask, render_template
from user import User

app = Flask(__name__)
app.secret_key="It's a secret to everyone"

@app.route("/")
def index():
    return render_template("index.html", users = User.get_all())

if __name__ == "__main__":
    app.run(debug=True)