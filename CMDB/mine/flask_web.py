#encoding=utf-8
#
from flask import Flask,render_template,request,session,redirect,url_for
from config import db_config,page_config
from dbutil.dbutil import DB
import json
import sys,os

# print db_config
reload(sys)
sys.setdefaultencoding('utf-8')
db = DB(host=db_config['host'], mysql_user=db_config['user'], mysql_pass=db_config['passwd'], mysql_db=db_config['db'])
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/login',methods=['GET','POST'])
def login():
    sql = 'select username,password from user'
    res = db.execute(sql)
    user_info = {}
    for i in res:
        user_info[i['username']] = i['password']
    print user_info
    print type(user_info)
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        print user,pwd
        if user not in user_info:
            return '用户不存在!'
        elif user_info[user] == pwd:
            session['username'] = user
            return redirect(url_for('user'))
        else:
            return '密码错误！'


# create table user (id int(4) primary key not null auto_increment, username varchar(255) not null, password varchar(255) not null);
@app.route('/user')
def user():
    sql = 'select * from user'
    res = db.execute(sql)
    return render_template('user_info.html', user_info=res)

@app.route('/user/add', methods=['POST'])
def user_add():
    username = request.form.get('username', None)
    password = request.form.get('password', None)
    role = request.form.get('role', None)

    sql = 'insert into user(username,password,role) values("%s","%s","%s")' % (username,password,role)
    try:
        db.execute(sql)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/user/update', methods=['POST'])
def user_update():
    id = request.form.get('id', None)
    password = request.form.get('update_password', None)
    role = request.form.get('update_role', None)

    sql = 'update user set password="%s", role="%s" where id="%s"' % (password,role,id)
    # print sql
    try:
        db.execute(sql)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/user/delete', methods=['POST'])
def user_delete():
    id = request.form.get('id', None)

    sql = 'delete from user where id="%s"' % (id)
    try:
        db.execute(sql)
    except:
        return 'error'
    else:
        return 'ok'

# @app.route('/vm_assets_data')
# def vm_assets_data():
#     sql = 'select * from vm_assets'
#     res = json.dumps(db.execute(sql))
#     return res

@app.route('/vm_assets')
def vm_assets():
    sql = 'select * from vm_assets'
    res = db.execute(sql)
    return render_template('vm_assets.html',get_vmassets=res)

@app.route('/vm_assets/add', methods=['POST'])
def vm_assets_add():
    ip_addr = request.form.get('ip_addr',None)
    app_name = request.form.get('app_name',None)
    hostname = request.form.get('hostname',None)
    vc_name = request.form.get('vc_name',None)
    cpu = request.form.get('cpu',None)
    memory = request.form.get('memory',None)
    disk = request.form.get('disk',None)
    os = request.form.get('os',None)
    status = request.form.get('status',None)
    office_name = request.form.get('office_name',None)
    office_contact = request.form.get('office_contact',None)
    office_phone = request.form.get('office_phone',None)
    object_contact = request.form.get('object_contact',None)
    object_phone = request.form.get('object_phone',None)
    create_date = request.form.get('create_date',None)
    end_date = request.form.get('end_date',None)
    notes = request.form.get('notes',None)

    sql = 'insert into vm_assets(ip_addr,app_name,hostname,vc_name,cpu,memory,disk,os,status,office_name,office_contact,office_phone,object_contact,object_phone,create_date,end_date,notes) values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (ip_addr,app_name,hostname,vc_name,cpu,memory,disk,os,status,office_name,office_contact,office_phone,object_contact,object_phone,create_date,end_date,notes)
    try:
        db.execute(sql)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/vm_assets/delete', methods=['POST'])
def vm_assets_del():
    id = request.form.get('id', None)
    sql = 'delete from vm_assets where id=%s' % (id)
    try:
        db.execute(sql)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/vm_assets/update', methods=['POST'])
def vm_assets_update():
    print request.form
    id = request.form.get('id', None)
    # print 'id'+id
    update_ip_addr = request.form.get('update_ip_addr',None)
    print 'Theis ip' + update_ip_addr
    update_app_name = request.form.get('update_app_name',None)
    update_hostname = request.form.get('update_hostname',None)
    update_vc_name = request.form.get('update_vc_name',None)
    update_cpu = request.form.get('update_cpu',None)
    update_memory = request.form.get('update_memory',None)
    update_disk = request.form.get('update_disk',None)
    update_os = request.form.get('update_os',None)
    update_status = request.form.get('update_status',None)
    update_office_name = request.form.get('update_office_name',None)
    update_office_contact = request.form.get('update_office_contact',None)
    update_office_phone = request.form.get('update_office_phone',None)
    update_object_contact = request.form.get('update_object_contact',None)
    update_object_phone = request.form.get('update_object_phone',None)
    update_create_date = request.form.get('update_create_date',None)
    update_end_date = request.form.get('update_end_date',None)
    update_notes = request.form.get('update_notes',None)

    sql = 'update vm_assets set ip_addr="%s",app_name="%s",hostname="%s",vc_name="%s",cpu="%s",memory="%s", disk="%s", os="%s", status="%s", office_name="%s", office_contact="%s", office_phone="%s", object_contact="%s", object_phone="%s", create_date="%s", end_date="%s", notes="%s" where id=%s' % (update_ip_addr, update_app_name, update_hostname, update_vc_name, update_cpu, update_memory, update_disk, update_os, update_status, update_office_name, update_office_contact, update_office_phone, update_object_contact, update_object_phone, update_create_date, update_end_date, update_notes, id)
    print sql
    try:
        db.execute(sql)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/layout')
def layout():
    return render_template('layout.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)



