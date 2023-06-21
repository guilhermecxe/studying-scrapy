from itemloaders.processors import TakeFirst, MapCompose, Join
from scrapy.loader import ItemLoader
from datetime import datetime

class NewsLoader(ItemLoader):
    default_output_processor = TakeFirst()
    title_in = MapCompose(str.strip)
    subtitle_in = MapCompose(str.strip)

    def process_article_in(self, values):
        return ' '.join(values).strip()
    
    article_in = process_article_in