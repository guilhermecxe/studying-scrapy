# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class G1Item(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    subtitle = scrapy.Field()
    publication_date = scrapy.Field()
    last_update = scrapy.Field()
    acquisition_date = scrapy.Field()
    article = scrapy.Field()
