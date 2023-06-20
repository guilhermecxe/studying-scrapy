Por padrão, o Scrapy usa o protocolo http, mas alguns sites usam https, então, se necessário, é possível alterar o protocolo de `start_urls` no Spider.

---
```
ValueError: Missing scheme in request url: /world-population/china-population/
```
O erro acima ao tentar rodar um Spider significa que o scrapy não sabe se o link usa HTTP ou HTTPS. E esse erro costuma ser associado a links relativos já que esses não trazem o protocolo. Mas isso pode ser facilmente solucionado unindo o domínio do site com o link relativo usando `urljoin` ou `response.follow`.

---
```
Filtered offsite request to 'www.worldometers.info': <GET https://www.worldometers.info/world-population/china-population/>
```
Geralmente ocasionado por uma barra final na url do domínio do site em `allowed_domains.`
