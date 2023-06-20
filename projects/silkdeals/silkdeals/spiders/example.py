import scrapy
import time
from scrapy.selector import Selector
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ExampleSpider(scrapy.Spider):
    name = 'example'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://duckduckgo.com',
            wait_time=3, # esperando depois de requisitar a página
            screenshot=True, # fazer uma imagem da tela
            callback=self.parse,
        )

    def parse(self, response):
        # obtendo a imagem tirada da página e salvando
        # img = response.meta['screenshot']
        # with open('screenshot.png', 'wb') as f:
        #     f.write(img)

        driver = response.meta['driver']
        search_input = driver.find_element(By.ID, 'searchbox_input')
        search_input.send_keys('Hello World')
        # driver.save_screenshot('after_filling_input.png')
        search_input.send_keys(Keys.ENTER)
        time.sleep(2) # Se não houver esse wait, então 
        # driver.save_screenshot('after_enter.png')

        html = driver.page_source
        response_obj = Selector(text=html)

        links = response_obj.xpath("//a[@class='eVNpHGjtxRBq_gLOfGDr LQNqh2U1kzYxREs65IJu']")
        print('-----', len(links), '------')
        for link in links:
            yield {
                'URL': link.xpath('.//@href').get()
            }
