import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configurar as opções de download
chrome_options = Options()
load_dotenv()
download_dir = os.environ["DOWNLOADS_PATH"]

# Definir o diretório de download e desativar a janela de confirmação
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", prefs)

# Iniciar navegador
browser = webdriver.Chrome(options=chrome_options)
browser.get("https://nulog.avaconcloud.com/")

# Aguarda o carregamento da página
time.sleep(2)

browser.minimize_window()