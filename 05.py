__author__ = 'chi'


import urllib2
import re

str1='63579'
while True:
    tt=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str1).read()
    print(tt)
    qq=re.search('\d+',tt)
    if qq:
        str1=qq.group(0)
        print(str1)
    else:
        break

print(tt)



















