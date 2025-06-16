from time import sleep

from src.GoToTable import GoToTable
from src.utils.ClickButton import ClickButton
from src.utils.PutInitialDate import PutInitialDate
from src.utils.RenameFile import RenameFile
from src.utils.WaitLoadPage import WaitLoadPage


def Abastecimento():
    GoToTable("Consulta de Abastecimento (Modelo 2)")
    try:

        PutInitialDate("/html/body/div[1]/div[4]/form/div[1]/div[2]/div/div[1]/div[3]/div/div/div/input[1]")

        ClickButton("/html/body/div[1]/div[4]/form/div[1]/div[2]/div/div[1]/div[15]/input")

        ClickButton("/html/body/div[1]/div[4]/form/div[6]/div[5]/div/div/div/div[1]/div/span[2]/button[2]")

        WaitLoadPage()
        sleep(4)

        ClickButton("/html/body/div[1]/div[4]/form/div[6]/div[5]/div/div/div/div[1]/div/span/button[2]")

        WaitLoadPage()
        sleep(4)

        ClickButton("/html/body/div[1]/div[4]/form/div[6]/div[2]/div[4]/a[2]")

        RenameFile("Consulta Abastecimento (Modelo 2)", "abastecimento")


    finally:
        # Fecha o navegador após a execução
        print("Abastecimento finalizado")