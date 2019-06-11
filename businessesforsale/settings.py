# -*- coding: utf-8 -*-


LOGIN_REQUIRED = 1
LOGIN = 'login'
PASSWORD = 'password'

COUNTRY = ''

BUSINESS_CATEGORY = 'Food'
BUSINESS_SUBCATEGORY = ''

# Agriculture >> [Agricultural Supplies, Farms, Misc. Agriculture, Ranches]
# Engineering >> [Consultants, Electrical Services, Manufacturing. Mechanical Services, Other Technical Services]
# Food >> [Cafes, Catering Services, Food & Drink Distributors. Food & Drink Manufacturers, Food & Drink Wholesalers, Restaurants, Retailers]
# Franchise Resales >> [Agricultural Supplies, Farms, Misc. Agriculture, Ranches]
# Leisure >> [Entertainment & Fun, Hotels & Motels, Pubs, Bars & Nightclubs, Recreation]
# Manufacturing >> [Clothing & Footwear Manufacturers, Energy Related, Furniture & Wood, Machinery & Metal, Mining, Other, Transportation Related]
# Real Estate >> [Cafes, Farms, Gas/Petrol Service Stations, Hotels & Motels, Industrial Warehouse / Distribution, Investment, Land, etc.]
# Retail >> [Clothing, Food & Drink, General, Health & Beauty, Home & Garden, TV, Audio, Video & Photographic, Vehicles]
# Services >> [Advertising & Marketing, Construction, Education, Financial, General, Health Care, Hire, House & Garden, Maintenance, etc.]
# Tech & Media >> [Advertising & Marketing, Information Technology, Internet, Media]
# Wholesale & Distribution >> [Distribution, Wholesale]

### Asking Price ###
ASKING_PRICE = {'min': '', 'max': '1'}

### Fash Flow ###
FASH_FLOW = {'min': '', 'max': '1'}

### Sales Revenue ###
SALES_REVENUE = {'min': '', 'max': ''}

DOWNLOAD_DELAY = 1

CONNECTION_STRING = "sqlite:///businessesforsale.db"

ITEM_PIPELINES = {
    'businessesforsale.pipelines.BusinessesforsalePipeline': 300,
}


DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
}


BOT_NAME = 'businessesforsale'

SPIDER_MODULES = ['businessesforsale.spiders']
NEWSPIDER_MODULE = 'businessesforsale.spiders'


LOG_LEVEL = 'ERROR'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
