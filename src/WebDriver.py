import os
import time

import win32con
import win32gui
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

chrome_options.add_argument('--headless=new')

# Iniciar navegador
browser = webdriver.Chrome(options=chrome_options)
browser.get("https://nulog.avaconcloud.com/")

# Aguarda o carregamento da página e da janela
time.sleep(2)

# Tenta localizar a janela pelo título
window_title = browser.title
hwnd = win32gui.FindWindow(None, window_title)

if hwnd:
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
else:
    print(f"Janela com título '{window_title}' não encontrada.")
    browser.minimize_window()
