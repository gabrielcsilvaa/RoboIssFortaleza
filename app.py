from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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
        actions = ActionChains(driver)
        actions.move_to_element(clicar_Cnpj).click().perform()
        print("cliquei no cnpj")
        time.sleep(2)

        caminho_planilha = r'C:\Users\Nicolas-ti\Desktop\planilha_robo_iss.xlsx'
        dados = pd.read_excel(caminho_planilha)
        print(f"Dados carregados:\n{dados}")

        for index, row in dados.iterrows():
            cnpj=row['CNPJ']
            print(f"Processando CNPJ: {cnpj}")

            campo_cnpj = driver.find_element(By.XPATH, '//*[@id="alteraInscricaoForm:cpfPesquisa"]')
            campo_cnpj.clear()
            campo_cnpj.send_keys(cnpj)
            time.sleep(2)

            clicar_pesquisar = driver.find_element(By.XPATH, '//*[@id="alteraInscricaoForm:btnPesquisar"]')
            clicar_pesquisar.click()
            print("cliquei em pesquisar")
            time.sleep(5)

            clicar_empresa = driver.find_element(By.XPATH, '//*[@id="alteraInscricaoForm:empresaDataTable:0:linkInscricao"]')
            clicar_empresa.click()
            print("cliquei na empresa")
            time.sleep(4)

            clicar_escrituracao = driver.find_element(By.XPATH, '//*[@id="navbar"]/ul/li[6]/a')
            clicar_escrituracao.click()
            time.sleep(2)

            clicar_escrituracao2 = driver.find_element(By.XPATH, '//*[@id="formMenuTopo:menuEscrituracao:j_id78"]')
            clicar_escrituracao2.click()
            time.sleep(10000)

    except Exception as e:
        print(f"Erro ao acessar o site: {e}")



acessar_site("https://iss.fortaleza.ce.gov.br/grpfor/login.seam?cid=33110")
