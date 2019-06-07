import scrapy
from businessesforsale.items import BusinessesforsaleItem
from scrapy.utils.project import get_project_settings
from .search_criteria import SelectingSearchParametrs
from bs4 import BeautifulSoup



class BusinessesforsaleSpider(scrapy.Spider):


    name = 'businessesforsale'


    def start_requests(self):
        settings = self.setting_search_criteria()
        cookies = settings[0]
        url = settings[1]
        yield scrapy.Request(url=url, cookies=cookies, callback=self.parse)


    def setting_search_criteria(self):
        selecter = SelectingSearchParametrs()

        if get_project_settings().get('LOGIN_REQUIRED') == 1:
            login = get_project_settings().get('LOGIN')
            password = get_project_settings().get('PASSWORD')
            selecter.login(login, password)

        buisness_category = get_project_settings().get('BUSINESS_CATEGORY')
        if len(buisness_category) > 0:
            selecter.select_business_category(buisness_category)

        buisness_subcategory = get_project_settings().get('BUSINESS_SUBCATEGORY')
        if len(buisness_subcategory) > 0:
            selecter.select_business_sub_category(buisness_subcategory)

        country = get_project_settings().get('COUNTRY')
        if len(country) > 0:
            selecter.select_countries(country)

        asking_price = get_project_settings().get('ASKING_PRICE')
        if len(asking_price['max']) > 0 or len(asking_price['min']) > 0:
            selecter.select_asking_price(asking_price['min'], asking_price['max'])

        fash_flow = get_project_settings().get('FASH_FLOW')
        if len(fash_flow['max']) > 0 or len(fash_flow['min']) > 0:
           selecter.select_fash_flow(fash_flow['min'], fash_flow['max'])

        sales_revenue = get_project_settings().get('SALES_REVENUE')
        if len(sales_revenue['max']) > 0 or len(sales_revenue['min']) > 0:
           selecter.select_sales_revenue(sales_revenue['min'], sales_revenue['max'])

        cookies = selecter.browser.get_cookies()
        cur_url = selecter.browser.current_url
        selecter.browser.quit()

        return cookies, cur_url


    def parse(self, response):
        print('Start')
        url_on_page = list(set([url for url in response.xpath('//table[@class="result-table"]//a/@href').extract() if 'franchises' not in url]))
        for url in url_on_page:
            yield scrapy.Request(url, callback=self.scrape_info)
        next_page = response.xpath('//li[@class="next-link"]/a/@href').extract_first()
        if next_page:
            print(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


    def scrape_info(self, response):
        log = response.xpath('//div[@class="login-title"]/span').extract_first().strip()
        print(log)
        title = response.xpath('//h1[@itemprop="name"]/text()').extract_first().strip()
        location = response.xpath('//span[@itemprop="addressLocality"]/text()').extract_first().strip()
        asking_price = response.xpath('//dl[@class="price"]//span[@itemprop="LocalBusiness/AskingPrice"]/text()').extract_first().replace(',', '').replace('$', '').replace('£', '').replace('€', '').strip()
        sales_revenu = response.xpath('//dl[@id="revenue"]//dd[@itemprop="LocalBusiness/SalesRevenue"]//text()').extract_first().replace(',', '').replace('$', '').replace('£', '').replace('€', '').strip()
        cash_flow = response.xpath('//dl[@id="profit"]//dd[@itemprop="LocalBusiness/CashFlow"]//text()').extract_first().replace(',', '').replace('$', '').replace('£', '').replace('€', '').strip()
        try:
            currency = [i for i in ''.join(response.xpath('//div[@class="overview-details"]//text()').extract()) if i == '$' or i == '£' or i == '€'][0]
        except IndexError:
            currency = '-'
        description = ''.join([i.replace('\r\n', '').replace('\t', '').replace('  ', '').strip() for i in response.xpath('//div[@itemprop="description"]//text()').extract() if i.replace('\r\n', '').replace('\t', '').replace('  ', '') != ''])
        details = response.xpath('//div[@class="section-break collapse-section"]/div').extract()
        details = self.get_dict_for_additional_details(details)
        URL = response.url


        item = BusinessesforsaleItem()

        item['title']        = title
        item['location']     = location
        item['asking_price'] = asking_price
        item['sales_revenu'] = sales_revenu
        item['cash_flow']    = cash_flow
        item['currency']     = currency
        item['description']  = description
        item['details']      = details
        item['URL']          = URL

        yield item


    @staticmethod
    def get_dict_for_additional_details(html):
        soup = BeautifulSoup(str(html), 'lxml')
        keys = [k.text.replace(':', '').strip() for k in soup.findAll('dt')]
        values = [v.text.replace('\\r\\n', '').strip() for v in soup.findAll('dd')]
        details = dict(zip(keys, values))
        return details
