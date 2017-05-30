# -*- coding: utf-8 -*-
import scrapy


class DyttSpiderSpider(scrapy.Spider):
    name = "ifeng"
    start_urls = ["http://hb.ifeng.com"]

    def parse(self, response):
        lis = response.css('.box_hots h2 a::attr(href)')
        for href in lis:
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url,callback=self.parse_question)



    def parse_question(self,response):
        yield{
            'title':response.css('.artical h1::text').extract()[0],
            'link': response.url,
        }
