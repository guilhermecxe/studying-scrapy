import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from urllib.parse import urlparse, parse_qs
from datetime import datetime

def process_url(url):
    return parse_qs(urlparse(url).query)['u'][0]

class SearchSpider(CrawlSpider):
    name = 'search'
    allowed_domains = ['g1.globo.com']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[contains(@class, 'product-color')]/parent::a", process_value=process_url), callback='parse_news'),
    )

    def start_requests(self):
        yield scrapy.Request('https://g1.globo.com/busca/?q=crime+organizado&ps=on&order=recent&species=not%C3%ADcias&from=2023-06-17T00%3A00%3A00-0300&to=2023-06-17T23%3A59%3A59-0300&ajax=1')

    # def parse(self, response):
    #     pass

    def parse_news(self, response):
        publication_date = datetime.strptime(response.css('time::text').get().strip(), r'%d/%m/%Y %Hh%M').strftime(r'%d-%m-%Y')
        last_update = datetime.strptime(response.css('time')[1].attrib['datetime'].strip(), r'%Y-%m-%dT%H:%M:%S.%fZ').strftime(r'%d-%m-%Y')

        article_headers_selector = "article[itemprop='articleBody'] h2"
        article_paragraphs_selector = "div[data-block-type='unstyled'] p.content-text__container"
        article_quotes_selector = None
        yield {
            'url': response.url,
            'title': response.css('.content-head__title::text').get().strip(),
            'subtitle': response.css("h2[itemprop='alternativeHeadline']::text").get().strip(),
            'publication_date': publication_date,
            'last_update': last_update,
            'article': ''.join(response.css('p.content-text__container *::text').getall()),
        }