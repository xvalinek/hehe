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
    kasaplus = db.Column("kasaplus", db.Integer)
    kasaminus = db.Column("kasaminus", db.Integer)

    def __init__(self, nazwa, cena, ilosc, wartosc_calkowita, kasaplus, kasaminus):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc
        self.wartosc_calkowita = wartosc_calkowita
        self.kasaplus = kasaplus
        self.kasaminus = kasaminus

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        nazwa = request.form["nazwa"]
        cena = request.form["cena"]
        ilosc = request.form["ilosc"]
        kasaplus = request.form["kasaplus"]
        kasaminus = request.form["kasaminus"]
        
        if nazwa:
            cena = int(cena)
            ilosc = int(ilosc)
            kasaplus = int(kasaplus)
            kasaminus = int(kasaminus)
            w_c = cena*ilosc
            lgn = szydelko(nazwa, cena, ilosc, w_c, kasaplus, kasaminus)
            db.session.add(lgn)
            db.session.commit()
            return render_template("index.html")
            
    else:
        return render_template("index.html")

@app.route("/info")
def info():
    lista = szydelko.query.all()
    suma = db.session.query(db.func.sum(szydelko.wartosc_calkowita)).scalar()
    kasaminus = db.session.query(db.func.sum(szydelko.kasaminus)).scalar()
    kasaplus = db.session.query(db.func.sum(szydelko.kasaplus)).scalar()
    sumakoniec = suma-kasaminus+kasaplus
    return render_template("info.html", lista=lista, sumakoniec=sumakoniec)



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)