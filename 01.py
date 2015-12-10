__author__ = 'chi'

import string

str1="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

decode=string.lowercase
encode=decode[-2:-1]+decode[-1]+decode[:-2]
dict1={}
for i in  range(26) :
    dict1[encode[i]]=decode[i]

strtmp=""
for j in str1:
    if j.isalpha():
        strtmp+=dict1[j]
    else:
        strtmp+=j

print strtmp