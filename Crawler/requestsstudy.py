#!/usr/bin/python
#-*- coding:utf8 -*-
#autor:Carlos
#目的：掌握requests的各种用法
import requests
r = requests.get('https://github.com/timeline.json')
#获取响应内容
#print("response text:"+r.text)
#获取响应编码
#print("修改前的编码:"+r.encoding)
#编码也可以被改变
r.encoding='gb13080'
#print("修改后的编码:"+r.encoding)
#print(r.content)
#jason响应
#print('jason response:')
#print(r.json())
#jason响应失败会抛出异常，比如401。尝试访问 r.json() 将会抛出 ValueError: No JSON object could be decoded 异常
#成功调用r.jason()并非成功响应，有的服务器会在失败的响应中包含一个 JSON 对象（比如 HTTP 500 的错误细节）
#status_code可以反馈响应信息，201
#print('status code:')
#print(r.status_code)
#print(r)
#传递URL参数,参数包装在字典中。
payload={'key1':'value1','key2':'value2'}
r=requests.get('http://httpbin.org/get',params=payload)
#print r.url
#参数中可以传入list
payload={'key1':'value1','key2':['value2','value3']}
r=requests.get('http://httpbin.org/get',params=payload)
#print r.url
#定制请求头
url='https://api.github.com/some/endpoint'
headers={'user-agent':'my-app/0.0.1'}
r = requests.get(url,headers)
#post请求
payload={'key1':'value1','key2':'value2'}
r=requests.post('http://httpbin.org/post',payload)
print(r.text)