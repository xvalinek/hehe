from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
app = Flask(__name__)
app.secret_key="xvalinek"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

class szydelko(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    nazwa = db.Column("nazwa", db.String(20))
    cena = db.Column("cena", db.Integer)
    ilosc = db.Column("ilosc", db.Integer)
    wartosc_calkowita = db.Column("wc", db.Integer)

    def __init__(self, nazwa, cena, ilosc, wartosc_calkowita):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc
        self.wartosc_calkowita = wartosc_calkowita

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        nazwa = request.form["nazwa"]
        cena = request.form["cena"]
        ilosc = request.form["ilosc"]
        
        if nazwa:
            cena = int(cena)
            ilosc = int(ilosc)
            w_c = cena*ilosc
            lgn = szydelko(nazwa, cena, ilosc, w_c)
            db.session.add(lgn)
            db.session.commit()
            return render_template("index.html")
            
    else:
        return render_template("index.html")

@app.route("/info")
def info():
    lista = szydelko.query.all()
    suma = db.session.query(db.func.sum(szydelko.wartosc_calkowita)).scalar()
    return render_template("info.html", lista=lista, suma=suma)

    


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)