from time import sleep

from selenium.common.exceptions import TimeoutException, WebDriverException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.GoToTable import GoToTable
from src.WebDriver import browser
from src.utils.ClickButton import ClickButton
from src.utils.PutInitialDate import PutInitialDate
from src.utils.RenameFile import RenameFile
from src.utils.WaitLoadPage import WaitLoadPage


def DocumentosEmitidos():
    try:
        # Configura timeout global para operações
        browser.implicitly_wait(30)

        # 1. Navega para a tabela
        GoToTable("Consulta de Documentos Emitidos e Cancelados - Modelo 2")

        # 2. Define a data inicial
        PutInitialDate("/html/body/div[1]/div[4]/form/div[1]/div[2]/div/div[1]/div[7]/div/div/div/input[1]")

        ClickButton("/html/body/div[1]/div[4]/form/div[1]/div[2]/div/div[1]/div[19]/div/select/option[2]")

        # 3. Clica no botão de pesquisa
        ClickButton("/html/body/div[1]/div[4]/form/div[1]/div[2]/div/div[1]/div[32]/input")

        # 4. Espera o processamento terminar (loading desaparecer)
        try:
            WaitLoadPage()
        except TimeoutException:
            print("Aviso: Timeout ao esperar pelo fim do carregamento, continuando mesmo assim...")

        # 5. Localiza e clica no botão de exportação com tratamento robusto
        export_button_xpath = "/html/body/div[1]/div[4]/form/div[6]/div[2]/div[4]/a[2]"

        try:
            sleep(60)
            button = WebDriverWait(browser, 60).until(
                EC.element_to_be_clickable((By.XPATH, export_button_xpath))
            )
            button.click()
        except ElementClickInterceptedException:
            # Fallback: clique via JavaScript
            button = browser.find_element(By.XPATH, export_button_xpath)
            browser.execute_script("arguments[0].click();", button)

        # 6. Espera o download completar
        sleep(120)  # Espera básica - pode ser substituída por verificação de arquivo

        # 7. Renomeia o arquivo baixado
        RenameFile("Filial_ 1 _ Unidade_ 1 _ Período_ ", "documentos emitidos", 10000000000)

    except TimeoutException as te:
        print(f"Erro de timeout: {str(te)}")
        raise
    except WebDriverException as wde:
        print(f"Erro do WebDriver: {str(wde)}")
        raise
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")
        raise
    finally:
        print("Documentos emitidos finalizado")