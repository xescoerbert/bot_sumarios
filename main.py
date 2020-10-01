from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.driver_path = '/home/codebin/Área de Trabalho/Projetos 2020-2021/UDEMY/PYTHON/sumarios/chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(
         self.driver_path,
         options=self.options   
        )
    

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def faz_login(self):
        try:
            # numero do cartao
            input_login = self.chrome.find_element_by_id("ncartao")
            # pass
            input_password = self.chrome.find_element_by_id('codigo')
            # butão
            btn_login = self.chrome.find_element_by_class_name('btn.blue.pull-right')
            # Dados do user
            input_login.send_keys('')
            input_password.send_keys('')
            sleep(3)
            btn_login.click()
        except Exception as e:
            print('Erro ao fazer login:', e)


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('http://193.236.88.238:8080/index.html#login')
    chrome.faz_login()

    sleep(5)

    chrome.sair()