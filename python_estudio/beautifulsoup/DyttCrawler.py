#!/usr/bin/python
#-*- coding:utf8 -*-
from bs4 import BeautifulSoup as bs
import urllib2
import  re
import pymysql
import os

#autor:Carlos
#功能：利用beautifulsoup，urllib2爬取ygdy8.net中电影下载链接


def html_downloader(url):
    #读取网页内容
    html_content = urllib2.urlopen(url).read()
    return html_content

def parser(html_content):
    #把网页内容传递给BeautifulSoup解析
    soup = bs(html_content, 'html.parser', from_encoding='gb18030')
    #新建set,用以存储下一步爬取的链接。
    new_urls = set()
    #downloadlink存储下载链接
    downloadlink=''
    #获取网页中所有的内容页链接
    urllist = soup.findAll('a',href=re.compile(r'/html/gndy/\w{4}/.*/'))
    #将内容页链接拼接完整后存储至set new_urls中
    for url in urllist :
        new_urls.add('http://www.ygdy8.net'+url['href'])
    #获取下载链接
    if soup.find('a',href=re.compile(r'ftp\:\/\/(.*)')):
        downloadlink=soup.find('a',href=re.compile(r'ftp\:\/\/(.*)'))['href']
    return new_urls,downloadlink

def save(content):
    #将爬取的内容保存到txt文档中
    with open('downloadlist.txt','a') as f:
        f.write(content)
    f.close()

rooturl='http://www.ygdy8.net'
'''
html = html_downloader(url)
urls,download = parser(html)
print len(urls)
for url in urls:
    print url
'''
#uncrawled_list为未爬取链接库，开始为空，格式为set,可以自动过滤重复链接。
uncrawled_list=set()
#crawled_list为已爬取链接库
crawled_list =set()
#将最开始爬取的链接放入未爬取链接库中
uncrawled_list.add(rooturl)
#download_list = set()
#count和num均为计数器，count记录爬取链接数量，num记录成功爬取下载链接数量。
count=0
num = 1
#未爬取链接库不为空时处于循环状态
while len(uncrawled_list)>0:
    try:
        count = count + 1
        #从未爬取链接库中取出一个新的url
        newurl = uncrawled_list.pop()
        #判断新的url是否在已爬取链接库中
        if newurl not in crawled_list:
            html_content = html_downloader(newurl)
        #new_urls,downloadlink = parser(html_content)
        #url_manager(new_urls)
            #将已爬过的链接放入crawled_list
            crawled_list.add(newurl)
            #返回新的内容页链接和下载链接
            new_urls,downloadlink = parser(html_content)
            #打印爬取状态
            print "crawled %s:%s" % (count, newurl)
            #判断new_urls是否为空
            if new_urls is not None or len(new_urls)!=0:
                for url in new_urls:
                    #将new_urls加入uncrawled_list
                    uncrawled_list.add(url)
            #判断downloadlink是否为空
            if downloadlink!='':
                #将downloadlink格式
                downloadurl = downloadlink.encode("utf8")
                save(str(num)+'.'+downloadurl+'\r\n')
                #download_list.add(downloadurl)
                num=num+1
    except:
        print "crawl failed"




