# -*- coding: utf-8 -*-
import scrapy


class HotArticlesSpiderSpider(scrapy.Spider):
    name = 'hot_articles_spider'
    allowed_domains = ['tinhte.vn']
    start_urls = ['http://tinhte.vn/']

    def parse(self, response):
        # <ol class="jsx-3139588515"><li class="jsx-3139588515">...</ol>
        articles = response.css('ol .jsx-3139588515')
        for article in articles:
            yield {
                'link': article.css('a::attr(href)').get(),
                'title': article.css('h3 .title::text').get(),
                'author': article.css('.info .author::text').get(),
                'since': article.css('.info .since span::text').get(),
            }
