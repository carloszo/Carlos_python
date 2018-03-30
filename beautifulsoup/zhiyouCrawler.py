#-*-coding:utf-8 -*-
import urllib2,os,sys
from bs4 import BeautifulSoup as bs
reload(sys)
sys.setdefaultencoding( "utf-8" )

global num
num=1
# for i in range(1,8):
#     url= 'http://www.jobui.com/rank/company/view/shanghai/jinrong/2013/?n=%i'%i
#     html= urllib2.urlopen(url).read()
#     soup=bs(html,'html.parser',from_encoding='gb18030')
#     content=soup.findAll('a',{'class':'fs18 mr5'})
#     for title in content:
#         with open('shanghai conpanies.txt','a')as f:
#             f.write(str(num)+'.'+title.text+'\r\n')
#             num += 1

#全国支付公司名单
# for i in range(1,51):
#     url= 'http://www.jobui.com/cmp?keyword=支付&area=全国&n=%i#listInter'%i
#     html= urllib2.urlopen(url).read()
#     soup=bs(html,'html.parser',from_encoding='gb18030')
#     content=soup.findAll('a',{'class':'fs18 mr5'})
#     for title in content:
#         with open('pay conpanies.txt','a')as f:
#             f.write(str(num)+'.'+title.text+'\r\n')
#             num += 1
#
# print('crawled successful!')

#上海支付公司名单
for i in range(1,7):
    url= 'http://www.jobui.com/cmp?keyword=支付&area=上海&n=%i#listInter'%i
    html= urllib2.urlopen(url).read()
    soup=bs(html,'html.parser',from_encoding='gb18030')
    content=soup.findAll('a',{'class':'fs18 mr5'})
    for title in content:
        with open('上海支付公司名单.txt','a')as f:
            f.write(str(num)+'.'+title.text+'\r\n')
            num += 1

print('crawled successful!')



