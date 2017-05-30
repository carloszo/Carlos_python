# -*- coding: utf-8 -*-
import scrapy
from spider_peliculas.items import SpiderPeliculasItem

class CarlosSpiderSpider(scrapy.Spider):
    name = 'carlos_spider'
    allowed_domains = ['dytt8.net']
    start_urls = ['http://www.dytt8.net/html/gndy/dyzz/index.html']

    def parse(self, response):
        #filename=response.url.split('/')[-2] +'.html'
        #with open(filename,'wb') as fp:
        #fp.write(response.body)

        lis = response.xpath('/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[2]/ul/table')
        for table in lis:
            item = SpiderPeliculasItem()
            item['title'] = table.xpath('a/text()').extract()
            item['link'] = table.xpath('a/@href').extract()
            item['desc'] = table.xpath('text()')
            yield item
        print item
