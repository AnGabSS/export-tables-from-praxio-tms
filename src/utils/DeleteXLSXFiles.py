import os
import glob
from dotenv import load_dotenv

def DeleteXLSXFiles():
    # Carrega variáveis de ambiente do .env
    load_dotenv()

    # Obtém o diretório de downloads a partir da variável de ambiente
    download_dir = os.environ.get("DOWNLOADS_PATH")

    if not download_dir or not os.path.isdir(download_dir):
        raise ValueError(f"Caminho inválido ou não definido em DOWNLOADS_PATH: {download_dir}")

    # Busca todos os arquivos .xlsx no diretório
    arquivos_xlsx = glob.glob(os.path.join(download_dir, "*.xlsx"))

    # Apaga os arquivos encontrados
    for arquivo in arquivos_xlsx:
        try:
            os.remove(arquivo)
            print(f"Arquivo removido: {arquivo}")
        except Exception as e:
            print(f"Erro ao remover {arquivo}: {e}")
