import pandas as pd  
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


def click_inscricao(driver, caminho_planilha,cnpj):


    clicar_Cnpj = driver.find_element(By.XPATH, '//*[@id="alteraInscricaoForm:tipoPesquisa"]/tbody/tr/td[2]/label')
    actions = ActionChains(driver)
    actions.move_to_element(clicar_Cnpj).click().perform()
    time.sleep(2) 
    dados = pd.read_excel(caminho_planilha)

    campo_cnpj = driver.find_element(By.XPATH, '//*[@id="alteraInscricaoForm:cpfPesquisa"]')
    campo_cnpj.clear()
    campo_cnpj.send_keys(cnpj)
    time.sleep(2)

    clicar_pesquisar = driver.find_element(By.XPATH, '//*[@id="alteraInscricaoForm:btnPesquisar"]')
    clicar_pesquisar.click()
    time.sleep(5)

    clicar_empresa = driver.find_element(By.XPATH, '//*[@id="alteraInscricaoForm:empresaDataTable:0:linkInscricao"]')
    clicar_empresa.click()
    time.sleep(2)

    return dados