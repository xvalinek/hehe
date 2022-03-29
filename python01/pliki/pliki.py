from flask import Flask, render_template
from drugi import drugi

app = Flask(__name__)

@app.register_blueprint(drugi, url_prefix="/drugi")


@app.route("/nnn")
def nnn():
    return "<h1>test w h1</h1>"
    
if __name__ == "__main__":
    app.run(debug=True)