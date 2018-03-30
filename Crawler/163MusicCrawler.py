#!/usr/bin/python
#-*- coding:utf8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re
import urllib
import os
#autor:carlos
#介绍：
# 利用selenium获取网易云音乐toplist页面中frame框架的源代码
# 利用BeautifulSoup获取音乐id、标题
# 拼接网易云音乐真实下载链接（'http://music.163.com/song/media/outer/url?%s.mp3' % id）
# 利用urllib.urlretrieve()下载音乐文件

#利用selenium打开浏览器
driver=webdriver.Chrome()
#打开链接
driver.get('http://music.163.com/#/discover/toplist')
#跳转到contentFrame框架
driver.switch_to.frame('contentFrame')
#获取contentFrame框架源代码
html = driver.page_source
#driver.find_element_by_xpath("//span[@class='txt']")
#print driver.page_source
#browser.find_element_by_xpath(u"//img[@alt='强化学习 (Reinforcement Learning)']").click()
#browser.find_element_by_link_text("About").click()
#driver.get("http://music.163.com/#/discover/toplist")
# driver.find_element_by_xpath("//div[@id='g-topbar']/div/div/ul/li[2]/span/a/em").click()
# driver.find_element_by_xpath("//div[@id='g-topbar']/div/div/ul/li[3]/span/a/em").click()
# driver.find_element_by_css_selector("em").click()
# html=driver.page_source
# print html
# driver.close()
#退出浏览器
driver.quit()
soup = bs(html,'lxml')
#将音乐内容信息保存到contents中
contents =  soup.findAll('div',{'class':'ttc'})
data=[]
for content in contents:
    dataunit={}
    #获取链接中的id部分 /song?id=525238891
    id = content.find('a')['href'].split('?')[-1]
    title = content.find('b')['title']
    dataunit['id']=id
    dataunit['title']=title
    #将音乐id和标题保存在字典dataunit中，然后存放到list。
    data.append(dataunit)

#利用urllib.urlretrieve(）下载图片
def music_download(filename,downloadlink):
    path= '/Users/apple/documents/music/' + filename
    if(os.path.exists('/Users/apple/documents/music')==False):
        os.makedirs('/Users/apple/documents/music/')
    elif(os.path.isfile(path)==False):
            urllib.urlretrieve(downloadlink, '/Users/apple/documents/music/' + filename)
    else:
        return
#循环输出list中的内容[{'title':'','id':''}]
for content in data:
    #
    title=content['title']
    id=content['id']
    #利用id拼接真实下载链接
    downloadlink = 'http://music.163.com/song/media/outer/url?%s.mp3' % id
    filename=title+'.'+'.mp3'

    try:
        music_download(filename,downloadlink)
        print(title+' downloaded successfully!!')
    except:
        print('download failed!')