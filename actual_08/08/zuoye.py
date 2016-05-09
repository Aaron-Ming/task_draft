#encoding=utf-8
#
from flask import Flask,render_template,redirect,session


app = Flask(__name__)
app.secret_key = '1234567890!@#$%^&*()'

@app.route('/login', methods=['GET','POST'])
def login():
    return 'Hello World.'

@app.route('/log_page')
def log_page():
    pass

@app.route('/user_page')
def user_page():
    pass

@app.route('/update_user')
def update_user():
    pass

@app.route('/add_user')
def add_user():
    pass

@app.route('/del_user')
def del_user():
    pass

@app.route('/logout')
def logout():
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
