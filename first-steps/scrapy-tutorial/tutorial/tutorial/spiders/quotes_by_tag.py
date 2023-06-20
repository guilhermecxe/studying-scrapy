import scrapy


class QuotesSpider(scrapy.Spider):
    name = "tag"

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

# É possível passar argumentos para o spider por meio da linha de comando usando a flag -a
# e esse argumento é passado para o __init__ do Spider.
# Exemplo:
# scrapy crawl tag -a tag=humor
# Com isso iremos obter apenas os quotes da tag humor