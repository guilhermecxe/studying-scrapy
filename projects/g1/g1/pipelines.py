# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime
import jsonlines

from .spiders.search import SearchSpider

class DatesToStrPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        adapter['publication_date'] = datetime.strptime(adapter['publication_date'], r'%Y-%m-%dT%H:%M:%S.%fZ').strftime(r'%d-%m-%Y')
        adapter['last_update'] = datetime.strptime(adapter['last_update'], r'%Y-%m-%dT%H:%M:%S.%fZ').strftime(r'%d-%m-%Y')
        return item