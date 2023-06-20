import scrapy

# Em settings.py, a variável FEED_EXPORT_ENCODING está especificando que os dados devem ser salvos no formato utf-8
# para evitar aqueles caracteres estranhos que aparecem em urls

# Em settings.py, foram alteradas duas variáveis para modificar o user-agent e as headers

class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['web.archive.org']
    start_urls = ['https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html']

    # Uma outra forma de informar as headers é dentro de Request
    # def start_requests(self):
    #     yield scrapy.Request(url='https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html', callback=self.parse, headers={
    #     })

    def parse(self, response):
        for product in response.xpath("//ul[@class='productlisting-ul']/div/li"):
            yield {
                'title': product.xpath(".//a[@class='p_box_title']/text()").get(),
                'url': response.urljoin(product.xpath(".//a[@class='p_box_title']/@href").get()),
                'discoutned_price': product.xpath(".//div[@class='p_box_price']/span[1]/text()").get(),
                'original_price': product.xpath(".//div[@class='p_box_price']/span[2]/text()").get(),
                'User-Agent': response.request.headers['User-Agent'] # Obtendo o user-agent usado
            }

        next_page = response.xpath("//a[@class='nextPage']/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)