__author__ = 'chi'

import urllib2
import re


tt=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read()
qq=re.compile('below:.*<!--(.*)-->', re.S).findall(tt)[0]

cc={}
for j in qq:
    cc[j]=cc.get(j,0)+1

str1="".join(re.compile('[a-z]').findall(qq))

"""
for j in qq:
    if j.isalpha():
        str1+=j
"""

print(cc)
print(str1)
















