# Selectors

## CSS Selector

`"h1"`: Selecionando todos os elementos de tag `h1`.

---
`".intro"`: Todos os elementos com classe `intro`.

---
`"#location"`: Selecionando o elemento com id `location`.

---
`"div.intro"`: Elementos de tag `div` e com classe `intro`.

---
`"span#location"`: Elemento de tag `span` e com id `location`.

---
`".bold.italic"`: Elementos com classe `bold` e com classe `italic`.

---
`li[data-identifier=7]`: Elementos de tag `li` com atributo `data-identifier` igual a 7.

---
`"a[href^='https']"`: Links que começam com "https"

---
`"a[href$='fr']"`: Links que terminam com "fr"

---
`"a[href~='google']"`: Links que contém "google"

---
`"div.intro p"`: Elementos de tag `p` descendentes diretos de elementos de `div` com classe `intro`.

---
`"div > p"`: Elementos de `p` descendentes, em qualquer nível, de elementos de tag `div`.

---
`"div + p"`: Elementos de tag `p` que venham **imediatamente** depois (no mesmo nível) de elementos de tag `div`.

---
`"div ~ p"`: Para selecionar qualquer elemento `p` que venha depois (no mesmo nível) de um `div`.

---
`"li:nth-child(1)"`: Selecionando o primeiro elemento descendente direto de um `li`.

---
`"li:nth-child(even)"`: Selecionando os descendentes de `li` que tenham uma posição par.

---
`"li:nth-child(odd)"`: Selecionando os descendentes de `li` que tenham uma posição ímpar.


## XPath Selector

`"//h1"`: Selecionando todos os elementos de tag `h1`.

---
`"//div[@class='intro']"`: Todos os elementos `div` com classe `intro`.

---
`"//div[@class='intro' or @class='outro']"`: Elementos `div` com classe `intro` ou `outro`.

---
`"//div[@class='intro']/p"`: Elementos `p` que estão dentro de elementos `div` com classe `intro`.

---
`"//p/text()"`: Obtendo o texto dos elementos `p`.

---
`"//a/@href"`: Obtendo todos os links.

---
`"//a[starts-with(@href, 'https')]"`: Obtendo todos os elementos `a` cujo link começa com "https".

---
`"//a[ends-with(@href, 'fr')]"`: Todos os elementos `a` cujo link termina com "fr". Talvez não disponível para todos os navegadores

---
`"//a[contains(@href, 'google')]"`: Todos os elementos `a` que o link contém "google".

---
`"//a[contains(text(), 'France')]"`: Todos os elementos `a` que o texto contém "France".

---
`"ul[@id='items']/li[1]"`: Primeiro elemento `li` que está dentro de um elemento `ul` com classe `items`.

---
`"ul[@id='items']/li[1 or 4]"`: Do primeiro ao quarto elemento `li`.

---
`"ul[@id='items']/li[position() = 1 or position() = 4]"`: O primeiro e o quarto elemento `li`.

---
`"ul[@id='items']/li[position() = last()]"`: O último elemento `li`.

---
`"ul[@id='items']/li[position() > 1]"`: Todos os elementos `li` depois do primeiro.

## Indo para cima no HTML

> `"//p[@id='unique']/parent::div"`
>
> Obtendo elementos `div` que são pais de elementos `p` com id `unique`.

> `"//p[@id='unique']/parent::node()"`
>
> Obtendo elementos que são pais de elementos `p` com id `unique`.

> `"//p[@id='unique']/ancestor::div"`
>
> Obtendo elementos `div` que são ancestrais de elementos `p` em qualquer nível.

> `"//p[@id='unique']/ancestor::node()"`
>
> Obtendo elementos que são ancestrais de elementos `p` em qualquer nível.

> `//p[@id='unique']/preceding::node()`
>
> Todos os elementos que precedem o elemento `p` de id `unique`, menos os seus "ancestrais".

> `//p[@id='outside']/preceding-sibling::node()`
>
> Elementos irmãos do elemento `p` de id `outside` e que venham antes.

## Indo para baixo no HTML

> `"//div/child::p"`
>
> Todos os filhos `p` de `div`.

> `"//div/child::node()"`
>
> Todos os filhos de `div`.

> `"//div/following::node()"`
>
> Todos os elementos que vem depois de `div` no HTML.

> `"//div/following-sibling::node()"`
>
> Todos os elementos que vem depois de `div` e que estão no mesmo nível que ele.

> `"//div/descendant::node()"`
>
> Todos os descendentes de `div`.


Os dois comandos abaixo retornam a mesma coisa.
```py
>>> response.css('title::text')[0].get()
>>> response.css('title::text').get()
```

---

Para selecionar um elemento baseado em mais de uma de suas classes, é preciso separá-las com um ponto (`.`).

Exemplo ("`result-title`" e "`hdrlnk`" são as classes):
```py
>>> response.css("a.result-title.hdrlnk::text").get()
```

response.xpath('//h1')
response.xpath('//h1/text()')
response.xpath('//h1/text()').get()

response.css('h1::text').get()

response.xpath('//td/a/text()').getall()

Sempre começar xpath com `.//` quando estiver usando ele em um Selector, diferente de quando é um response.