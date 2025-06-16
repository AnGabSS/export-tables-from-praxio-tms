from src.GoToTable import GoToTable
from src.utils.ClickButton import ClickButton
from src.utils.RenameFile import RenameFile


def FaturamentoDeVeiculo():
    GoToTable("Meta de Faturamento por Veículo")
    try:

        ClickButton("/html/body/div[1]/div[4]/form/div[1]/div[2]/div[1]/div[1]/div[5]/div/select/option[4]")

        ClickButton("/html/body/div[1]/div[4]/form/div[1]/div[2]/div[1]/div[1]/div[7]/div/select/option[2]")

        ClickButton("/html/body/div[1]/div[4]/form/div[1]/div[2]/div[1]/div[1]/div[11]/div/select/option[4]")

        ClickButton("/html/body/div[1]/div[4]/form/div[1]/div[2]/div[1]/div[1]/div[12]/input")

        ClickButton("/html/body/div[1]/div[4]/form/div[6]/div[2]/div[4]/a[2]")

        RenameFile("Consulta - Meta de Faturamento por Veículo", "faturamento de veiculo")


    finally:
        # Fecha o navegador após a execução
        print("Faturamento de veículo finalizado")