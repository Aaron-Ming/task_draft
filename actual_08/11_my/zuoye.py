#encoding=utf-8
#
from flask import Flask,render_template,redirect,url_for,session,request
import dbutil
import json
import config

db = dbutil.DB(db=config.db,host=config.db_host,user=config.db_user,passwd=config.db_passwd)
app = Flask(__name__)
app.secret_key = '1234567890!@#$%^&*()'

@app.route('/testdata')
def testdata():
    return 'hello ajax'

@app.route('/uinfo')
def uinfo():
    sql = 'select id,username,password from user'
    res = json.dumps(db.execute(sql))
    return res

@app.route('/resinfo')
def resinfo():
    sql = 'select * from res_mgt'
    res = json.dumps(db.execute(sql))
    return res


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    info_dict = {}
    sql = 'select username,password from user'
    res_list = db.execute(sql)
    for tup in res_list:
        info_dict[tup[0]] = tup[1]

    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user not in info_dict:
            return 'user not exists.'
        elif info_dict[user] == pwd:
            session['user'] = user
            return redirect(url_for('user_page'))
        else:
            return 'password error.'

@app.route('/log_page')
def log_page():
    page = request.args.get('page',1)
    cont = request.args.get('cont',10)
    page = int(page)
    cont = int(cont)
    if 100%cont:
        all_pages = (100/cont) + 1
    else:
        all_pages = 100/cont
    page_list = range(all_pages)
    sql = 'select * from log_data limit %s,%s' % ((page-1)*cont,cont)
    logs = db.execute(sql)
    # logs = dbutil.log_info((page-1)*cont,cont)
    return render_template('log_page.html', logs=logs,page=page,all_pages=all_pages,page_list=page_list)

@app.route('/user_page')
def user_page():
    return render_template('user_page.html')

@app.route('/update_user', methods=['POST'])
def update_user():
    uppwd = request.form.get('uppwd')
    id = request.form.get('id')
    sql = 'update user set password="%s" where id=%s' % (uppwd,id)

    try:
        db.execute(sql)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/add_user', methods=['POST'])
def add_user():
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    print user, pwd
    sql = 'insert into user (username,password) values ("%s","%s")' % (user,pwd)
    if user:
        try:
            db.execute(sql)
        except:
            return 'error'
        else:
            return 'ok'
    else:
        return 'error'


@app.route('/del_user', methods=['POST'])
def del_user():

    id = request.form.get('id',None)
    sql = 'delete from user where id=%s' % (id)
    try:
        db.execute(sql)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/res_mgt')
def res_mgt():
    return render_template('res_mgt.html')

@app.route('/add_res', methods=['POST'])
def add_res():
    host_name = request.form.get('host_name',None)
    cpu_core = request.form.get('cpu_core',None)
    mem_size = request.form.get('mem_size',None)
    val_per = request.form.get('val_per',None)
    contacts = request.form.get('contacts',None)
    sql = 'insert into res_mgt(host_name,cpu_core,mem_size,val_per,contacts) values("%s","%s","%s","%s","%s")' % (host_name,cpu_core,mem_size,val_per,contacts)
    # print host_name,cpu_core,mem_size,val_per,contacts
    try:
        db.execute(sql)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/del_res', methods=['POST'])
def del_res():
    id = request.form.get('id')
    sql = 'delete from res_mgt where id=%s' % (id)
    try:
        db.execute(sql)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/update_res', methods=['POST'])
def update_res():
    userid = request.form.get('userid',None)
    host_name = request.form.get('host_name',None)
    cpu_core = request.form.get('cpu_core',None)
    mem_size = request.form.get('mem_size',None)
    val_per = request.form.get('val_per',None)
    contacts = request.form.get('contacts',None)
    print userid,host_name,cpu_core,mem_size,val_per,contacts
    # res_dict = {'userid':userid,
    #             'host_name':host_name,
    #             'cpu_core':cpu_core,
    #             'mem_size':mem_size,
    #             'val_per':val_per,
    #             'contacts':contacts}
    sql = 'update res_mgt set host_name="%s",cpu_core="%s",mem_size="%s",val_per="%s",contacts="%s" where id=%s' % (host_name, cpu_core, mem_size, val_per, contacts, userid)
    try:
        db.execute(sql) 
    except:
        return 'error'
    else:
        return 'ok'


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
