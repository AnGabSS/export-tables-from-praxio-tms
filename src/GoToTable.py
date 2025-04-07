
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.WebDriver import browser


def GoToTable(tableName, XPathInTheList=None):
    try:
        # Wait for the search icon to be visible and click it
        search_icon = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/form/div"))
        )
        search_icon.click()

        # Wait for the search input field to be visible
        input_search = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/form/input[1]"))
        )

        # Insert the tableName into the search input
        input_search.send_keys(tableName)
        input_search.send_keys(Keys.RETURN)  # Use RETURN to submit

        # Optional: Check if an element exists and click it (uncomment if needed)
        if(XPathInTheList != None):
            WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, XPathInTheList))
            ).click()
        else:
            try:
                WebDriverWait(browser, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "/html/body/div[1]/div[4]/form/div[4]/div[2]/section[2]/div/ul/li[1]/h3/a"))
                ).click()
            except TimeoutException:
                print("Element not found, skipping click.")

    except TimeoutException:
        print("Timeout waiting for elements to load.")

    finally:
        # Optionally close the browser or handle cleanup here
        print(f"Tabela {tableName} acessada")

