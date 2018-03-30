#!/usr/bin/python
#-*- coding:utf8 -*-
from bs4 import BeautifulSoup as bs
import requests,urllib,re
import json

def parser(sid):
    sid = '121353608'
    api = 'http://musicapi.qianqian.com/v1/restserver/ting?method=baidu.ting.song.play&format=jsonp&callback=jQuery17208098337996053833_1513859108469&songid=%s&_=1513859109906' % sid
    response = requests.get(api).text
    # soup = bs(html,'lxml')
    data1=re.findall(r'\((.*)\)',response)[0]
    data2 = json.loads(data1)
    downloadlink =  data2['bitrate']['show_link']
    title =  data2['songinfo']['title']+'.mp3'
    urllib.urlretrieve(downloadlink,title)