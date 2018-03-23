#usr/bin/python
#-*- coding:utf8 -*-

#autor:Carlos
#目的：利用requests,cookies实现模拟登陆
import requests
from bs4 import BeautifulSoup as bs

#url='https://www.zhihu.com/topic/19681246/hot'
url='https://www.zhihu.com/inbox'
c='aliyungf_tc=AQAAAGkdDD3TkwAAMRw5cW/BayKHVXgK; capsion_ticket="2|1:0|10:1516344408|14:capsion_ticket|44:ZmMxZTkxMDMxZDdlNDg4N2I1NjM5ZDY5ZmIyZGU3N2Q=|86dc16c18bc31af2b154fe0cf11b02ffeded9f93d436939c1e084b72b6cb12fc"; z_c0="2|1:0|10:1516344431|4:z_c0|92:Mi4xMVk2OUFnQUFBQUFBNEd5XzdsMEREU1lBQUFCZ0FsVk5iLUpPV3dETWU0akVQbmpDV3Rqa2IyckhLQ1FQaUxYZmt3|de5854b20742cbbe577865e046a1fe95dedaa2c76ec4ba3534b46c47e80a9c3f'
data={'source':'index_nav','form_email':'carlos@cishao.cn','form_password':'Anniivan0202'}
cookies = {}
for line in c.split(';'):
    key,value = line.split('=',1)
    cookies[key]=value
headers={
    'Accept'    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Host' : 'www.zhihu.com',
    'Referer' : 'https://www.zhihu.com/signup?next=%2F',
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
r=requests.get(url,headers=headers,cookies=cookies)
soup = bs(r.text,'html.parser',from_encoding='13080')
#print(r.status_code)
#titles = soup.findAll('a',{'class':'pm-touser author-link'})
#print(titles)
print(soup.title)
