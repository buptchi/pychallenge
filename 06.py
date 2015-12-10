__author__ = 'chi'

import pickle
import urllib2

tt=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()
obj2=pickle.loads(tt)
print '\n'.join([''.join([p[0] * p[1] for p in row]) for row in obj2])
