from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time

# Especificando o local do arquivo geckodriver e que o navegador não deve ser exibido
service = Service('./geckodriver.exe')
options = Options()
options.add_argument('--headless')

# Instanciando o driver e requisitando uma página
driver = webdriver.Firefox(service=service, options=options)
driver.get('https://duckduckgo.com')

# Escrevendo um texto em um campo
search_input = driver.find_element(By.ID, 'searchbox_input')
search_input.send_keys('My User Agent')

# Clicando em um botão para realizar a busca
# search_btn = driver.find_element(By.CLASS_NAME, 'searchbox_searchButton__F5Bwq')
# search_btn.click()

# Pressionando enter para realizar a busca
search_input.send_keys(Keys.ENTER)

# Exibindo o html da página
# print(driver.page_source)

# Esperando 5 segundos e fechando o driver
time.sleep(5)
driver.close()