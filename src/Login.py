import os

from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.WebDriver import browser


def Login():
    try:

        load_dotenv()

        input_user = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/section[2]/form/div[3]/ul/li[1]/input"))
        )

        # Agora você pode interagir com o elemento se necessário
        # input_element.send_keys("algum valor")  # Por exemplo, para preencher um campo de texto

        input_user.send_keys(os.environ["PRAXIO_USER"])  # Pode usar o sleep para testar ou esperar um pouco mais, se necessário.

        input_password = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/section[2]/form/div[3]/ul/li[2]/input"))

        )

        input_password.send_keys(os.environ["PRAXIO_PASSWORD"])

        input_button = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/section[2]/form/div[3]/div/input"))
        )

        input_button.click()

    finally:
        # Fecha o navegador após a execução
        print("Login realizado com sucesso")