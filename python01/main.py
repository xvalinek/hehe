from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "chuj"


@app.route("/")
def home():
    return "<h1>test w h1</h1>"

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["login"]
        session["user"] = user
        return redirect(url_for("podstrona"))
    else:
        if "user" in session: 
            return redirect(url_for("podstrona"))
        return render_template("login.html")

@app.route("/idk")
def idk():
    return render_template("dupa.html")

@app.route("/user")
def podstrona():
    if "user" in session:
        user = session["user"]
        return f"sesja: {user}"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)