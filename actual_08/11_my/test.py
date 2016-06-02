#encoding=utf-8
#
import requests
from pyquery import PyQuery as pq


# requests.post('http://localhost/add_user', data={'user':'testuser','pwd':'123'})
# 
# 

r = requests.get('https://www.douban.com/photos/album/1629173473/')
photo_read = pq(r.content).find('.photo_wrap').find('a').find('img')
print photo_read

	# print pq(title).text()
	# print pq(title).html()
	# print pq(title).html().encode('utf-8')
