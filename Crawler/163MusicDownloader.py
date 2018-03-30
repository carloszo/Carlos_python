#!/usr/bin/python
#-*- coding:utf8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re
import urllib
import os
driver=webdriver.Firefox()
driver.get('http://music.163.com/#/discover/toplist')
driver.switch_to.frame('contentFrame')
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
driver.quit()
soup = bs(html,'lxml')
contents =  soup.findAll('div',{'class':'ttc'})
data=[]
for content in contents:
    dataunit={}
    id = content.find('a')['href'].split('?')[-1]
    title = content.find('b')['title']
    dataunit['id']=id
    dataunit['title']=title
    data.append(dataunit)

def music_download(filename,downloadlink):
    path= '/Users/carlos/documents/music/' + filename
    if(os.path.exists('/Users/carlos/documents/music')==False):
        os.makedirs('/Users/carlos/documents/music/')
    elif(os.path.isfile(path)==False):
            urllib.urlretrieve(downloadlink, '/Users/carlos/documents/music/' + filename)
    else:
        return

for content in data:
    title=content['title']
    id=content['id']
    downloadlink = 'http://music.163.com/song/media/outer/url?%s.mp3' % id
    filename=title+'.'+'.mp3'
    print(downloadlink)
    try:
        music_download(filename,downloadlink)
        print(title+' downloaded successfully!!')
    except:
        print('download failed!')
