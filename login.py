from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def authUser(driver, url):
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

    except Exception as e:
        print(f'Deu erro no login, segue o erro: {e}')    