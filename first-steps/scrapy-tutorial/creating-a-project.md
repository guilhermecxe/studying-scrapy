# Criando um projeto

Usando o comando `$ scrapy startproject tutorial` iniciamos um projeto com
o nome "tutorial" e com a seguinte estrutura:

```py
tutorial/
    scrapy.cfg            # configurações de deploy

    tutorial/             # módulo do projeto, você irá importar seu código daqui
        __init__.py

        items.py          # definicação dos items do projeto

        middlewares.py    # definicação dos middlewares

        pipelines.py      # definicação dos pipelines

        settings.py       # configurações do projeto

        spiders/          # onde as spiders do projeto serão colocadas
            __init__.py
```