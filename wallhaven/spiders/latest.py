# -*- coding: utf-8 -*-
import scrapy


class LatestSpider(scrapy.Spider):
    name = 'latest'
    allowed_domains = ['alpha.wallhaven.cc']
    start_urls = ['http://alpha.wallhaven.cc/']

    def parse(self, response):
        pass
