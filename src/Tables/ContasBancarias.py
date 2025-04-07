from src.GoToTable import GoToTable
from src.utils.ClickButton import ClickButton
from src.utils.RenameFile import RenameFile
from src.utils.WaitLoadPage import WaitLoadPage


def ContasBancarias():
    GoToTable("Contas Bancárias")
    try:
        WaitLoadPage()
        ClickButton("/html/body/div[1]/div[4]/form/div[5]/div[1]/div[2]/div/div[2]/div[4]/a[1]")
        RenameFile("Contas", "contas bancarias")
    finally:
        # Fecha o navegador após a execução
        print("Contas Bancarias finalizada")