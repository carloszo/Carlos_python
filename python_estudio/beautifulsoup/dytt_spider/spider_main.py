#!/usr/bin/python
#-*-coding:utf-8 -*-
import url_manager,html_downloader,html_parser,html_outputer,time
import traceback
'''from html_downloader import HtmlDownloader
from url_manager import UrlManager
from html_parser import HtmlParser
from html_outputer import HtmlOutputer'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'crawled %d:%s'%(count,new_url)
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 10:
                    break
                count = count +1

            except:
                print "crawled faild %s"%new_url
    
        self.outputer.output_html()
        #print self.outputerdata['download_link']

if __name__=='__main__':
        root_url = 'http://www.ygdy8.net/html/gndy/dyzz/20170116/52990.html'
        obj_spider = SpiderMain()
        obj_spider.craw(root_url)
