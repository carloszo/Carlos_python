#-*- coding:utf-8 -*-
import cookielib
import urllib2,urllib
import ssl
ssl._create_default_https_context=ssl._create_unverified_context
c = cookielib.CookieJar()
cookie = urllib2.HTTPCookieProcessor(c)
opener=urllib2.build_opener(cookie)
req=urllib2.Request('https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.5335842024888449')
req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
req.add_header('Referer','https://kyfw.12306.cn/otn/login/init')
codeimg = opener.open(req).read()
with open('codeimg.png','wb') as fn:
    fn.write(codeimg)

code=raw_input(">>>")
req=urllib2.Request('https://kyfw.12306.cn/passport/captcha/captcha-check')
data={'answer':code,'login_site':'E','rand':'sjrand'}
data=urllib.urlencode(data)
req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
req.add_header('Referer','https://kyfw.12306.cn/otn/login/init')
html=opener.open(req,data=data).read()
print(html)

req=urllib2.Request('https://kyfw.12306.cn/passport/web/login')
req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
req.add_header('Referer','https://kyfw.12306.cn/otn/login/init')
data={'username':'carloszo@qq.com','password':'a12345','appid':'otn'}
data=urllib.urlencode(data)
html=opener.open(req,data=data).read()

print(html)
