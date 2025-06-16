from src.GoToTable import GoToTable
from src.utils.ClickButton import ClickButton
from src.utils.RenameFile import RenameFile


def Fornecedores():
    GoToTable("Fornecedor", "/html/body/div[1]/div[4]/form/div[4]/div[2]/section[2]/div[1]/ul/li[5]/h3/a")
    try:

        ClickButton("/html/body/div[1]/div[4]/form/div[5]/div[1]/div[2]/div/div[2]/div[4]/a[2]")

        RenameFile("Fornecedores", "fornecedores")
    finally:
        # Fecha o navegador após a execução
        print("Fornecedores finalizado")