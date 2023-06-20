import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes" # Este nome para o spider deve ser único no projeto

    def start_requests(self):
        """Neste método estamos explicitando as urls a serem usadas e
        o callback da resposta da requisição das páginas,
        que é o método parse."""
        urls = [
            'http://quotes.toscrape.com/page/1/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """Aqui estamos salvando o conteúdo da página em um arquivo .html."""
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        # Obtendo o conteúdo de cada quote. Isso não é salvo, mas é exibido
        # no terminal ao rodar o spider
        for quote in response.css('.quote'):
            yield {
                'quote': quote.css('.text::text').get(),
                'author': quote.css('.author::text').get(),
                'tag': quote.css('.tags .tag::text').getall()
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

# Por padrão não precisávamos ter definido o método start_requests ou
# explicitado parse como o callback da url. Como feito em scrapy-at-a-glance,
# poderíamos apenas ter definido as urls em uma lista chamada start_urls.
# Com isso scrapy.Spider faria o resto do trabalho, inclusive chamando parse
# para cada url.

# Quando um método callback, como parse, coleta (yield) um Request o Scrapy
# vai "agendar" aquele request e executar o callback dele quando receber uma
# resposta.

# Porém, ao invés de termos usado urljoin e Request poderíamos apenas ter usado:
# yield response.follow(next_page, callback=self.parse)
# Já que o método follow aceita url relativas e isso iria abstrair a criação
# explícita de um Request

# Em .follow também é aceito um seletor que aponte para uma tag <a>,
# com isso o método já faz a extração da url:
# for a in response.css('ul.pager a'):
#   yield response.follow(a, callback=self.parse)

# Agendando a requisição de várias urls:
# anchors = response.css('ul.pager a')
# yield from response.follow_all(anchors, callback=self.parse)
# Ou
# yield from response.follow_all(css='ul.pager a', callback=self.parse)
