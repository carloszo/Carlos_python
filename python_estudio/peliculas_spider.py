#!/usr/bin/python
#-*- coding:utf-8 -*-

import urllib2
import re
import os
import time

class Peliculas_Spider(object):
    def __init__(self,website):
        self.website = website

    def GetList(self,index):
        list = []
        for i in range(1,index+1):
            request = urllib2.urlopen("http://www.dytt8.net/html/gndy/dyzz/list_23_"+str(i)+".html")
            page = request.read().decode('utf-8')
            #linkpattern =re.compile('\<a href\=\"(.*)\" class\=\"ulink\"\>')
            pattern =re.compile('class\=\"ulink\"\>(.*)\<\/a\>')
            list += re.findall(pattern,page)
        return list

    def SaveList(self,content):
        path = os.path.abspath('.')
        filename = '\list_'+time.strftime("%Y%m%d%H")+".txt"
        with open(path+filename,'w') as f:
            for i in range(len(content)):
                f.write(content[i])
                f.write("\n")
            f.close()



peliculas = Peliculas_Spider("http://www.dytt8.net")
list = peliculas.GetList(3)
print list
#peliculas.SaveList(list)

