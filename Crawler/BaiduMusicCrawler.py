#!/urs/bin/python
#-*- coding:utf8 -*-
from bs4 import BeautifulSoup as bs
import urllib
import re
import json
import os

def get_musicid(url):
#url='http://music.baidu.com/top/dayhot'
    html = urllib.urlopen(url).read()
    soup = bs(html,'lxml',from_encoding='utf8')
    urls = soup.findAll('a',href=re.compile(r'/song/(\d+)'))
    musicidlist=set()
    for url in urls:
        musicidlist.add(url['href'].split('/')[-1])
    return musicidlist

def parser(api):
    #api="http://musicapi.qianqian.com/v1/restserver/ting?method=baidu.ting.song.play&format=jsonp&callback=jQuery17208098337996053833_1513859108469&songid=%s&_=1513859109906" % musicid
    html=urllib.urlopen(api).read()
    data = re.findall(r'\((.*)\)',html)[0]
    jsondata = json.loads(data)
    songtitle=jsondata['songinfo']['title']
    songdownloadlink=jsondata['bitrate']['file_link']
    songformat=jsondata['bitrate']['file_extension']
    #print(jsondata)
    return songtitle,songformat,songdownloadlink

def music_download(filename,downloadlink):
    path= '/Users/apple/documents/music/' + filename
    if(os.path.exists('/Users/apple/documents/music')==False):
        os.makedirs('/Users/apple/documents/music/')
    elif(os.path.isfile(path)==False):
            urllib.urlretrieve(downloadlink, '/Users/apple/documents/music/' + filename)
    else:
        return

url='http://music.baidu.com/top/dayhot'
musicidlist = get_musicid(url)
for songid in musicidlist:
    try:
        api = "http://musicapi.qianqian.com/v1/restserver/ting?method=baidu.ting.song.play&format=jsonp&callback=jQuery17208098337996053833_1513859108469&songid=%s&_=1513859109906"%songid
        songtitle,songformat,songdownloadlink=parser(api)
        filename=songtitle+'.'+songformat
        music_download(filename,songdownloadlink)
        print(songtitle+' downloaded successfully!')
    except:
        print('download fail')
#parser(api)
#print(musicidlist)
