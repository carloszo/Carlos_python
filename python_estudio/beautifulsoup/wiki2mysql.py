#!/usr/python/bin
#-*- coding:utf8 -*-

import re
import urllib
from bs4 import BeautifulSoup as bs
import pymysql.cursors

resq =  urllib.urlopen('https://es.wikipedia.org/wiki/Colombia').read()
soup = bs(resq,'html.parser')
listUrl = soup.findAll('a',href=re.compile(r'^/wiki'))

for url in listUrl:
    if not re.search('\.(jpg|JPG)$',url['href']):
        print url.get_text(),"<------------------------>","https://es.wikipedia.org"+url['href']

        #获取数据库链接
        connection=pymysql.connect(
            host='localhost',
            user='root',
            password='a12345',
            db='wikiurl',
            charset='utf8'
        )
        #获取会话指针
        sql="insert into `wikiurl`(`urlname`,`urlhref`)values(%s,%s)"
        try:
            with connection.cursor() as cursor:
        #   创建sql语句

        #执行sql
                cursor.execute(sql,(url.get_text(),'https://es.wikipedia.org'+url['href']))
                #cursor.execute(sql)
        #提交
                connection.commit()

        finally:
            connection.close()

