# Organização

## Projetos

### `livecoin`

Nesse projeto estamos usando `selenium` para fazer uma requisição e o `scrapy` para lidar com a página obtida.

## Debugging

As técnicas de debugging estão descritas no projeto `worldometers`. Essas técnicas são as seguintes:
- `open_in_browser`
- `inspect_response`
- `logging.info`

Existe ainda mais uma técnica de debugging que está em um vídeo de 4 minutos de um curso da Udemy. Ele consiste em usarmos os métodos de debugging do VSCode. [Clique aqui para acessar o vídeo](https://www.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/16388482#overview).

Além desses, há, no arquivo `WRITTEN-CONTENT.md`, um método de debugging usando o terminal.

## Templates

### Crawl

No projeto nomeado `imdb` temos um spider, o `best_movies`, que foi criado usando o template `crawl`. Após criar o projeto, esse spider foi criado com o seguinte comando:
```bash
$ scrapy genspider -t crawl best_movies "http://web.archive.org"
```

Além disso, as classes `Rule` e `LinkExtractor` são descritas nesse mesmo projeto.