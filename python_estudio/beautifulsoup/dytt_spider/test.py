#!/usr/bin/python
#-*-coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
from html_downloader import HtmlDownloader
from html_parser import HtmlParser
from url_manager import UrlManager
from html_outputer import HtmlOutputer
url = 'http://www.dytt8.net/html/gndy/dyzz/20170630/54374.html'

'''response = urllib2.urlopen(url)
content = response.read()
print content

content2 = '<h1><font color=#07519a>2017年动画《蓝精灵：寻找神秘村》国英双语.BD中英双字幕</font></h1>'
soup = BeautifulSoup(content2,'html.parser',from_encoding='utf-8')
title = soup.find('h1').find('font').get_text()
print title
'''


d = HtmlDownloader()
content = d.download(url)

hp = HtmlParser()
new_urls,new_data = hp.parse(url,content)

um = UrlManager()
um.add_new_urls(new_urls)

outputer = HtmlOutputer()
outputer.collect_data(new_data)
outputer.output_html()

for url in new_urls:
    print url +"\r\n"


print "=========================="
print new_data

