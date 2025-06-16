from time import sleep

from src.GoToTable import GoToTable
from src.utils.ClickButton import ClickButton
from src.utils.PutInitialDate import PutInitialDate
from src.utils.RenameFile import RenameFile
from src.utils.WaitLoadPage import WaitLoadPage


def OrdemDeServico():
    GoToTable("Ordem de Serviço", "/html/body/div[1]/div[4]/form/div[4]/div[2]/section[2]/div[1]/ul/li[6]/h3/a")
    try:

        PutInitialDate("/html/body/div[1]/div[4]/form/div[5]/div[1]/div[1]/div[5]/div/div/input[1]", True)

        ClickButton("/html/body/div[1]/div[4]/form/div[5]/div[1]/div[1]/div[11]/button")

        sleep(5)
        WaitLoadPage()

        ClickButton("/html/body/div[1]/div[4]/form/div[5]/div[1]/div[3]/div/div[2]/div[4]/a[2]")

        RenameFile("Filial_Unidade_ 1_1 - Período_ ", "ordem de serviço")


    finally:
        # Fecha o navegador após a execução
        print("Ordem de serviço finalizado")