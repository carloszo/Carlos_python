# -*- coding: utf-8 -*-
import scrapy


class DyttSpiderSpider(scrapy.Spider):
    name = "ifeng"
    start_urls = ["http://hb.ifeng.com"]

    def parse(self, response):
        lis = response.css('.box_01 .box_hots h3 a::attr(href)')
        for href in lis:
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url,callback=self.parse_question)



    def parse_question(self,response):
        yield{
            'title':response.css('#artical_topic::text').extract()[0],
            'body':response.css('.js_img_share_area .js_selection_area').extract()[0],
            'link': response.url,
        }
