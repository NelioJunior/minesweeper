from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/simu')
def ola():
    return "<h1>Hello world!</h1><br><center><h2>Terrific! Isn't necessary go back to heroku site</h2><h2>Just commit, push and waiting a few seconds</h2><center>"

@app.route("/user/<name>")
# Exemple:   http://127.0.0.1:5000/user/john
# Tip:  https://jinja.palletsprojects.com/en/3.0.x/
def user(name):
    return render_template('user.html', user_name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

def main():
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    main()
