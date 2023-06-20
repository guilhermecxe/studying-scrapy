import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from urllib.parse import urlparse, parse_qs
from datetime import datetime, timedelta
import pytz

from g1.items import G1Item

def process_url(url):
    return parse_qs(urlparse(url).query)['u'][0]

class SearchSpider(scrapy.Spider):
    name = 'search'
    allowed_domains = ['g1.globo.com']
    SEARCH_URL_TEMPLATE = "https://g1.globo.com/busca/?q={}&page={}&order=recent&species=not%C3%ADcias&from={}T00%3A00%3A00-0300&to={}T23%3A59%3A59-0300&ajax=1"
    Q = 'noroeste'
    START_DATE = datetime(2022, 2, 1)
    END_DATE = datetime(2022, 2, 28)

    def parse(self, response):
        date = response.request.meta['date']
        results = response.xpath("//div[contains(@class, 'product-color')]/parent::a")
        
        if not results:
            next_date = date + timedelta(days=1)
            if next_date <= SearchSpider.END_DATE:
                page = 1
                next_url = SearchSpider.SEARCH_URL_TEMPLATE.format(SearchSpider.Q, page, next_date.strftime(r'%Y-%m-%d'), next_date.strftime(r'%Y-%m-%d'))
                yield scrapy.Request(next_url, meta={'date': next_date, 'page': page})
            return
        for result in results:
            url = process_url(result.xpath('.//@href').get())
            if '/go/' in url:
                yield response.follow(url, callback=self.parse_news)
        
        next_page = response.request.meta['page'] + 1
        next_page_url = SearchSpider.SEARCH_URL_TEMPLATE.format(SearchSpider.Q, next_page, date.strftime(r'%Y-%m-%d'), date.strftime(r'%Y-%m-%d'))
        yield scrapy.Request(next_page_url, meta={'date': date, 'page': next_page})

    def start_requests(self):
        page = 1
        date = SearchSpider.START_DATE
        url = SearchSpider.SEARCH_URL_TEMPLATE.format(SearchSpider.Q, page, date.strftime(r'%Y-%m-%d'), date.strftime(r'%Y-%m-%d'))
        yield scrapy.Request(url, meta={'date': date, 'page': page})

    def parse_news(self, response):
        publication_date = datetime.strptime(response.css('time::text').get().strip(), r'%d/%m/%Y %Hh%M').strftime(r'%d-%m-%Y')
        last_update = datetime.strptime(response.css('time')[1].attrib['datetime'].strip(), r'%Y-%m-%dT%H:%M:%S.%fZ').strftime(r'%d-%m-%Y')
        REGION = 'America/Sao_Paulo'

        yield {
            'url': response.url,
            'title': response.css('.content-head__title::text').get().strip(),
            'subtitle': response.css("h2[itemprop='alternativeHeadline']::text").get().strip(),
            'publication_date': publication_date,
            'last_update': last_update,
            'acquisition_date': datetime.now(pytz.timezone(REGION)).strftime('%d-%m-%Y'),
            'article': ''.join(response.css("article[itemprop='articleBody'] *::text").getall()).strip(),
        }