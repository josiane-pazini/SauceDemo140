#1- Bibliotecas ou frameworks
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Classe (opcional)
class Teste_Produtos():

    # 2.1 Atributos (campos, valores)
    url = "https://www.saucedemo.com"             # endereço do site alvo

    # 2.2 Funções e Métodos
    def setup_method(self, method):                     # método de inicialização dos testes
        self.driver = webdriver.Chrome            # instanciar o objeto do Selenium Webdriver com o Chrome
        self.driver.implicitly_wait (10)          # define o tempo de espera padrão por elementos em 10 segundos
        
    def teardown_method(self):                  # método de finalização de testes
        self.driver.quit()                        # encerra/destroi o objeto do Selenium Webdriver da memoria.

    def test_selecionar_produto(self, method):     #método de teste
        self.driver.get(self.url)                  # abre o navegador
        self.driver.find_element(By.ID,  "user-name").send_keys ("standard_user")    # escreve o nome user-name         
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")     # escreve a senha


