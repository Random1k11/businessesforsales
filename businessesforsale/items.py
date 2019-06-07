# -*- coding: utf-8 -*-
import scrapy


class BusinessesforsaleItem(scrapy.Item):

    title        = scrapy.Field()
    location     = scrapy.Field()
    asking_price = scrapy.Field()
    sales_revenu = scrapy.Field()
    cash_flow    = scrapy.Field()
    currency     = scrapy.Field()
    description  = scrapy.Field()
    details      = scrapy.Field()
    URL          = scrapy.Field()
