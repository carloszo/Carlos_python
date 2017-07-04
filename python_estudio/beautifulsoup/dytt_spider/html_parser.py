#!/usr/bin/python
#-*-coding:utf-8 -*-
from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):
    
    def _get_new_urls(self,page_url,soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r'/html/\w{4}/\w{4}/\d{8}/\d{5}\.html'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self,page_url,soup):
        res_data = {}
        #url
        res_data['url'] =  page_url
        
        #<h1><font color=#07519a>2017年动画《蓝精灵：寻找神秘村》国英双语.BD中英双字幕</font></h1>
        title_node = soup.find('h1').find('font')
        res_data['title'] = title_node.get_text()

        #<div id="Zoom">
        #summary_node =soup.find('div',id='Zoom')
        #res_data['summary'] = summary_node.get_text()

        #<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="ftp://d:d@dygodj8.com:12311/[电影天堂www.dy2018.com]冈仁波齐DVD中字.mkv">
        link_node = soup.find('td',bgcolor='#fdfddf').find('a')
        res_data['download_link'] = link_node['href']

        return res_data

    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data


