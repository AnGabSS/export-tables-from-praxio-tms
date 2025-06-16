from time import sleep

from src.Login import Login
from src.Tables.Abastecimento import Abastecimento
from src.Tables.AcertoDeViagem import AcertoDeViagem
from src.Tables.AdiantamentoDiaria import AdiantamentoDiaria
from src.Tables.Afretamento import Afretamento
from src.Tables.Clientes import Clientes
from src.Tables.ColetasEmitidas import ColetasEmitidas
from src.Tables.ContasAPagar import ContasAPagar
from src.Tables.ContasAReceber import ContasAReceber
from src.Tables.ContasBancarias import ContasBancarias
from src.Tables.Disponibilidade import Disponibilidade
from src.Tables.DocumentosEmitidos import DocumentosEmitidos
from src.Tables.FaturamentoDeVeiculo import FaturamentoDeVeiculo
from src.Tables.Fornecedor import Fornecedores
from src.Tables.ManifestoEletronico import ManifestoEletronico
from src.Tables.ManifestosEmitidos import ManifestosEmitidos
from src.Tables.Manutencao import Manutencao
from src.Tables.Motoristas import Motoristas
from src.Tables.OrdemDeServico import OrdemDeServico
from src.Tables.PEF import PEF
from src.Tables.PosicaoOrdemServico import PosicaoOrdemServico
from src.Tables.Transporte import Transporte
from src.Tables.ValePedagio import ValePedagio
from src.Tables.Veiculo import Veiculo
from src.utils.DeleteCSVandCRDOWNLOADFiles import deleteCSVandCRDOWNLOADFiles
from utils.DeleteXLSXFiles import DeleteXLSXFiles


def main():
    Login()
    DeleteXLSXFiles()
    AcertoDeViagem()
    Afretamento()
    Clientes()
    Fornecedores()
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
    ValePedagio()
    PEF()
    ManifestoEletronico()
    PosicaoOrdemServico()
    ColetasEmitidas()
    AdiantamentoDiaria()
    Disponibilidade()
    deleteCSVandCRDOWNLOADFiles()


if __name__ == "__main__":
    main()