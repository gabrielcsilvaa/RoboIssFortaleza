from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.automation.inscricao import click_inscricao
from src.automation.login import authUser
from src.automation.post_data import (
    escrituracaoFinalStretch,
    escriturando1,
    escriturarData,
    finishInscricao,
)
from src.config.settings import ISS_LOGIN_URL, PLANILHA_PATH
from src.utils.date_utils import get_previos_month_and_year


def configurar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def main():
    cnpj = input("Digite o CNPJ da empresa: ")
    mes = input("informe o mes desejado(exemplo 5):  ")
    ano = input("informe o ano desejado(exemplo 2024): ")
    ano = str(ano)
    mes = int(mes)

    # mes_ano = get_previos_month_and_year()
    # mes = mes_ano[0]
    # ano = str(mes_ano[1])

    driver = configurar_driver()
    try:
        authUser(driver, ISS_LOGIN_URL)

        dados = click_inscricao(driver, PLANILHA_PATH, cnpj)
        continuacao = "inicio"
        for index, row in dados.iterrows():
            print(f"Processando {index + 1} de {len(dados)} escrituracoes de notas")

            if continuacao == "inicio":
                escriturarData(driver, ano, mes)
                escriturando1(driver)

            finishInscricao(driver, dados, row)
            continuacao = escrituracaoFinalStretch(driver, row)

        print("Escrituracoes finalizadas!")

    except Exception as e:
        print(f"Erro ao acessar o site. Tente novamente: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
