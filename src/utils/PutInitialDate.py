from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.WebDriver import browser
from src.utils.GetDate3MonthsAgo import GetDate3MonthsAgo
from src.utils.GetDate6MonthsAgo import GetDate6MonthsAgo


def PutInitialDate(xpath, isSixMonth=False):
    initialDate_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, xpath))
    )
    initialDate_input.clear()
    if(isSixMonth):
        initialDate_input.send_keys(GetDate6MonthsAgo())
    else:
        initialDate_input.send_keys(GetDate3MonthsAgo())