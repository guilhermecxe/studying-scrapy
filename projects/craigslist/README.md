# Notas sobre este projeto

Fonte: https://www.pythongasm.com/introduction-to-scrapy/

## Scrapy Shell
Ao invés de rodar o spider para testá-lo a cada alteração, é possível usar uma versão estática da página que é retornada a partir de um request do scrapy.

- Abrindo um shell do Python:
```
$ scrapy shell
```
- Fazendo a requisição de uma página e gerando uma variável `response` (que fica disponível no ambiente, sem a necessidade de capturar o retorno da função):
```
>>> fetch(link)
```
- Abrindo o navegador com o arquivo html retornado:
```
>>> view(response)
```

## Iniciando um projeto Scrapy
```
$ scrapy startproject craigslist
```

## Iniciando um Spider
```
$ scrapy genspider realestate newyork.craigslist.org/d/real-estate/search/rea
```
`realestate` é o nome do Spider e o link é salvo na lista `start_urls`.

O código acima precisa ser executado dentro da pasta `spiders`, que é criada ao iniciar um projeto.

## Rodando o Spider
```
$ scrapy crawl realestate -o output.csv
```
O comando roda o spider `realestate` e salva os resultados em `output.csv`.