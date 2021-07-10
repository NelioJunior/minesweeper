from flask import request
@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    print(username)
    password= request.args.get('password')
    print(password)