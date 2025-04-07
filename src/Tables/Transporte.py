from time import sleep

from src.GoToTable import GoToTable
from src.utils.ClickButton import ClickButton
from src.utils.PutInitialDate import PutInitialDate
from src.utils.RenameFile import RenameFile
from src.utils.WaitLoadPage import WaitLoadPage


def Transporte():
    GoToTable("Transporte", "/html/body/div[1]/div[4]/form/div[4]/div[2]/section[2]/div[1]/ul/li[19]/h3/a")
    try:
        ClickButton("/html/body/div[1]/div[4]/form/div[5]/div[1]/div[1]/div[2]/select/option[1]")

        PutInitialDate("/html/body/div[1]/div[4]/form/div[5]/div[1]/div[1]/div[5]/div/div/input[1]")

        ClickButton("/html/body/div[1]/div[4]/form/div[5]/div[1]/div[1]/div[18]/button")

        sleep(1)
        WaitLoadPage()

        ClickButton("/html/body/div[1]/div[4]/form/div[5]/div[1]/div[2]/div/div[2]/div[4]/a[1]")

        RenameFile("Filial_  _ Unidade_  _ Período_ ", "transporte")


    finally:
        # Fecha o navegador após a execução
        print("Transporte finalizado")