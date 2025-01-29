from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os 

from get_year_month import get_previos_month_and_year
from login import authUser
from inscricao import click_inscricao
from post_data import escriturarData, escriturando1,finishInscricao, escrituracaoFinalStretch

cnpj = input('Digite o CNPJ da empresa: ')

nome_planilha = 'planilha_robo_iss.xlsx'
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
print(f"Caminho da planilha robo_iss: {desktop_path}")

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
try:
    authUser(driver, 'https://iss.fortaleza.ce.gov.br/grpfor/login.seam?cid=33110')

    dados = click_inscricao(driver, caminho_planilha, cnpj)
    continuacao = 'inicio'
    for index, row in dados.iterrows():
        
        print(f'Processando {index +1 } de {len(dados)} escriturações de notas')

        if continuacao == 'inicio':
            escriturarData(driver, ano , mes )
            escriturando1(driver)
        
        descricao = finishInscricao(driver, dados, row)
        continuacao = escrituracaoFinalStretch(driver, row)

    print('Escriturações Finalizadas!')



       



     


except Exception as e:
    print(f"Erro ao acessar o site tente novamente: {e}")




