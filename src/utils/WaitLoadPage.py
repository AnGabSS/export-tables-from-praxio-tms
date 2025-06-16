from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.WebDriver import browser


def WaitLoadPage(id=None):

    sleep(4)
    if(id != None):
        return WebDriverWait(browser, 1000).until(
            EC.invisibility_of_element_located(
                (By.XPATH, '/html/body/div[1]/div[4]/form/div[5]/div[3][contains(@style, "display: none")]'))
        )
    return WebDriverWait(browser, 1000).until(
        EC.invisibility_of_element_located(
            (By.XPATH, '/html/body/div[1]/div[4]/form/div[5]/div[3][contains(@style, "display: none")]'))
    )