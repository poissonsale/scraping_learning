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

title = set()
def tillNone(family):
    if family.string is not None:
         title.add(family.string)
    else:
        for each_child in family:
            tillNone(each_child)
def getTitle(bs0bj):
    try:
        #print(len(bs0bj.findAll("",class_=re.compile('.*title(.*)'))))
        for posbl_div in bs0bj.findAll("",class_=re.compile('.*title(.*)')):
            tillNone(posbl_div)
    except AttributeError as attrerr:
        print("aaa"+str(attrerr))

getTitle(bs0bj)
print("post name:")
for t in title:
    print(t)