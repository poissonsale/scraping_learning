# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 15:31:26 2017

@author: aes alienum
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://bbs.tianya.cn/post-stocks-1841155-1.shtml')
bs0bj = BeautifulSoup(html,'lxml')

title = set()   #type set picks only the non-repeated ones
def tillNone(family):
    if family.string is not None:   #'cause if a Tag has more than one child, it’s not clear what .string should refer to, so .string is defined to be None
         title.add(family.string)
    else:
        for each_child in family:
            tillNone(each_child)
def getTitle(bs0bj):
    try:
        #print(len(bs0bj.findAll("",class_=re.compile('.*title(.*)'))))
        for posbl_div in bs0bj.findAll("",class_=re.compile('.*title(.*)')):    #possible division
            tillNone(posbl_div)
    except AttributeError as attrerr:
        print("aaa"+str(attrerr))   #"aaa"is for informing that it's failed for AttributeError and then the error message come as followed

getTitle(bs0bj)
print("post name:")
for t in title:
    print(t)
