#!/usr/python/bin
#-*- coding:utf8 -*-

import re
import urllib
from bs4 import BeautifulSoup as bs

resq =  urllib.urlopen('https://es.wikipedia.org/wiki/Colombia').read()
soup = bs(resq,'html.parser')
listUrl = soup.findAll('a',href=re.compile(r'^/wiki'))
n=1
for url in listUrl:
    if not re.search('\.(jpg|JPG)$',url['href']):
        print n,"<---->",url.get_text(),"<------------------------>","https://es.wikipedia.org"+url['href']
        n=n+1
