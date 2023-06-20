# Conteúdo escrito

## Debugging usando o terminal

Nesse comando para debugging estamos obtendo o resultado de `parse_country` quando ele é executado para a url informada. Estamos assinalando um valor para `meta` porque nessa execução o método `parse` é pulado, então o valor de `meta` não é passado para `parse_country` durante a execução.
```bash
scrapy parse --spider=countries -c parse_country --meta='{\"country_name\": \"China\"}' https://www.worldometers.info/world-population/china-population/
```

## Alterando o User-Agent

Para alterar o User-Agent de um projeto basta alterar a variável `USER_AGENT` dentro do arquivo `settings.py` do projeto.

No projeto `imdb` há um spider (`best_movies`) que descreve como alterar o user-agent dentro do próprio spider.

## Alterando as headers

Para alterar as headers usadas em um projeto basta alterar a variável `DEFAULT_REQUEST_HEADERS` dentro do arquivo `settings.py` do projeto.

No projeto `imdb` há um spider (`best_movies`) que descreve como alterar as headers dentro do próprio spider.

## Sobre o `scrapy-selenium`

Olhando agora (26 de março de 2023), esse pacote não é atualizado a cerca de 4 anos. E um dos problemas disso é que, usando ele e o pacote `selenium` mais recente, aparece um problema com o argumento `firefox_options`, então a forma que eu escolhi resolver isso foi usando a versão do `selenium` que está nos requisitos do `scrapy-selenium`, que é a versão 3.9.