from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from businessesforsale.spiders.businessesforsale import BusinessesforsaleSpider
 
 
process = CrawlerProcess(get_project_settings())
process.crawl(BusinessesforsaleSpider)
process.start()
