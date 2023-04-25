from scrapy.exporters import BaseItemExporter
from myapp.models import MyModel

class DjangoPipeline(BaseItemExporter):
    def process_item(self, item, spider):
        print("Pipeline: " + item['rw'][0])
        return item
