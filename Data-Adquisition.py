
import kaggle
import os
from zipfile import ZipFile

from kaggle.api.kaggle_api_extended import KaggleApi
try:
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('fearsomejockey/olympics-dataset-2020-tokyo-dataset',path="./csv")
    print("Descarga finalizada")
except:
    print("Error al descargar dataset")
    pass


try:
    with ZipFile('./csv/olympics-dataset-2020-tokyo-dataset.zip', 'r') as zip:
        zip.extractall('./csv')
    print("Extracción finalizada") 
except:
    print("Error al descomprimir zip")
    pass
  

try:
    os.remove('./csv/olympics-dataset-2020-tokyo-dataset.zip')
except:
    print("Error al eliminar zip")
    pass
