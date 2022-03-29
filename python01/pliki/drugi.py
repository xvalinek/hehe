from flask import Blueprint, render_template

drugi = Blueprint("drugi", __name__, static_folder="static", template_folder="templates")

@drugi.route("/dom")
@drugi.route("/huj")
def home():
    return render_template("base.html")