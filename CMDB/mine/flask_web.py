#encoding=utf-8
#
from flask import Flask,render_template,request
from config import db_config,page_config
from dbutil.dbutil import DB
import json
import sys,os

# print db_config

db = DB(host=db_config['host'], mysql_user=db_config['user'], mysql_pass=db_config['passwd'], mysql_db=db_config['db'])
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/login',methods=['GET','POST'])
def login():
    return '这是登录页面'

@app.route('/user')
def user():
    return '这个是用户目录'

@app.route('/vm_assets_data')
def vm_assets_data():
    sql = 'select * from vm_assets'
    res = json.dumps(db.execute(sql))
    return res

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

@app.route('/vm_assets/update')
def vm_assets_update():
    return True

@app.route('/layout')
def layout():
    return render_template('layout.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)



