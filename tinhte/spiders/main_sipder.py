# -*- coding: utf-8 -*-
import scrapy


class MainSipderSpider(scrapy.Spider):
    name = 'main_spider'
    allowed_domains = ['tinhte.vn']
    start_urls = ['http://tinhte.vn/']

    def parse(self, response):
        hot_articles = response.css('.jsx-1114360312 + .main').getall() 
        self.logger.info('================================')
        self.logger.info(hot_articles)
        self.logger.info('================================')
