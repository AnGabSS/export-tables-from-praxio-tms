from src.GoToTable import GoToTable
from src.utils.ClickButton import ClickButton
from src.utils.PutInitialDate import PutInitialDate
from src.utils.RenameFile import RenameFile


def Manutencao():
    GoToTable("Histórico de Gastos com Manutenção")
    try:

        PutInitialDate("/html/body/div[1]/div[4]/form/div[1]/div[2]/div/div[1]/div[5]/div/div/div/input[1]")

        ClickButton("/html/body/div[1]/div[4]/form/div[1]/div[2]/div[1]/div[1]/div[17]/input")

        ClickButton("/html/body/div[1]/div[4]/form/div[6]/div[6]/div/div/div/div[1]/div/span/button[2]")

        ClickButton("/html/body/div[1]/div[4]/form/div[6]/div[2]/div[4]/a[1]")

        RenameFile("Veículo_  _ Tipo de Documento_ Todos _ Grupo de Produto_  _ Tipo de Frota_ Todas", "manutencao")


    finally:
        # Fecha o navegador após a execução
        print("Manutenção finalizada")