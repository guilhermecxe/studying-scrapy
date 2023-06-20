import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

"""
Este é um spider que entra na primeira página dos filmes com as melhores notas do IMDB, entra nos filmes
listados, lê os dados desses filmes e vai para a próxima página do ranking.
"""

# Para que pudessemos especificar o user-agent dentro do spider foi necessário que substituíssimos start_urls
# pelo método start_requests e especificássemos o user-agent dentro desse método. Mas isso só altera
# as headers da url inicial

class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['web.archive.org']

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"

    def start_requests(self):
        yield scrapy.Request(url='http://web.archive.org/web/20200715000935/https://www.imdb.com/search/title/?groups=top_250&sort=user_rating',
                             headers={
                                'User-Agent': self.user_agent
                             })

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"), callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"), follow=True, process_request='set_user_agent')
    )
    # O callback de Rule nunca deve ser "parse".
    # O argumento follow define se queremos ou não requisita a url obtida
    # O argumento allow de LinkExtractor é usado para informarmos, com uma expressão regular,
    # os links que queremos obter. Essa classe tem também o parâmetro deny que também usa
    # expressão regular.
    # restrict_xpaths é um parâmetro de LinkExtractor que podemos usar para especificar os links
    # que queremos usando XPath. Por exemplo: '//a[@class="active"]' define que queremos as urls
    # que estejam em elementos com a classe "active" (Não foi necessário usar "/@href").
    # restrict_css funciona como o parâmetro anterior. Mas para CSS.

    # A segunda Rule busca pela url que acessa a próxima página, por isso ela é definida depois da Rule
    # que entra nos filmes. Então todos os filmes de uma página são processados e só então a próxima página
    # é obtida.

    # Com o process_request especificamos qual deve ser a função chamada para lidar com o request da url.

    def set_user_agent(self, request, spider):
        """Método que lida com o request a ser feito adicionando um user-agent às headers."""
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            'title': response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            'year': response.xpath("//span[@id='titleYear']/a/text()").get(),
            'duration': response.xpath("normalize-space((//time)[1]/text())").get(),
            'genre': response.xpath("//div[@class='subtext']/a[1]/text()").get(),
            'rating': response.xpath("//span[@itemprop='ratingValue']/text()").get(),
            'movie_rating': response.url,
            'user-agent': response.request.headers['User-Agent']
        }