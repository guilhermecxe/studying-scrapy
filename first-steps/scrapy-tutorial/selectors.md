# Seletores

## Alguns exemplos usando CSS


Obtendo as tags de título.

`response.css('title')`

---

Obtendo os textos das tags de título.

`response.css('title::text')`

---

Obtendo o texto da primeira tag de título.

`response.css('title::text').get()`

---

Obtendo o texto de todas as tags de título.

`response.css('title::text').getall()`

---

Obtendo o atributo de um elemento.

`response.css('a::attr(href)').get()`


## Exemplo usando expressão regular

Obtendo palavras do começo de um título que começam
com "Q".

`response.css('title::text').re(r'Q\w+')`

## Ferramenta para auxiliar na definição de seletores CSS

[SelectorGadget](https://selectorgadget.com/)

## Seletores XPATH

Por baixo dos panos, Scrapy converte seletores CSS em seletores
CSS por eles serem mais poderosos. Inclusive podendo selecionar
elementos baseado no conteúdo de seu texto.

Tutorial para aprender XPATH: http://zvon.org/comp/r/tut-XPath_1.html