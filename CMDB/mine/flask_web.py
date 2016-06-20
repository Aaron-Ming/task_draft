#encoding=utf-8
#
from flask import Flask,render_template

import sys


reload(sys)
sys.setdefaultencoding("utf-8")
app = Flask(__name__)
app.secret_key = '1234567890qwertyuiopasdfghjkl'


@app.route('/login',methods=['GET','POST'])
def login():
    return '这是登录页面'

@app.route('/vm_assets')
def vm_assets():
    return render_template('vm_assets.html')

@app.route('/layout')
def layout():
    return render_template('layout.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2898, debug=True)