# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .items import WebcrawlerItem
from core.models import Reviews
class WebcrawlerPipeline(object):
    
    def process_item(self, item, rw):
        # b = Reviews(PlaintextReviews = item, Review = None, Final = None)
        # b.save()
        # print("FUCK")
        print("Pipeline: " + item[rw][0])
        return item
