# -*- coding: utf-8 -*-
import sys
import os
import scrapy
dirname = os.path.dirname(__file__)
sys.path.append(os.path.dirname(dirname))
from items import TinhteItem, AuthorItem

class ArticleSpider(scrapy.Spider):
    name = 'article_spider'
    allowed_domains = ['tinhte.vn']
    start_urls = ['http://tinhte.vn/']

    def parse(self, response):
        articles = response.css('.section .fst .jsx-187331041 ol li article')
        for article in articles:
            article_link = article.css('a::attr(href)').get()
            # self.logger.info(article.css('a::attr(href)'))
            # self.logger.info('---------------------------')
            yield response.follow(article_link, callback=self.parse_article)
        
            # item = TinhteItem()
            # item['title'] = article.css('.title::text').get()
            # item['img'] = article.css('.img img::attr(src)').get()
            # item['excerpt'] = article.css('.excerpt::text').get()
            # item['author'] = AuthorItem(name='aaa', phone='111')
            # yield item
    
    def parse_article(self, response):
        def extract_with_css(query):
            self.logger.info(response.css('.bdImage_cover .thread_title::text').get())
            self.logger.info(response.request)
            self.logger.info('--------------------------')
            return response.css(query).get(default='').strip()
        
        item = TinhteItem()
        item['title'] = extract_with_css('.bdImage_cover .thread_title::text')
        # self.logger.info('---------------------------')
        # self.logger.info(item['title'] )
        # self.logger.info('---------------------------')
        yield item
        
            
        # self.logger.info('---------------------------')
        # self.logger.info(img)
        # self.logger.info('---------------------------')

        
