from time import sleep

from src.GoToTable import GoToTable

from src.utils.ClickButton import ClickButton
from src.utils.PutInitialDate import PutInitialDate
from src.utils.RenameFile import RenameFile
from src.utils.WaitLoadPage import WaitLoadPage


def ColetasEmitidas():
    GoToTable("Listagem Coletas Emitidas - Modelo 2")
    try:
        ClickButton("/html/body/div[1]/div[4]/form/div[1]/div[2]/div/div[1]/div[10]/input")
        sleep(2)
        WaitLoadPage()

        ClickButton("/html/body/div[1]/div[4]/form/div[6]/div[2]/div[4]/a[2]")

        RenameFile("Listagem Coletas Emitidas - Modelo 1", "coletas emitidas")

    finally:
        # Fecha o navegador após a execução
        print("Listagem Coletas Emitidas Finalizado")