#!/usr/bin/python
#-*-coding:utf-8 -*-
import MySQLdb

class HtmlOutputer(object):
    def __init__(self):
        self.datas =[]

    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        db = MySQLdb.connect('127.0.0.1','root','a12345','spider')
        cursor = db.cursor()

        for data in self.datas:
            content_title = data['title'].decode('gbk').encode('utf-8')
            content_link = data['download_link'].decode('gbk').encode('utf-8')
            sql = "insert into dytt(title,link) values('%s','%s')"%(content_title,content_link)
            print sql
            #sql = "insert into dytt(title,link) values('123','345')"
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
        db.close()





