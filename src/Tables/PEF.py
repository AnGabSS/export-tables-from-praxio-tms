from time import sleep

from src.GoToTable import GoToTable

from src.utils.ClickButton import ClickButton
from src.utils.PutInitialDate import PutInitialDate
from src.utils.RenameFile import RenameFile
from src.utils.WaitLoadPage import WaitLoadPage


def PEF():
    GoToTable("PEF", "/html/body/div[1]/div[4]/form/div[4]/div[2]/section[2]/div[1]/ul/li[2]/h3/a")
    try:

        PutInitialDate("/html/body/div[1]/div[4]/form/div[5]/div[1]/div[1]/div[5]/div/div/input[1]")

        ClickButton("/html/body/div[1]/div[4]/form/div[5]/div[1]/div[1]/div[7]/button")
        sleep(2)
        WaitLoadPage()

        ClickButton("/html/body/div[1]/div[4]/form/div[5]/div[1]/div[3]/div/div[2]/div[4]/a[2]")

        RenameFile("PEF", "pef")

    finally:
        # Fecha o navegador após a execução
        print("PEF Finalizado")