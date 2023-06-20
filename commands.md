# Comandos

## startproject
```bash
$ scrapy startproject <name>
```
Inicia um projeto Scrapy com o nome dado.

## bench

```bash
$ scrapy bench
```
Este comando roda vários requests na máquina para avaliar a performance do computador e da internet. Rodando agora, o resultado apresenta que esta máquina consegue requisitar algo em torno de 2880 páginas por minuto.

## fetch

```bash
$ scrapy fetch <link>
```
Faz uma requisição do link informado.

## crawl

```bash
$ scrapy crawl <spider>
```
Dentro de um projeto, executa o Spider informado.

Ainda é possível salvar os dados obtidos usando a flag `-o` e o nome do arquivo com o tipo desejado no seguinte formato:
```bash
$ scrapy crawl <spider> -o <filename>.<filetype>
```
Podendo o tipo ser de diversos formatos, incluindo: `json`, `csv` e `xml`.

## genspider

```bash
$ scrapy genspider <name> <domain>
```

Usado para criar um novo spider (dentro de um projeto) com o nome dado e com o domínio informado já dentro de `allowed_domains` e `start_urls`.

O link do domínio deve vir sem o protocolo (http/https) e sem uma barra (/) ao final.

## runspider

```bash
$ scrapy runspider
```

Roda um spider que não está dentro de um projeto Scrapy. Podemos especificar qual será o output como no comando `crawl`.

## settings

```bash
$ scrapy settings
```

Exibe as configurações do projeto atual.

## shell

```bash
$ scrapy shell
```

Inicia um console python com alguns objetos, funções e variáveis do Scrapy. Útil para testes.

## version

```bash
$ scrapy version
```

Exibe a verão atual do Scrapy

## view
```bash
$ scrapy view <link>
```
Exibe no navegador como a página é retornada para o Scrapy.

## Dicas:

---
Usar
```bash
$ scrapy <command> -h
```
para entender melhor algum comando quando necessário.

---