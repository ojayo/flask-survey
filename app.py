from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config["SECRET_KEY"] = "anything"

responses = []

@app.route("/")
def index():
    """ return homepage """ 

    return render_template("base.html", title=satisfaction_survey.title, instructions=satisfaction_survey.instructions)

@app.route("/question")
def question():
    """ return a question page """


    return redirect("/questions/0")