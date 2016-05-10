#encoding=utf-8
#
from flask import Flask,render_template,redirect,session,url_for,request


app = Flask(__name__)
app.secret_key = '1234567890!@#$%^&*()'

@app.route('/')
def index():
    return render_template('layout_page.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user not in get_user.auth_info():
            return 'user not exists.'
        elif get_user.auth_info()[user] == pwd:
            session['user'] = user           
            return redirect('/home')
        else:
            return 'password error.'

@app.route('/log_page')
def log_page():
    page_title = 'Log-Page'
    return render_template('log_page.html', page_title=page_title)

@app.route('/user_page')
def user_page():
    page_title = 'User management'
    return render_template('user_page.html', page_title=page_title)

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
