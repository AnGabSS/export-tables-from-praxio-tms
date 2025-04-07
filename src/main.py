from time import sleep

from src.Login import Login
from src.Tables.Abastecimento import Abastecimento
from src.Tables.Afretamento import Afretamento
from src.Tables.Clientes import Clientes
from src.Tables.ContasAPagar import ContasAPagar
from src.Tables.ContasAReceber import ContasAReceber
from src.Tables.ContasBancarias import ContasBancarias
from src.Tables.DocumentosEmitidos import DocumentosEmitidos
from src.Tables.FaturamentoDeVeiculo import FaturamentoDeVeiculo
from src.Tables.ManifestosEmitidos import ManifestosEmitidos
from src.Tables.Manutencao import Manutencao
from src.Tables.Motoristas import Motoristas
from src.Tables.OrdemDeServico import OrdemDeServico
from src.Tables.Transporte import Transporte
from src.Tables.Veiculo import Veiculo


def main():
    Login()
    Afretamento()
    Clientes()
    ContasAPagar()
    ContasAReceber()
    ContasBancarias()
    Abastecimento()
    FaturamentoDeVeiculo()
    ManifestosEmitidos()
    Manutencao()
    Motoristas()
    OrdemDeServico()
    Transporte()
    Veiculo()
    DocumentosEmitidos()
    sleep(2000)

if __name__ == "__main__":
    main()