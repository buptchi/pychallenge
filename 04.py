__author__ = 'chi'


import urllib2
import re


tt=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read()
qq=re.compile('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]').findall(tt)

print(qq)




























