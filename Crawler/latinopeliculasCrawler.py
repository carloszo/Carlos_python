#!/usr/bin/python
#-*- coding:utf8 -*-
from bs4 import BeautifulSoup as bs
import urllib2
import  re
import pymysql
import os

def html_downloader(url):
    #读取网页内容
    request = urllib2.Request(url)
    request.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')
    opener = urllib2.build_opener()
    f = opener.open(request)
    return f.read()

def parser_list(html_content):
    #把网页内容传递给BeautifulSoup解析
    soup = bs(html_content, 'html.parser', from_encoding='gb18030')
    #新建set,用以存储下一步爬取的链接。
    new_urls = set()
    #downloadlink存储下载链接
    downloadlink=''
    #获取网页中所有的内容页链接
    urllist = soup.findAll('td',{'class':'vertThseccion'})
    for item in urllist:
        url = item.find('a')['href']
        new_urls.add(url)
    return new_urls

def parser_page(urllist):
    torrentlist=set()
    for url in urllist:
        html_content = html_downloader(url)
        soup = bs(html_content, 'html.parser', from_encoding='gb18030')
        torrent = soup.find('a',{'class':'fichabtndes linktorrent'})
        torrentlist.add(torrent['href'])
    return torrentlist
def save(content):
    #将爬取的内容保存到txt文档中
    with open('downloadlist.txt','a') as f:
        f.write(content)
    f.close()

url = 'http://www.subtorrents.io/peliculas-subtituladas/page/2/?filtro=audio-latino'
content = html_downloader(url)
list = parser_list(content)
torrentlist = parser_page(list)
for torrent in torrentlist:
    print(torrent)