import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ..config.settings import ISS_PASSWORD, ISS_USERNAME, WAIT_TIMEOUT_SECONDS


def authUser(driver, url):
    try:
        driver.get(url)
        print(f"Acessando o site: {url}")

        wait = WebDriverWait(driver, WAIT_TIMEOUT_SECONDS)
        click_botao_login = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="login"]/div[1]/div/a[1]'))
        )
        click_botao_login.click()

        inserir_cpf = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))
        inserir_cpf.send_keys(ISS_USERNAME)
        time.sleep(2)

        inserir_senha = driver.find_element(By.XPATH, '//*[@id="password"]')
        inserir_senha.send_keys(ISS_PASSWORD)
        time.sleep(2)

        clicar_login = driver.find_element(By.XPATH, '//*[@id="botao-entrar"]')
        clicar_login.click()
        print("Login realizado com sucesso!")
        time.sleep(3)
        return True

    except Exception as e:
        print(f"Deu erro no login, segue o erro e tente novamente: {e}")
        raise