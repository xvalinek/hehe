from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__,template_folder='templates')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"



database = SQLAlchemy(app)

class Task(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String)
    surname = database.Column(database.String)
    password = database.Column(database.String)
    


@app.route("/", methods=["GET", "POST"])
def todolist():
    
    if request.method == "POST":
        task1 = Task(name=request.form.get("namme", False))
        task2 = Task(name=request.form.get("surname", False))
        task3 = Task(name=request.form.get("password", False))
        database.session.add(task1)
        database.session.add(task2)
        database.session.add(task3)
        database.session.commit()


    tasks = Task.query.all()
    return render_template("login.html", tasks=tasks)

if __name__=="__main__":
    app.run(debug=True)