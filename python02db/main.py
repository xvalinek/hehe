from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__,template_folder='templates')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"


database = SQLAlchemy(app)

class Task(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String, nullable=False)


@app.route("/", methods=["GET", "POST"])
def todolist():
    
    if request.method == "POST":
        task = Task(name=request.form["task"])
        database.session.add(task)
        database.session.commit()

    tasks = Task.query.all()
    return render_template("todolist.html", tasks=tasks)

if __name__=="__main__":
    app.run(debug=True)


