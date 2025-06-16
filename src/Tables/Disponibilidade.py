from src.GoToTable import GoToTable
from src.utils.ClickButton import ClickButton
from src.utils.RenameFile import RenameFile
from src.utils.WaitLoadPage import WaitLoadPage


def Disponibilidade():
    GoToTable("Disponibilidade")
    try:
        WaitLoadPage()
        ClickButton("/html/body/div[1]/div[4]/form/div[5]/div[1]/div[2]/div[1]/div/ul/li[2]")
        ClickButton("/html/body/div[1]/div[4]/form/div[5]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/a[2]")
        RenameFile("Planejamento de Cargas X Veiculos - Documentos", "disponibilidade")
    finally:
        # Fecha o navegador após a execução
        print("Disponibilidade finalizada")