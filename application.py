import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
        headline = "Index"
        return render_template("index.html", headline=headline)

@app.route("/newyears")
def newyears():
        now = datetime.datetime.now()
        new_year = now.month == 1 and now.day == 1
        return render_template("newyears.html", new_year=new_year)

@app.route("/bye")
def bye():
        headline = "Goodbye"
        return render_template("index.html", headline=headline)

@app.route("/names")
def names():
        names = ["Rina", "Mewmew", "Brian"]
        return render_template("names.html", names=names)

