# Extraindo dados

O Scrapy oferece ainda um shell onde é possível testar seletores dentro de
uma página. Para abri-lo rodamos `$ scrapy shell <url>`. Isso então baixa
o conteúdo da página da url e abre um shell onde podemos executar
seletores que serão executados na página por meio do objeto `response`.

Exemplo:
```py
>>> response.css('title')
```
Isso obtém o(s) título(s) usado(s) na página que estamos
analisando.

Há ainda a possibilidade de visualizarmos a página da url no navegador por meio do comando:
```py
>>> view(response)
```