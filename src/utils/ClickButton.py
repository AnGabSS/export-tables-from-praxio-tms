from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.WebDriver import browser


def ClickButton(xpath):
    WebDriverWait(browser, 1000).until(
        EC.element_to_be_clickable(
            (By.XPATH, xpath))
    ).click()