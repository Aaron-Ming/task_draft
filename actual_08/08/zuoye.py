#encoding=utf-8
#
from flask import Flask,render_template,redirect,session,url_for,request
import dbutil

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
        if user not in dbutil.auth_info():
            return 'user not exists.'
        elif dbutil.auth_info()[user] == pwd:
            session['user'] = user
            return redirect('/user_page')
        else:
            return 'password error.'

@app.route('/log_page')
def log_page():
    page = request.args.get('page',0)
    cont = request.args.get('cont',10)
    page = int(page)
    cont = int(cont)
    if 100%cont:
        all_pages = (100/cont)
    else:
        all_pages = 100/cont-1
    logs = dbutil.log_info(page*cont,cont)
    return render_template('log_page.html', logs=logs,page=page,all_pages=all_pages)

@app.route('/user_page')
def user_page():

    user_info = dbutil.user_info()
    return render_template('user_page.html', user_info=user_info)

@app.route('/update_user')
def update_user():
    uppwd = request.args.get('uppwd')
    id = request.args.get('id')
    dbutil.update_user(uppwd,id)
    return redirect('/user_page')

@app.route('/add_user', methods=['POST'])
def add_user():
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    dbutil.ins_user(user=user,pwd=pwd)
    return redirect('/user_page')

@app.route('/del_user')
def del_user():
    id = request.args.get('id')
    dbutil.del_user(id)
    return redirect('/user_page')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
