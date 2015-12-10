__author__ = 'chi'


import urllib2

"""
url = 'http://www.pythonchallenge.com/pc/return/evil4.jpg'
username = 'huge'
password = 'file'
p = urllib2.HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)

handler = urllib2.HTTPBasicAuthHandler(p)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)

page = urllib2.urlopen(url).read()
print(page)
"""

import requests
"""
username = 'huge'
password = 'file'
url = 'http://www.pythonchallenge.com/pc/return/evil4.jpg'
r = requests.get(url, auth=(username, password))
page =r.content
"""

"""
params={'a':5}
tt=requests.get("http://www.google.com",params)
print(tt.text)
#print(tt.content)
print(tt.url)
print(tt.status_code)
print(tt.reason)
print(tt.encoding)
"""



tt=open('evil2.gfx','rb').read()
print(tt[:1000])
types = ['jpg','png','gif','png','jpg']
for i in range(5): open('evil2%d.%s' % (i, types[i]),'wb').write(tt[i::5])



