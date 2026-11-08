from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)
app.secret_key = "portfolio_secret_key"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    print("Name:", name)
    print("Email:", email)
    print("Message:", message)

    return """
    <h2>Thank you for contacting me!</h2>
    <a href="/">Go Back</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
