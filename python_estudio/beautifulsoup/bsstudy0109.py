#!/usr/python/bin
#-*- coding:utf8 -*-
from bs4 import BeautifulSoup as bs
import urllib
url ='http://www.ygdy8.net'
resq=urllib.urlopen(url).read()
soup =bs(resq,'html.parser',from_encoding='gb13080')
tag = soup.select('.co_area2')[0].contents
head=soup.head
print head.contents[1]
for child in head.children:
    print child