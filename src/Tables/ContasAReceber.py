from time import sleep

from src.GoToTable import GoToTable
from src.utils.ClickButton import ClickButton
from src.utils.PutDueDate import PutDueDate
from src.utils.PutInitialDate import PutInitialDate
from src.utils.RenameFile import RenameFile
from src.utils.WaitLoadPage import WaitLoadPage


def ContasAReceber():
    GoToTable("Relatório de Contas a Receber", "/html/body/div[1]/div[4]/form/div[4]/div[2]/section[2]/div/ul/li[1]/h3/a")
    try:
        ClickButton("/html/body/div[1]/div[4]/form/div[1]/div[2]/div[1]/div[1]/div[1]/div/select/option[1]")

        ClickButton("/html/body/div[1]/div[4]/form/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/select/option")

        PutInitialDate("/html/body/div[1]/div[4]/form/div[1]/div[2]/div/div[1]/div[3]/div/div/div/input[1]", True)
        PutDueDate("/html/body/div[1]/div[4]/form/div[1]/div[2]/div/div[1]/div[5]/div/div/div/input[1]")

        sleep(2)

        WaitLoadPage()
        ClickButton("/html/body/div[1]/div[4]/form/div[1]/div[2]/div/div[1]/div[12]/input")

        sleep(2)

        WaitLoadPage()

        ClickButton("/html/body/div[1]/div[4]/form/div[6]/div[2]/div[4]/a[2]")

        RenameFile("Filial_  _ Unidade_  _ Período", "contas a receber")


    finally:
        # Fecha o navegador após a execução
        print("Contas a Receber finalizada")