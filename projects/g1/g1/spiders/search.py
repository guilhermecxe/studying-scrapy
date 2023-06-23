import scrapy
from scrapy.linkextractors import LinkExtractor
from itemloaders.processors import Join
from scrapy.spiders import CrawlSpider, Rule
from urllib.parse import urlparse, parse_qs
from datetime import datetime, timedelta
import pytz
import jsonlines

from g1.items import G1Item
from g1.itemsloaders import NewsLoader

def process_url(url):
    return parse_qs(urlparse(url).query)['u'][0]

class SearchSpider(scrapy.Spider):
    name = 'search'
    allowed_domains = ['g1.globo.com']

    SEARCH_URL_TEMPLATE = "https://g1.globo.com/busca/?q={}&page={}&order=recent&species=not%C3%ADcias&from={}T00%3A00%3A00-0300&to={}T23%3A59%3A59-0300&ajax=1"
    Q = 'noroeste'
    START_DATE = datetime(2022, 2, 1)
    END_DATE = datetime(2022, 12, 31)
    SAVE_ON = 'file.jl'

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)

        # Obtendo as urls já salvas
        self.urls_seen = []
        with jsonlines.open(SearchSpider.SAVE_ON, 'r') as reader:
            for line in reader:
                self.urls_seen.append(line['url'])

    def start_requests(self):
        page = 1
        date = SearchSpider.START_DATE
        url = SearchSpider.SEARCH_URL_TEMPLATE.format(SearchSpider.Q, page, date.strftime(r'%Y-%m-%d'), date.strftime(r'%Y-%m-%d'))
        yield scrapy.Request(url, meta={'date': date, 'page': page})

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
            if ('/go/' in url) and (not url in self.urls_seen):
                yield response.follow(url, callback=self.parse_news)
        
        next_page = response.request.meta['page'] + 1
        next_page_url = SearchSpider.SEARCH_URL_TEMPLATE.format(SearchSpider.Q, next_page, date.strftime(r'%Y-%m-%d'), date.strftime(r'%Y-%m-%d'))
        yield scrapy.Request(next_page_url, meta={'date': date, 'page': next_page})

    def parse_news(self, response):
        REGION = 'America/Sao_Paulo'

        news_item = NewsLoader(item=G1Item(), selector=response)
        news_item.add_value('url', response.url)
        news_item.add_css('title', '.content-head__title::text')
        news_item.add_css('subtitle', "h2[itemprop='alternativeHeadline']::text")
        news_item.add_css('publication_date', 'time[itemprop="datePublished"]::attr(datetime)')
        news_item.add_css('last_update', 'time[itemprop="dateModified"]::attr(datetime)')
        news_item.add_value('acquisition_date', datetime.now(pytz.timezone(REGION)).strftime('%d-%m-%Y'))
        news_item.add_css('article', 'article[itemprop="articleBody"] *::text')

        self.urls_seen.append(response.url)

        yield news_item.load_item()