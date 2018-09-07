#!/usr/bin/python
#-*-coding:utf-8 -*-
# import urllib2
# import re
# from bs4 import BeautifulSoup
# import os
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
#
# url = "http://www.dytt8.net/html/gndy/dyzz/20170627/54346.html"
# response = urllib2.urlopen(url)
# page = response.read()
# soup = BeautifulSoup(page,'html.parser',from_encoding='gb13080')
# #find_all(name,attrs,string)
# list = soup.find_all('a',href=re.compile(r'\/html\/(.*)\/(.*)\/\d{8}\/\d{5}\.html'))
# with open('test_soup.txt','a') as f:
#     for link in list:
#         f.write(link['href']+"  "+link.get_text()+'\r\n')
#
#     durl = soup.find_all('a',href=re.compile(r'ftp\:\/\/(.*)\.mkv'))
#     f.write("=============下载链接============="+'\r\n')
#     f.write(str(durl))
# f.close()
#
import random
a = ['泰','全','朗','健','怡','宜','宁']
b=['静','益' ,'寿','精','气' ,'神','顺','补','温','灵','平','和' ,'延','念' ,'旺','衡' ,'润' ,'源']
c=['卓','秀','怡','丽','纤','泽','蓉']
d=['安','康','清' ,'姿','欣','轩','丽','授','纤']
print len(a)
print len(b)
print len(d)
# for i in range(0,21):
#     num1 = random.randint(0, 36)
#     num2 = random.randint(0, 23)
#     num3 = random.randint(0, 8)
#     print(a[num1]+b[num2]+d[num3])
for i in range(0,len(a)-1):
    num1 = random.randint(0, 36)
    num2 = random.randint(0, 22)
    num3 = random.randint(0, 8)
    for j in range(0,len(b)-1):
        for k in range(0,len(d)-1):
            str = a[i] + b[j] + d[k]
            print str+',',
