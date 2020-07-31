   #         <input type="submit" value="Submit"/>
# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import *
from datetime import datetime

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time=datetime.now())

@app.route('/results', methods= ['GET', 'POST'])
def results():
    meat = request.form["meat"]
    meal = user_meat(meat)
    return render_template("results.html", meal=meal, meat=meat, time=datetime.now())


@app.route('/course', methods= ['GET', 'POST'])
def course():
    course = request.form["course"]
    food = user_course(course)
    return render_template("course.html", course=course, food=food,time=datetime.now())

@app.route('/health', methods= ['GET', 'POST'])
def health():
    health = request.form["health"]
    sweet = user_health(health)
    return render_template("health.html", health=health, sweet=sweet,time=datetime.now())


@app.route('/recipe', methods= ['GET', 'POST'])
def recipe():
    recipe = request.form["recipe"]
    final = user_meat(recipe)
    return render_template("recipe.html", recipe=recipe, final=final, time=datetime.now())
