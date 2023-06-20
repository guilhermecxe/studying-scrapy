from requests import head
import scrapy
from ..settings import DEFAULT_REQUEST_HEADERS

class PneusSpider(scrapy.Spider):
    name = 'pneus'
    allowed_domains = ['www.casasbahia.com.br']

    def start_requests(self):
        yield scrapy.Request('http://www.casasbahia.com.br/pneu-aro-14/b', headers=DEFAULT_REQUEST_HEADERS)

    def parse(self, response):
        for product in response.css('.KTGxe'): ## Esse atributo CSS pode mudar a qualquer momento
            print('p:', product)
            yield {
                'title': product.css('::text').get(),
            }
