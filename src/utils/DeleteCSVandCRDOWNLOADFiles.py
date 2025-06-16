import os
from pathlib import Path
from dotenv import load_dotenv


def delete_files_by_extension(directory: Path, extensions: list[str]) -> None:
    """Remove arquivos no diretório especificado com as extensões informadas."""
    for ext in extensions:
        for file in directory.glob(f"*.{ext}"):
            try:
                file.unlink()
                print(f"Arquivo removido: {file}")
            except Exception as e:
                print(f"Erro ao remover {file}: {e}")


def deleteCSVandCRDOWNLOADFiles():
    """Carrega o diretório de downloads e remove arquivos .csv e .crdownload."""
    load_dotenv()

    download_path = os.getenv("DOWNLOADS_PATH")
    if not download_path:
        raise ValueError("A variável de ambiente DOWNLOADS_PATH não está definida.")

    download_dir = Path(download_path)
    if not download_dir.is_dir():
        raise ValueError(f"Caminho inválido: {download_dir}")

    delete_files_by_extension(download_dir, ["csv", "crdownload"])