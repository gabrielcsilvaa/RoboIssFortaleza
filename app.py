from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd  
import time

def configurar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def acessar_site(url):
    driver = configurar_driver()

    try:
        driver.get(url)
        print(f"Acessando o site: {url}")

        wait = WebDriverWait(driver, 10)
        click_botao_login = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="login"]/div[1]/div/a[1]'))
        )
        click_botao_login.click()
        print("Cliquei em 'fazer login'")

        inserir_cpf = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))
        inserir_cpf.send_keys("389.256.643-72")
        time.sleep(2)

        inserir_senha = driver.find_element(By.XPATH, '//*[@id="password"]')
        inserir_senha.send_keys("Fiscal@2021")
        time.sleep(2)

        clicar_login = driver.find_element(By.XPATH, '//*[@id="botao-entrar"]')  
        clicar_login.click()
        print("Login realizado com sucesso!")
        time.sleep(5)
        clicar_Cnpj = driver.find_element(By.XPATH, '//*[@id="alteraInscricaoForm:tipoPesquisa"]/tbody/tr/td[2]/label')
        clicar_Cnpj.click
        print("cliquei no cnpj")
        time.sleep(10000)

    except Exception as e:
        print(f"Erro ao acessar o site: {e}")

def buscar_dados_excel():
    arquivo = "planilha_robo_iss.xlsx"
    df = pd.read_excel(arquivo)

    for index, row in df.iterrows():
        cnpj = row['CNPJ'] 
    

acessar_site("https://iss.fortaleza.ce.gov.br/grpfor/login.seam?cid=33110")
buscar_dados_excel()
