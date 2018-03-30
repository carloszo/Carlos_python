#usr/bin/python
#-*- coding:utf8 -*-

#autor:Carlos
#目的：利用requests实现模拟登陆
import requests
from selenium import webdriver
url='http://www.linkedin.com'
# c = 'bcookie="v=2&45b43584-5876-447d-84fc-068e7715c2f7"; lang="v=2&lang=zh-cn"; leo_auth_token="GST:8-3dtMFQBNxqw4FrEslqPbbE4tIUY5rr6YfqDUS6yYjIrinYrZ1n-g:1516333871:7b56de94b3f32b2049d9769d99c71094200c3966"; liap=true; JSESSIONID="ajax:2259371697790826151"; li_at=AQEDARe5uRYDrG0fAAABYQyKsioAAAFhMJc2KlEAYcGJg3zRXwfkj9mKu1jR50ROcN10_xRFjK5woX2xqUq3u6HlT2BMKLgmVYqjrwJKg6COI3GngS2w7Wo97DjE1zIWUtsz8B0k80A0swoSp3qljz2U; RT=s=1516333872564&r=https%3A%2F%2Fwww.linkedin.com%2F; visit="v=1&M"; sdsc=22%3A1%2C1516334195559%7ECONN%2C0E651PzlzqyzgKn%2B4FMGtTj4oUqY%3D; _lipt=CwEAAAFhDI_18mbiGcHZ52Hz0BxqvEShZt01mMPL0DACcNW_r-08NH3Laykgq6ScrvBpgkj9asWZiT1xcgGixEgz-N5VmpqQ5hQwGMx-EURhLMrSCUNoV8VAP6vifd7X8RtQuF8lTCNZD2kOY2tG6-VLGE6d8DvZRnw6pg70mYMoPb_3RV0axR4IrIppU_7gdF1vUgkqDWAXdJQ4CPW_bz1MV00-sa3kwTFFy0uv0ZmmhxYo89MFBOpNVAVH-tymJgH5ObD55uVskKwwQ0jq6TVniYXpaNVjNMeP64FcKeyvtTbsZoM; lidc="b=SB10:g=65:u=140:i=1516334224:t=1516364713:s=AQHr2iNcRTAo22nxaihAg32cHD7hmHfm'
# data={'source':'index_nav','form_email':'carlos@cishao.cn','form_password':'Anniivan0202'}
# cookies = {}
# for line in c.split(';'):
#     key,value = line.split('=',1)
#     cookies[key]=value
# headers={
#     'Accept'    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Host' : 'www.linkedin.com',
#     'Referer' : 'http://www.linkedin.com/mynetwork/',
#     'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
# }
# r=requests.get(url,headers=headers,cookies=cookies)
# #print(r.status_code)
# print(r.text)
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_id('login-email').click()
driver.find_element_by_id('login-email').clear()
driver.find_element_by_id('login-email').send_keys('carlos@lieneng.com.cn')
driver.find_element_by_id('login-password').click()
driver.find_element_by_id('login-password').clear()
driver.find_element_by_id('login-password').send_keys('Anniivan0202')
driver.find_element_by_id('login-submit').click()
driver.get('http://www.linkedin.com/in/michael-xu-6930991/')
print driver.page_source
#driver.close()