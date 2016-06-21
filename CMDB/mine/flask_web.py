#encoding=utf-8
#
from flask import Flask,render_template
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

@app.route('/vm_assets_data')
def vm_assets_data():
    sql = 'select * from vm_assets'
    # print db.execute(sql)
    # return 'hh'
    res = json.dumps(db.execute(sql))
    return res


@app.route('/vm_assets')
def vm_assets():
    sql = 'select * from vm_assets'
    # print db.execute(sql)
    # return 'hh'
    # res = json.dumps(db.execute(sql))
    res = db.execute(sql)
    return render_template('vm_assets.html',get_vmassets=res)

@app.route('/layout')
def layout():
    return render_template('layout.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2898, debug=True)



