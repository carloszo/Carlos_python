#!/usr/bin/python
#-*-coding:utf-8 -*-
import urllib2

class HtmlDownloader(object):
    

    def download(self,url):
        if url is None:
            return None
        request = urllib2.Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14')
        response = urllib2.urlopen(request)
        if response.getcode() != 200:
            return None
        return response.read()
