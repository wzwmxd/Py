# -*- coding: utf-8 -*-
import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["ustc.edu.cn"]
    start_urls = (
        'http://www.ustc.edu.cn/',
    )

    def parse(self, response):
        pass
