#!/usr/bin/python
#-*-coding:utf-8-*-

import  requests,os,time
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


def download(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser',from_encoding='gb2312')
    list = soup.find_all('span', class_="attribute")[::-1]
    title = soup.find('h2').text
    fname="%s下载链接.txt"%title
    with open(fname,'w') as f:
        for url in list:
            #将抓取的链接保存到TXT文档中
            download_url = "thunder://%s"%url.text
            f.write(download_url+'\r\n')
            print '成功抓取:'+download_url
            #使用迅雷下载。将链接拷贝到剪贴板。
            os.system("echo '%s'|pbcopy" % download_url)
            time.sleep(1)
        f.close
    print'抓取完毕'

def test(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser', from_encoding='gb2312')
    list = soup.find_all('span', class_="attribute")[::-1]
    for url in list:
        print url.text
url='http://www.bitfish8.net/otherbtseed/xldl/201311274407.html'
download(url)
#test(url)