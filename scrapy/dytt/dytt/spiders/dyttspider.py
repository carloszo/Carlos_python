# -*- coding: utf-8 -*-
import scrapy
from dytt.items import DyttItem

from scrapy.crawler import CrawlerProcess
from scrapy.conf import settings



class DyttspiderSpider(scrapy.Spider):
    name = 'dyttspider'
    allowed_domains = ['dytt8.net']
    start_urls = ['http://www.ygdy8.net/html/gndy/dyzz/index.html']
    

    def parse(self,response):
        list =  response.xpath('//b/a/@href').extract()
        for url in list:
            fullurl = response.urljoin(url)
            yield scrapy.Request(url=fullurl,callback=self.question,dont_filter=True)
                
    def question(self,response):
        item = DyttItem()
        item['title'] = response.xpath('//h1/font/text()').extract()[0]
        item['url'] = response.xpath('//td[@bgcolor="#fdfddf"]/a/@href').extract()[0]
        yield item

process = CrawlerProcess(settings)
process.crawl(DyttspiderSpider)
process.start()
