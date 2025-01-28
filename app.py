from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import pandas as pd  
import time
import os 

from get_year_month import get_previos_month_and_year
from login import authUser
from inscricao import click_inscricao
from post_data import escriturarData, escriturando1,finishInscricao

cnpj = input('Digite o CNPJ da empresa: ')

nome_planilha = 'planilha_robo_iss.xlsx'
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
print(f"Caminho da área de trabalho: {desktop_path}")

caminho_planilha = os.path.join(desktop_path, nome_planilha)
def configurar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

mesANO = get_previos_month_and_year()
mes = mesANO[0]
ano = str(mesANO[1])



driver = configurar_driver()
#aqio
try:
    authUser(driver, 'https://iss.fortaleza.ce.gov.br/grpfor/login.seam?cid=33110')


    dados = click_inscricao(driver, caminho_planilha, cnpj)
    
    userCnpj = dados['CNPJ']
    numDoc = dados['N-DOCUMENTO']
    dataDoc = dados['DATA DOCUMENTO']
    codCnae = dados['CODIGO CNAE']
    serie = dados['SERIE']
    uf = dados['UF']
    cidade = dados['CIDADE']
    serviceValue = dados['VALOR DO SERVIÇO']

    escriturarData(driver, ano , mes )
    escriturando1(driver)
    finishInscricao(driver, dados)
    




except Exception as e:
    print(f"Erro ao acessar o site: {e}")




