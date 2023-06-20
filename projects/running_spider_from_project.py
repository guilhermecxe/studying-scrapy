# Rodando um spider que está dentro de um projeto

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from casas_bahia.casas_bahia.spiders.pneus import PneusSpider

process = CrawlerProcess(settings=get_project_settings())
process.crawl(PneusSpider)
process.start()