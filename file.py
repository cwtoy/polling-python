import webbrowser
import ballot_count
from threading import Timer
from flask import Flask, render_template, request,jsonify
import os


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

@app.route("/poll", methods = ["POST"] )
def poll():


    checked = request.form["candidates"]
    votes = ballot_count.countVote(checked)
    ballot_count.storage(votes)


    return ballot_count.results()


if __name__ == '__main__':

    Timer(1, open_browser).start()
    app.run(port=5000)





