from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.WebDriver import browser
from src.utils.GetDateIn3Months import GetDateInThreeMonths


def PutDueDate(xpath):
    dueDate_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, xpath))
    )
    dueDate_input.clear()
    dueDate_input.send_keys(GetDateInThreeMonths())
