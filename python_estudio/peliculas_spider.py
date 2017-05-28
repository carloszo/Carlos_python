#!/usr/bin/python
#-*-coding:utf-8 -*-
import urllib2
import os
import re
import time

class Peliculas_Spider(object):
    def __init__(self,website):
        self.website=website

#getPeliculaList()的功能为抓取内容页的链接，通过正则过滤URL并返回结果。
    def  getPeliculaList(self,index):
        list =[]
        for i in range(1,index+1):
            url ="http://www.ygdy8.net/html/gndy/oumei/list_7_"+str(i)+".html"
            request = urllib2.urlopen(url)
            page = request.read()
            pattern = re.compile( "\<a href\=\"(.*)\" class=\"ulink\"\>")
            list += re.findall(pattern,page)
        return list

#getPeliculaUrl()的功能为抓取下载链接。
    def getPeliculaUrl(self,list):
        downloadlink=[]
        for i in range(len(list)):
            request = urllib2.urlopen(self.website+list[i])
            page = request.read()
            #pattern = re.compile("\<a href\=\"ftp\:\/\/(.*)\"")
            pattern = re.compile( "\"\#fdfddf\"\>\<a href\=\"(.*?)\>")
            downloadlink+=re.findall(pattern,page)
        return downloadlink

#SaveList()将getPeliculaUrl()得到的链接列表保存到txt 文件中。
    def SaveList(self,content):
        path = os.path.abspath('.')
        filename = "/list"+time.strftime("%Y%m%d%H")+".txt"
        with open(path+filename,'w') as f:
            for i in range(len(content)):
                f.write(content[i])
                f.write("\n")
            f.close()




peliculas = Peliculas_Spider('http://www.ygdy8.net')
list = peliculas.getPeliculaList(160)
downloadlink = peliculas.getPeliculaUrl(list)
peliculas.SaveList(downloadlink)
#test
1111
2222
