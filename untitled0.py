# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 22:11:40 2017

@author: 81267
"""

#from urllib.request import urlopen
#from bs4 import BeautifulSoup
"""
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bs0bj = BeautifulSoup(html.read(),"lxml")
#print(bs0bj.find("img",{"src":"../img/gifts/img1.jpg"
#                        }).parent.previous_sibling.get_text())
print(bs0bj.h1)
def gettitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs0bj = BeautifulSoup(html.read(),"lxml")
        title = bs0bj.body.h1
    except AttributeError as a:
        return None
    return title

title = gettitle("http://www.pythonscraping.com/pages/page3.html")
if title == None:
    print("Title could not be found")
else:
    print(title)

alice = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs0bj = BeautifulSoup(alice,"lxml")

namelist = bs0bj.findAll("span",{"class":"green"})
for name in namelist:
    print(name)
"""
"""
import re
html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bs0bj = BeautifulSoup(html,'lxml')
for link in bs0bj.find("div",{"id":"bodyContent"}).findAll("a",
                      href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])"""
        
        
        
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://tech.163.com/17/0328/19/CGL076T200097U7T.html")
bs0bj = BeautifulSoup(html,'lxml')
#soup = bs0bj.select('#epContentLeft > h1')[0].text
for title in bs0bj.findAll("div",{"class":"post_content_main"}):
    #if 'h1' in title:
    print(title.h1.get_text())
#re.compile("^(.*content_main(.*))")
#"div",{"class":"post_content_main"}
#print(soup)
