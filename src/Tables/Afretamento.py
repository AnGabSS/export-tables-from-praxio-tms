from src.GoToTable import GoToTable

from src.utils.ClickButton import ClickButton
from src.utils.PutInitialDate import PutInitialDate
from src.utils.RenameFile import RenameFile


def Afretamento():
    GoToTable("Relatório de Afretamento")
    try:

        PutInitialDate("/html/body/div[1]/div[4]/form/div[1]/div[2]/div/div[1]/div[5]/div/div/div/input[1]")

        ClickButton("/html/body/div[1]/div[4]/form/div[1]/div[2]/div/div[1]/div[17]/input")

        ClickButton("/html/body/div[1]/div[4]/form/div[6]/div[2]/div[4]/a[1]")

        RenameFile("Relatório de Afretamento", "afretamento")

    finally:
        # Fecha o navegador após a execução
        print("Afretamento Finalizado")