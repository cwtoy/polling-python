import webbrowser
from threading import Timer
from flask import Flask, render_template, request
import os


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

@app.route("/poll", methods = ["POST"] )
def poll():
    checked = request.form["candidates"] #after the button is pressed, this will pull up that candiate and save the value
                                         #that is a number assigned to each one and save it to checked.

    return render_template('thankyou.html')

if __name__ == '__main__':

    Timer(1, open_browser).start()
    app.run(port=5000)





