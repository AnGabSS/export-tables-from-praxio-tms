from time import sleep

from src.GoToTable import GoToTable
from src.utils.ClickButton import ClickButton
from src.utils.PutInitialDate import PutInitialDate
from src.utils.RenameFile import RenameFile
from src.utils.WaitLoadPage import WaitLoadPage


def ContasAPagar():
    GoToTable("Relatório de Contas a Pagar")
    try:

        ClickButton("/html/body/div[1]/div[4]/form/div[1]/div[2]/div/div[1]/div[3]/div/select/option[1]")

        ClickButton("/html/body/div[1]/div[4]/form/div[1]/div[2]/div/div[1]/div[4]/div/div/select/option")

        PutInitialDate("/html/body/div[1]/div[4]/form/div[1]/div[2]/div/div[1]/div[5]/div/div/div/input[1]")

        ClickButton("/html/body/div[1]/div[4]/form/div[1]/div[2]/div/div[1]/div[15]/input")

        sleep(2)

        # Wait for overlay to be hidden (display: none)
        WaitLoadPage()

        # Now perform the final click
        ClickButton("/html/body/div[1]/div[4]/form/div[6]/div[2]/div[4]/a[1]")
        RenameFile("Filial_  _ Unidade_  _ Período_ ", "contas a pagar")

    finally:
        # Fecha o navegador após a execução
        print("Contas a Pagar finalizada")