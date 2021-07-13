'''
tests  
    http://127.0.0.1:5000
    https://minesweeper-flash-python.herokuapp.com/

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

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.route("/placeBombs")                          
def placeBombs():
    bombs = request.args.get('bombs')
    bombs = int(bombs)

    rowsNumber = request.args.get('rows')
    rowsNumber = int(rowsNumber) 

    colsNumber = request.args.get('cols')
    colsNumber = int(colsNumber)  

    rows = []
    for x in range(rowsNumber):
        cols = []  
        for y in range(colsNumber):    
            cols.append(None) 
        rows.append(cols)

    for idx in range(bombs):
        while True:
            nrow = random.randint(0,rowsNumber -1)
            ncol = random.randint(0,colsNumber -1)
            if rows[nrow][ncol] != True:  
                rows[nrow][ncol] = True
                break 
    
    return jsonify(rows)

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
