import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AllBooksSpider(CrawlSpider): # CrawlSpider é usado para definirmos rules/regras
    name = 'all_books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    # Abaixo estamos definindo regras que dizem que os links encontrados no caminho //img[@class='thumbnail']/parent::a
    # devem ser parseados pelo método parse_item e em seguida acessados também por causa do argumento follow=True.
    # Já a segunda regra define que os links encontrados no caminho ".next a" devem ser acessados mas não
    # parseados por nenhum método.
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//img[@class='thumbnail']/parent::a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_css=".next a"), follow=True),
    )

    def parse_item(self, response):
        yield {
            'title': response.css('h1::text').get(),
            'price': response.css('.price_color::text').get(),
            'availability': ' '.join(response.css('.product_main > .availability::text').getall()).strip(),
        }
