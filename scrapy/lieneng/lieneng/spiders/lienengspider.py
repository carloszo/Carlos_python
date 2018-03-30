# -*- coding: utf-8 -*-
import scrapy
from lieneng.items import LienengItem

class LienengspiderSpider(scrapy.Spider):
    name = 'lienengspider'
    allowed_domains = ['lieneng.com.cn']
    start_urls = ['http://lieneng.com.cn/news']

    '''def parse(self, response):

        list = response.xpath('//div[@class="news_list"]/ul/li')
        items=[]
        for content in list:
            item = LienengItem()
            item['title'] = response.xpath('//div[@class="news_list_title"]/a/text()').extract()
            items.append(item)
        return items'''
    def parse(self,response):
        list = response.xpath('//div[@class="news_list_title"]/a/@href').extract()
        for url in list:
            fullurl = response.urljoin(url)
            yield scrapy.Request(fullurl,callback=self.parse_question)

    def parse_question(self,response):
        item = LienengItem()
        #item['title'] = response.xpath('//div[@class="article_content_right_title"]/text()').extract()
        item['title'] = "11561561"
        yield item
