#encoding=utf-8
#
import requests
from pyquery import PyQuery as pq
import smtplib


from email.mime.text import MIMEText
import smtplib

msg = MIMEText('hello, send by python...', 'plain', 'utf-8')

from_addr = 'mingguangzhen@126.com'
password = 'mgz950818'

smtp_server = 'smtp.126.com'
smtp_port = 587
to_addr = 'Aaron_Ming@outlook.com'
server = smtplib.SMTP(smtp_server, smtp_port)
# server = smtplib.SMTP(smtp_server, 465)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
# requests.post('http://localhost/add_user', data={'user':'testuser','pwd':'123'})
# 
# # 

# r = requests.get('https://www.douban.com/photos/album/1629173473/')
# photo_read = pq(r.content).find('.photo_wrap').find('a').find('img')
# print photo_read

	# print pq(title).text()
	# print pq(title).html()
	# print pq(title).html().encode('utf-8')
