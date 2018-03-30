#!/usr/bin/python
#-*- coding:utf8 -*-
from bs4 import BeautifulSoup as bs
import urllib,re,json,os,time
import multiprocessing as mp

url= 'https://www.redtube.com/2723252'
def html_downloader(url):
    return urllib.urlopen(url).read()


def parser(html_content):
    soup = bs(html_content, 'html.parser', from_encoding='utf8')
    links = soup.findAll('a',href=re.compile(r'^\/\d{7}'))
    urls=set()
    for link in links:
        urls.add('https://www.redtube.com'+link['href'])

    data = {}
    result = re.findall(r'\{\"defaultQuality\"\:true.+?\}', html_content)[0]
    jdata = json.loads(result)
    if result:
        data['downloadlink'] = jdata['videoUrl']
        data['title'] = soup.find('h1',{'class':'video_title_text'}).text
    return urls,data

#html_content=html_downloader(url)
#urls,data = parser(html_content)
#print data

def save(content):
    #将爬取的内容保存到txt文档中
    with open('redtube_downloadlist4.txt','a') as f:
        f.write(content)
    f.close()

new_urls=set([url,])
old_urls=set()
#new_urls.add(url)
count =1
num=1
pool=mp.Pool(10)
# crawl_jobs = [pool.apply_async(html_downloader,(url,))for url in new_urls]
# htmls=[content.get() for content in crawl_jobs]
# parser_jobs=[pool.apply_async(parser,(html,)) for html in htmls]
# results = [content.get() for content in parser_jobs]
# old_urls.update(new_urls)
# new_urls.clear()
# for urls,data in results:
#     new_urls.update(urls-old_urls)



while len(new_urls)>0:
     try:
         crawl_jobs = [pool.apply_async(html_downloader,(url,))for url in new_urls]
         htmls=[content.get() for content in crawl_jobs]
         parser_jobs=[pool.apply_async(parser,(html,)) for html in htmls]
         results = [content.get() for content in parser_jobs]
         old_urls.update(new_urls)
         new_urls.clear()
         for urls,data in results:
             print('crawled successfully:%s' % data['title'])
             new_urls.update(urls-old_urls)

             if data['downloadlink'] != '':
                 content = str(num) + '.' + data['title'] + '\r\n' + data['downloadlink'] + '\r\n'
                 pool.apply_async(save,(content,))
                 #save(str(num) + '.' + data['title'] + '\r\n' + data['downloadlink'] + '\r\n')
                 print('crawled successfully:%s'%data['title'])
                 num = num + 1
                 #time.sleep(5)
     except:
         print("crawled fail")


# while len(new_urls)>0:
#      try:
#             htmls=[html_downloader(url) for url in new_urls]
#             result=[parser(html) for html in htmls]
#             old_urls.update(new_urls)
#             print('old_urls nums ',len(old_urls))
#             new_urls.clear()
#             for urls,data in result:
#                 new_urls.update(urls - old_urls)
#                 print('new_urls nums:',len(new_urls))
#                 save(str(num) + '.' + data['title'] + '\r\n' + data['downloadlink'] + '\r\n')
#                 print('crawled successfully:%s' % data['title'])
#                 num = num + 1
#
#             # if count>1000:
#             #     break
#      except:
#          print'craled failed'
#print(html_downloader(url))
# html=html_downloader(url)
# soup = bs(html, 'html.parser', from_encoding='utf8')
# result = re.findall(r'\{\"defaultQuality\"\:true.+?\}',html)[0]
# jdata=json.loads(result)
# print(jdata['videoUrl'])

# api='http://musicapi.qianqian.com/v1/restserver/ting?method=baidu.ting.song.play&format=jsonp&callback=jQuery17208098337996053833_1513859108469&songid=569080829&_=1513859109906'
# html=urllib.urlopen(api).read()
# data = re.findall(r'\((.*)\)',html)[0]
# result=json.loads(data)
# print(type(data))
# print(result)