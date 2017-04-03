# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:01:47 2017

@author: aes alienum
"""
from urllib.request import urlopen #从Python内置urllib库导入urlopen函数
from bs4 import BeautifulSoup #从bs4（Beautifulsoup4）导入BeautifulSoup函数
import re #导入正则表达式（regular expression）

html = urlopen("http://tech.163.com/17/0328/19/CGL076T200097U7T.html") #解析一个url链接并实例化为html（html只是一个名字）
bs0bj = BeautifulSoup(html,'lxml') #将经过解析的url作为参数传给bs函数，并指定使用lxml解析器，生成一个bs实例，起个名字叫bs0bj(beautifulsoup 0bject)


#打印标题
print("title is: ",end='')
title = bs0bj.find("div",{"class":"post_content_main"}).h1 #find函数，在bs变量结构中寻找class叫post_content_main的div（divsion，分区），
#并打印该分区下的h1元素
print(title.get_text())
#调用get_text()方法去掉我们不需要的html描述


print("post time: ",end='')
post_time = bs0bj.find("div",{"class":"post_time_source"}).get_text()
print(post_time)


print("content: ",end='')
for paragraph in bs0bj.find("div",{"class":"post_text"}).findAll("p"):
    print(paragraph.get_text())
#类似上面，只不过多加了一层findAll，就是在找到的分区中寻找所有的p（paragraph，段落）元素，
#（之所以用findAll是因为html结构是每段作为一个p元素）

#hot-posts > div.tie-list
"""
print("comment_list: ")
for each_comment in bs0bj.find("div",{"class":"tie-list"}).findAll("div",{"class":"single-tie"}):
    author_info = each_comment.find("div",{"class":"tie-author"})
    name = author_info.a
    time = author_info.find("span",{"class":"tie-time"})
    print(time)
    cnt = author_info.find("p",{"class":"tie-cnt"})
    print(cnt)
tie = bs0bj.find("div",{"class":"post_comment"})
"""