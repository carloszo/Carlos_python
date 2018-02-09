#!/usr/python/bin
#-*- coding:utf8 -*-

from bs4 import BeautifulSoup as bs
import urllib
url='http://www.dytt8.net'
resq=urllib.urlopen(url).read()
soup = bs(resq,'html.parser',from_encoding='gb18030')
print soup.prettify()