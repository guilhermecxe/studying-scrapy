# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from shutil import which


class CoinSpiderSelenium(scrapy.Spider):
    name = 'coin_selenium'
    allowed_domains = ['web.archive.org'] 
    # start_urls é especificado para que seja feito um request falso e entremos dentro do método parse,
    # isso porque apenas o request pelo selenium em __init__ não acionaria o método parse
    start_urls = [
        'https://web.archive.org'
    ]

    def __init__(self):
        service = Service(which('geckodriver'))
        options =  Options()
        options.add_argument('--headless')

        driver = webdriver.Firefox(service=service, options=options)
        driver.set_window_size(1920, 1080) # Aumentando o tamanho da janela para exibir mais itens
        driver.get('https://web.archive.org/web/20200116052415/https://www.livecoin.net/en/')

        rur_tab = driver.find_elements(By.CLASS_NAME, 'filterPanelItem___2z5Gb')
        rur_tab[4].click()

        self.html = driver.page_source # Salvando o html da página para ele ser usado no parse
        driver.close()

    def parse(self, response):
        resp = Selector(text=self.html) # obtendo o código da página obtido com o selenium
        for currency in resp.xpath("//div[contains(@class, 'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
            yield {
                'currency pair': currency.xpath(".//div[1]/div/text()").get(),
                'volume(24h)': currency.xpath(".//div[2]/span/text()").get()
            }