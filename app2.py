from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)
numbers_list = []

@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/data", methods=["POST"])
def data():
    user_input = request.form.get("number")

    try:
        number = float(user_input)
        numbers_list.append(number)
        return redirect("/home?message=success")
    except (ValueError, TypeError):
        return redirect("/home?message=error")

@app.route("/output", methods=["GET"])
def output():
    return jsonify(numbers_list)

if __name__ == "__main__":
    app.run(debug=True)
