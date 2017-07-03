#!/usr/bin/python
#-*-coding:utf-8 -*-
import urllib2
import re
from bs4 import BeautifulSoup
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = "http://www.dytt8.net/html/gndy/dyzz/20170627/54346.html"
response = urllib2.urlopen(url)
page = response.read()
soup = BeautifulSoup(page,'html.parser',from_encoding='utf-8')
#find_all(name,attrs,string)
list = soup.find_all('a',href=re.compile(r'\/html\/(.*)\/(.*)\/\d{8}\/\d{5}\.html'))
with open('test_soup.txt','a') as f:
    for link in list:
        f.write(link['href']+"  "+link.get_text()+'\r\n')
    
    durl = soup.find_all('a',href=re.compile(r'ftp\:\/\/(.*)\.mkv'))
    f.write("=============下载链接============="+'\r\n')
    f.write(str(durl))
f.close()

