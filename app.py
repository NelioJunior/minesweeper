from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/play')
def ola():
    return render_template('index.html')

@app.route('/simu')
def ola():
    return "<h1>Hello beatiful world!</h1>"

@app.route("/user/<name>")
# Exemple:   http://127.0.0.1:5000/user/john
# Tip:  https://jinja.palletsprojects.com/en/3.0.x/
def user(name):
    return render_template('user.html', user_name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

app.run()
