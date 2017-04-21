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
    try:
        html = urlopen(urlstring)
        bs0bj = BeautifulSoup(html,'lxml')
        try:
            class_values = set()
            with open('class_values.txt','a') as f:
                for item in bs0bj.body.find_all("",{"class":re.compile("^.*")}):
                    if len(item['class'])==1:
                        class_values.add(item['class'][0])
                    else:
                        for i in item['class']:
                            class_values.add(i)
                for item in class_values:
                    if '-' in item:
                        raw = item.split('-')
                        item = ' '.join(raw)
                    elif '_' in item:
                        raw = item.split('_')
                        item = ' '.join(raw)
                    print("mess",item,file=f)
            #print("done")
        except IOError:
            pass
    except:
        pass
'''with open('urllist.txt') as f:
    for each_line in f:
        getTag(each_line)'''
getTag('http://8.7k7k.com/thread-1453189-1-1.html')