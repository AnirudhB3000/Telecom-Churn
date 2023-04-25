from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from WebCrawler.WebCrawler.spiders.reviews_spider import ReviewSpider






def result():
      process = CrawlerProcess(get_project_settings())
      process.crawl(ReviewSpider)
      process.start()

