#!/usr/bin/python
#-*- coding:utf8 -*-
import urllib2
from bs4 import BeautifulSoup
path= '/Users/apple/PycharmProjects/Carlos_python/Crawler/qq_number.html'
htmlfile = open(path, 'r')
htmlhandle = htmlfile.read()
soup = BeautifulSoup(htmlhandle, 'lxml')
lis = soup.findAll('li',{'class':'list_item'})
for li in lis:
    num = li.find('a', {'class': 'avatar'})['_uin']
    name = li.find('p',{'class':'member_nick'}).text.strip()
    content = name+':'+num+'\r\n'
    print content
    with open('qq_numbers_list.txt','a') as f:
        f.write(content.encode('utf8'))
    f.close()

