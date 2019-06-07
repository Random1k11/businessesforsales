# -*- coding: utf-8 -*-


LOGIN_REQUIRED = 1
LOGIN = 'random1k11@yandex.ru'
PASSWORD = 'dima1994'

COUNTRY = ''

BUSINESS_CATEGORY = 'Engineering'
BUSINESS_SUBCATEGORY = ''

# Agriculture >> BUSINESS_SUBCATEGORY [Agricultural Supplies, Farms, Misc. Agriculture, Ranches]
# Engineering >> BUSINESS_SUBCATEGORY [Consultants, Electrical Services, Manufacturing. Mechanical Services, Other Technical Services]
# Food >> BUSINESS_SUBCATEGORY [Cafes, Catering Services, Food & Drink Distributors. Food & Drink Manufacturers, Food & Drink Wholesalers, Restaurants, Retailers]
# Franchise Resales >> BUSINESS_SUBCATEGORY [Agricultural Supplies, Farms, Misc. Agriculture, Ranches]
# Leisure
# Manufacturing
# Real Estate
# Retail
# Services
# Tech & Media
# Wholesale & Distribution

### Asking Price ###
ASKING_PRICE = {'min': '100', 'max': '200'}

### Fash Flow ###
FASH_FLOW = {'min': '300', 'max': '500'}

### Sales Revenue ###
SALES_REVENUE = {'min': '', 'max': ''}



BOT_NAME = 'businessesforsale'

SPIDER_MODULES = ['businessesforsale.spiders']
NEWSPIDER_MODULE = 'businessesforsale.spiders'


LOG_LEVEL = 'INFO'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
