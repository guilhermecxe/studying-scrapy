import scrapy
import logging # Estudar sobre essa biblioteca
from scrapy.shell import inspect_response
from scrapy.utils.response import open_in_browser

class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # open_in_browser(response)
        # Com a função open_in_browser conseguimos visualizar no navegador a página que foi retornada quando
        # o request foi feito. A página será aberta quando executarmos o spider normalmente.

        countries = response.xpath('//td/a')
        for country in countries:
            name = country.xpath('.//text()').get()
            link = country.xpath('.//@href').get()

            yield response.follow(link, callback=self.parse_country, meta={'country_name': name})
            # O parâmetro meta é a forma de passar informação para o parse que lida com o respectivo request

            # yield response.follow(link) # Isso faz exatamente a mesma coisa das duas linhas comentadas abaixo
            # absolute_url = response.urljoin(link)
            # yield scrapy.Request(url=absolute_url)

    def parse_country(self, response):
        # inspect_response(response, self)
        # Quando executarmos esse spider um shell vai se iniciar
        # onde teremos acesso à variável response gerada aqui por causa da função inspect_response.
        # Para fins de debug é interessante comentar o que vem depois da chamada dessa função.

        logging.info(response.status) # Exibe o status código do request feito
        logging.info(response.url) # Exibe no terminal a url sendo acessada
        # As informações de logging.info são exebidas após uma string semelhante a "2023-03-22 17:23:57 [root] INFO:"

        # Os atributos passados no parâmetro meta são acessados por meio do request feito
        # name = response.request.meta['country_name']
        # rows = response.xpath("(//table)[4]/tbody/tr")
        # for row in rows:
        #     year = row.xpath('.//td[1]/text()').get()
        #     population = row.xpath('.//td[2]/strong/text()').get()
        #     yield {
        #         'country_name': name,
        #         'year': year,
        #         'population': population
        #     }