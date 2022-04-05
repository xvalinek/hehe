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
    age = db.Column("age", db.Integer)

    def __init__(self, login, email, password, age):
        self.login = login
        self.email = email
        self.password = password
        self.age = age


@app.route("/login")
def loginPage():
    return render_template("login.html")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        login = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        age = request.form["age"]
        szukanie = users.query.filter_by(login=login).first()
        if szukanie:
            return render_template("register.html")
        elif login:
            lgn = users(login, email, password, age)
            db.session.add(lgn)
            db.session.commit()
            return render_template("register.html")
    else:
        return render_template("register.html")

@app.route("/users")
def uzytkownicy():
    lista = users.query.all()
    return render_template("lista.html", lista=lista)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)