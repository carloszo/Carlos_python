#!/usr/python/bin
# -*- coding:utf8 -*-
import urllib,re
from bs4 import BeautifulSoup
import pymysql

url = 'http://www.ygdy8.net'
resq = urllib.urlopen(url).read()
soup =BeautifulSoup(resq,'html.parser',from_encoding='gb13080')
listurl=[]
listurl = soup.select('.contain ul li a')
cate_url=[]
for url in listurl:
    cate_url.append('http://www.ygdy8.net'+url['href'])
cate_url =cate_url[:-2]
resq1 = urllib.urlopen(cate_url[0]).read()
soup1 =BeautifulSoup(resq1,'html.parser',from_encoding='gb13080')
pages= soup1.select('.x select option')
cate_listurl=[]
for i in range(0,len(pages)):
    cate_listurl.append(cate_url[0][:-10]+pages[i]['value'])

resq1 = urllib.urlopen(cate_listurl[0]).read()
soup1 =BeautifulSoup(resq1,'html.parser',from_encoding='gb13080')
contentlis= soup1.select('.co_content8 ul a')
for url in contentlis:
    pageurl = 'http://www.ygdy8.net'+url['href']
    resq = urllib.urlopen(pageurl).read()
    soup = BeautifulSoup(resq, 'html.parser')
    print soup.title.string
    print soup.select('#Zoom span table a')[0]['href']



