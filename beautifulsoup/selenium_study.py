#!/usr/bin/python
#-*- coding:utf8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re
driver=webdriver.Chrome()
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
urls =  soup.findAll('a',href=re.compile(r'song\?id=(\d+)'))
songid=set()
for url in urls:
    songid.add(url['href'].split('?')[-1])


