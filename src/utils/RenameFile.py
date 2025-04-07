import os
import time

from src.WebDriver import download_dir


def RenameFile(oldName, newName, max_wait_time=60):
    start_time = time.time()
    downloaded_file = None

    while time.time() - start_time < max_wait_time:
        # Listar arquivos no diretório de download
        files = os.listdir(download_dir)

        # Procurar arquivo com a substring desejada
        for file in files:
            if oldName in file:
                downloaded_file = os.path.join(download_dir, file)
                break

        if downloaded_file:
            break

        time.sleep(1)

    if downloaded_file:
        # Extrair a extensão do arquivo original
        file_ext = os.path.splitext(downloaded_file)[1]

        # Criar novo nome com data atual
        new_filename = f"{newName}{file_ext}"
        new_filepath = os.path.join(download_dir, new_filename)

        # Renomear o arquivo
        os.rename(downloaded_file, new_filepath)
        print(f"Arquivo renomeado para: {new_filename}")
    else:
        print("Não foi possível renomear o arquivo")