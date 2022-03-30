from flask import Flask, render_template

app = Flask(__name__)

# ROUTES
@app.route("/")
def index():
    return render_template("index.html", this_num = 5)

@app.route("/repeat/<int:num>/<string:word>")
def success(num, word):
    return f"{word} " * num

@app.route("/lists")
def lists():
    num_list = [2, 234, 34, 444, 3621993]
    pizza_info = [
        {"name": "Baconator McBaconly", "Toppings": "Bacon, Canadian Bacon"},
        {"name": "Veggies Galore", "Toppings": "Green Pepper, Mushroom, Onion, Black Olive"},
        {"name": "Gluten Free", "Toppings": "Pepperoni, Mushroom, Broccoli"}
    ]
    return render_template("lists.html", nums = num_list, pizzas = pizza_info)

# SERVER CODE

if __name__ == "__main__":
    app.run(debug=True)