#!/usr/bin/python
#-*- coding:utf8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re
import time
driver=webdriver.Chrome()
driver.get('http://yuancheng.xunlei.com/login.html')
driver.switch_to.frame('loginIframe')
driver.find_element_by_id('al_u').click()
driver.find_element_by_id('al_u').clear()
driver.find_element_by_id('al_u').send_keys('carloszo@qq.com')
driver.find_element_by_id('al_p').click()
driver.find_element_by_id('al_p').clear()
driver.find_element_by_id("al_p").send_keys('a12345')
time.sleep(5)
driver.find_element_by_id("al_submit").click()
# print driver.page_source
driver.find_element_by_css_selector('site_new').click()
# print driver.page_source
# driver = webdriver.Chrome()
# driver.get(url)
# driver.find_element_by_id('login-email').click()
# driver.find_element_by_id('login-email').clear()
# driver.find_element_by_id('login-email').send_keys('carlos@lieneng.com.cn')
# driver.find_element_by_id('login-password').click()
# driver.find_element_by_id('login-password').clear()
# driver.find_element_by_id('login-password').send_keys('Anniivan0202')
# driver.find_element_by_id('login-submit').click()
# driver.get('http://www.linkedin.com/in/michael-xu-6930991/')
# print driver.page_source
# driver.switch_to.frame('contentFrame')
# html = driver.page_source
#driver.find_element_by_xpath("//span[@class='txt']")
#print driver.page_source
#browser.find_element_by_xpath(u"//img[@alt='强化学习 (Reinforcement Learning)']").click()
#browser.find_element_by_link_text("About").click()
#driver.get("http://music.163.com/#/discover/toplist")
# driver.find_element_by_xpath("//div[@id='g-topbar']/div/div/ul/li[2]/span/a/em").click()
# driver.find_element_by_xpath("//div[@id='g-topbar']/div/div/ul/li[3]/span/a/em").click()
# driver.find_element_by_css_selector("in_txt").click()
# html=driver.page_source
# print html
# driver.close()
# driver.quit()
# soup = bs(html,'lxml')
# urls =  soup.findAll('a',href=re.compile(r'song\?id=(\d+)'))
# songid=set()
# for url in urls:
#     songid.add(url['href'].split('?')[-1])


