# Rodando o spider

Para rodar o spider em `tutorial/tutorial/spiders/quotes_spider.py` usamos o comando `$ scrapy crawl quotes`. Sendo `quotes` o nome do spider.

Se o objetivo for salvar os dados em coletados no método `parse` podemos usar o comando
`$ scrapy crawl quotes -O quotes.json` que isso salvará os dados em formato JSON. Para incrementar
`quotes.json` nós usamos a flag `-o` ao invés de `-O`, no entanto, isso tornará o arquivo JSON inválido,
então a nossa alternativa é armazenar os arquivos no fomato `.jl`, onde o incremento funcionará perfeitamente.