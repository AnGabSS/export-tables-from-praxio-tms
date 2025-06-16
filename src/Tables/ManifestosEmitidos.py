from src.GoToTable import GoToTable
from src.utils.ClickButton import ClickButton
from src.utils.PutInitialDate import PutInitialDate
from src.utils.RenameFile import RenameFile


def ManifestosEmitidos():
    GoToTable("Listagem de Manifestos Emitidos")
    try:

        PutInitialDate("/html/body/div[1]/div[4]/form/div[1]/div[2]/div/div[1]/div[5]/div/div/div/input[1]")

        ClickButton("/html/body/div[1]/div[4]/form/div[1]/div[2]/div/div[1]/div[15]/input")

        ClickButton("/html/body/div[1]/div[4]/form/div[6]/div[6]/div/div/div/div[1]/div/span/button[2]")

        ClickButton("/html/body/div[1]/div[4]/form/div[6]/div[2]/div[4]/a[2]")

        RenameFile("Filial_ 1 _ Unidade_ 1 _ Período_ ", "manifestos emitidos")


    finally:
        # Fecha o navegador após a execução
        print("Manifestos emitidos finalizado")