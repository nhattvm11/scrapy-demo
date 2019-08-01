# -*- coding: utf-8 -*-
import scrapy


class HotArticlesSpiderSpider(scrapy.Spider):
    name = 'hot_articles_spider'
    allowed_domains = ['tinhte.vn']
    start_urls = ['http://tinhte.vn/']

    def parse(self, response):
        # self.logger.info('================================')
        # # self.logger.info(response.css('.jsx-1114360312 + .main ol').getall())
        # self.logger.info('================================')
        items = response.css('.jsx-1114360312 + .main ol')
        for item in items:
            # self.logger.info('================================')
            # self.logger.info(item.css('ol').get())
            ol = item.css('ol')
            for li in ol:
                self.logger.info(li)
            # self.logger.info('================================')
        # filename = 'tinhte.html'
        # with open(filename, 'wb') as f:
        #     f.write(a)
        # self.log('Saved file %s' % filename)
        # hot_articles = response.css('.jsx-1114360312 + .main').getall()
        # for article in hot_articles:
        #     pass
