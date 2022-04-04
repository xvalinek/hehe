from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key="xvalinek"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    login = db.Column("login", db.String(20))
    email = db.Column("email", db.String(20))
    password = db.Column("password", db.String(20))

    def __init__(self, login, email, password):
        self.login = login
        self.email = email
        self.password = password


@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        login = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        szukanie = users.query.filter_by(login=login).first()
        if szukanie:
            return render_template("login.html")
        elif login:
            lgn = users(login, email, password)
            db.session.add(lgn)
            db.session.commit()
            return render_template("login.html")
    else:
        return render_template("login.html")

@app.route("/users")
def uzytkownicy():
    lista = users.query.all()
    return render_template("lista.html", lista=lista)

if __name__ == "__main__":
    app.run(debug=True)