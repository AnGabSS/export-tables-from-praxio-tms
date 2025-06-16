import os
import time
import pandas as pd
import zipfile
from src.WebDriver import download_dir


def RenameFile(oldName, newName, max_wait_time=1680):
    start_time = time.time()
    downloaded_file = None

    while time.time() - start_time < max_wait_time:
        files = os.listdir(download_dir)

        for file in files:
            if oldName in file:
                # Se o arquivo ainda está sendo baixado
                if file.endswith('.crdownload'):
                    print(f"Arquivo {file} ainda está sendo baixado. Aguardando 10 segundos...")
                    time.sleep(10)
                    break  # Sai do for para reler a lista de arquivos após aguardar
                else:
                    downloaded_file = os.path.join(download_dir, file)
                    break

        if downloaded_file:
            break

        time.sleep(1)

    if not downloaded_file:
        print("Não foi possível encontrar o arquivo para renomear")
        return

    file_ext = os.path.splitext(downloaded_file)[1].lower()

    try:
        if file_ext == '.zip':
            with zipfile.ZipFile(downloaded_file, 'r') as zip_ref:
                file_list = zip_ref.namelist()
                csv_file = next((f for f in file_list if f.lower().endswith('.csv')), None)

                if not csv_file:
                    print("Nenhum arquivo CSV encontrado no arquivo ZIP")
                    return

                zip_ref.extract(csv_file, download_dir)
                extracted_csv = os.path.join(download_dir, csv_file)

                df = pd.read_csv(extracted_csv, sep=';')
                new_filepath = os.path.join(download_dir, f"{newName}.xlsx")
                df.to_excel(new_filepath, index=False)

                os.remove(extracted_csv)
                os.remove(downloaded_file)
                print(f"Arquivo ZIP extraído, CSV convertido e renomeado para: {newName}.xlsx")

        elif file_ext == '.csv':
            df = pd.read_csv(downloaded_file, sep=';')
            new_filepath = os.path.join(download_dir, f"{newName}.xlsx")
            df.to_excel(new_filepath, index=False)
            os.remove(downloaded_file)
            print(f"Arquivo CSV convertido e renomeado para: {newName}.xlsx")

        else:
            new_filepath = os.path.join(download_dir, f"{newName}{file_ext}")
            os.rename(downloaded_file, new_filepath)
            print(f"Arquivo renomeado para: {newName}{file_ext}")

    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo: {str(e)}")
        if os.path.exists(downloaded_file):
            os.remove(downloaded_file)
