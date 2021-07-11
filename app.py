'''
tests  
    http://127.0.0.1:5000
    https://minesweeper-flash-python.herokuapp.com/

Tip  
    https://jinja.palletsprojects.com/en/3.0.x/

                                                    Nell Jr - Jul/21

'''

import os 
from flask import jsonify
from flask import request
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/add")                          # http://127.0.0.1:5000/add?a=10&b=20
def add():
    a = request.args.get('a')
    b = request.args.get('b')
    value = int(a) + int(b) 
    return jsonify({"result": value})

@app.route('/simu')
def ola():
    return "<h1>Service working</h1><br><center><h2>For heroku update just waiting a few seconds</h2><center>"

@app.route("/user/<name>")
def user(name):
    return render_template('user.html', user_name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
