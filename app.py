'''
tests  
    http://127.0.0.1:5000
    https://minesweeper-flash-python.herokuapp.com/

Tip  
    https://jinja.palletsprojects.com/en/3.0.x/

                                                    Nell Jr - Jul/21

'''

import os
import random
from flask import jsonify
from flask import request
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/add")                          
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

@app.route("/placeBombs")                          
def placeBombs():
    rows = []
    bombsNumber = request.args.get('bombs')
    bombsNumber = int(bombsNumber)

    for idx in range(bombsNumber):
        placeSingleBomb(rows)

    rows = "[[null,null,null,null,true,null,null,null,true,null,null,null,null,null,null,null,null,null,null,null,null,true],[null,null,true],[null,null,null,true,true,null,null,null,null,true,true,true,null,null,null,true,true,null,true],[null,null,null,null,null,null,null,true,null,null,null,null,null,null,null,null,null,null,null,true,true,true],[null,null,null,null,true,null,null,null,null,true,null,true,true,null,null,null,null,null,null,null,null,null,true],[null,true,null,true,null,null,null,null,null,null,null,null,null,null,true,null,null,true,null,null,true,true],[true,null,true,null,null,null,null,null,null,null,null,true,null,true,null,null,null,null,null,null,true],[null,true,null,null,null,null,null,null,null,true,null,null,null,null,null,true,null,true,null,null,null,true,true,true],[true,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,true],[null,null,null,true,null,true,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,true],[null,null,null,true,true,null,null,null,true,null,null,null,null,null,true,null,null,true],[true,null,null,true,null,null,null,null,null,null,null,null,true,true,null,null,null,null,null,null,null,true,null,true]]"
    return jsonify(rows)

def placeSingleBomb(bombs):
    rowsNumber = request.args.get('rows')
    rowsNumber = int(rowsNumber)

    colsNumber = request.args.get('cols')
    colsNumber = int(colsNumber)

    nrow = random.randint(0,rowsNumber)
    ncol = random.randint(0,colsNumber)

    '''
    try:
        row = bombs[nrow]
    except:
        bombs.append("[]")

    try:
        col = row[ncol]
        placeSingleBomb(bombs)
    except:
        row[ncol] = True
    '''

    return ""


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
