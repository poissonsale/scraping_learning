# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 17:42:31 2017

@author: 81267
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from bs4 import NavigableString

def getTag(urlstring):
    html = urlopen(urlstring)
    bs0bj = BeautifulSoup(html,'lxml')
    
    class_values = set()
    with open('class_values.txt','a') as f:
        for item in bs0bj.body.find_all("",{"class":re.compile("^.*")}):
            if len(item['class'])==1:
                class_values.add(item['class'][0])
            else:
                for i in item['class']:
                    class_values.add(i)
        for item in class_values:
            print("mess",item,file=f)
with open('urllist.txt') as f:
    for each_line in f:
        getTag(each_line)