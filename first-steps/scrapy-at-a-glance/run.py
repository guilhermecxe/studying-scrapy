import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'author': quote.xpath('span/small/text()').get(),
                'text': quote.css('span.text::text').get(),
            }
        
        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

# Para cada url em start_urls, o método `parse` será chamado e o conteúdo da página
# será passado para o método por meio de `response`. Dentro de `parse` cada quote
# da página é obtido usando seletores css e xpath e, ao final, `parse` é novamente chamado,
# mas para obter o conteúdo da próxima página, se existir. Então, em follow, self.parse
# funciona como um callback do resultado da página.

# Para executar este código:
# $ scrapy runspider run.py -o quotes.jl
# Isso criará o arquivo quotes.jl com todas as quotes resultantes.

# Eu poderia trocar "quotes.jl" por "quotes.json", "quotes.csv" ou outros formatos suportados
# que o Spider salvaria os dados no formato desejado.
# Um arquivo .jl é parecido com um arquivo .json, mas com uma (ou algumas) diferença.
# Para mais detalhes sobre isso:
# - https://stackoverflow.com/questions/52924300/what-is-the-difference-between-a-json-file-and-jl-file
# - https://www.reddit.com/r/scrapy/comments/cd2h65/how_to_tell_scrapy_that_when_you_yield_to_write/