from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            principal = float(request.form["principal"])
            rate = float(request.form["rate"])
            time = float(request.form["time"])
            frequency = int(request.form["frequency"])

            # Compound Interest Formula
            amount = principal * (1 + rate / frequency)**(frequency * time)
            interest = amount - principal

            result = {
                "amount": round(amount, 2),
                "interest": round(interest, 2)
            }
        except ValueError:
            result = {"error": "Invalid input. Please enter numeric values."}
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
