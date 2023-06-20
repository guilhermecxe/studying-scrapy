import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'author'

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        author_page_links = response.css('.author + a')
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.css('li.next a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()
            # Como response retorna uma lista, se a lista estiver vazia no momento do .get
            # o valor retornado é o de default

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }

# Este é um spider para extrair dados dos autores e ir passando pelas páginas

# Por padrão, não precisamos nos preocupar por visitar o(a) mesmo(a) autor(a) várias
# vezes, já que o Scrapy faz um filtro automática em que ele remove requests duplicados.
# Isso pode ser configurado pela setting DUPEFILTER_CLASS.