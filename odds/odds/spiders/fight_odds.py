# -*- coding: utf-8 -*-
import scrapy


class FightOddsSpider(scrapy.Spider):
    name = 'fight_odds'
    allowed_domains = ['https://www.bestfightodds.com']
    start_urls = ['https://www.bestfightodds.com/events/ufc-231-holloway-vs-ortega-1584/']

    def parse(self, response):
        pass
