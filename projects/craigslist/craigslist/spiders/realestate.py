import scrapy
from craigslist.items import CraigslistItem

class RealestateSpider(scrapy.Spider):
    name = 'realestate'
    allowed_domains = ['newyork.craigslist.org/d/real-estate/search/rea']
    start_urls = ['http://newyork.craigslist.org/d/real-estate/search/rea/']

    def parse(self, response):
        allAds = response.css(".result-info")

        for ad in allAds:
            date = ad.css("time::text").get()
            title =  ad.css("a.result-title.hdrlnk::text").get()
            price = ad.css("span.result-price::text").get()
            link = ad.css("a::attr(href)").get()

            items = CraigslistItem()
            items['date'] = date
            items['title'] = title
            items['price'] = price
            items['link'] = link

            yield items

# Eu acho que o site está bloqueando as requisições