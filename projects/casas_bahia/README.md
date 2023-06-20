Este é um mini projeto para obter os nomes do produtos de uma página do site da Casas Bahia que corresponde à pesquisa pelo termo "pneu aro 14".

No módulo `settings.py`, a variável `DEFAULT_REQUEST_HEADERS` foi alterado para melhor simular um request feito pelo navegador.

Para rodar o único spider do projeto basta executar `$ scrapy crawl pneus`.

O método `parse` é baseado em um caminho CSS que pode mudar a qualquer momento. Então, se a execução não retornar resultados pode ser que seja necessário alterar o método.