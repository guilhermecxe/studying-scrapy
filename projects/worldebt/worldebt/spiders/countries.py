import scrapy

class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['https://worldpopulationreview.com']
    start_urls = ['https://worldpopulationreview.com/countries/countries-by-national-debt']

    def parse(self, response):
        rows = response.xpath('//tbody/tr')
        for r in rows:
            yield {
                'country': r.xpath('.//td[1]/a/text()').get(),
                'debt': r.xpath('.//td[2]/text()').get(),
                'population': r.xpath('.//td[3]/text()').get()
            }