
import kaggle
import os
from zipfile import ZipFile
import pandas as pd
from tabulate import tabulate

from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset(url,dst):
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(url,path=dst)


def csv_unzip(src,dst):
    with ZipFile(src, 'r') as zip:
        zip.extractall(dst)

def df_from_csv(path):
    return pd.read_csv(path)

def clean_data(df):
    

    df = df.drop(['Games'], axis=1)
    df = df.drop(['Unnamed: 0'], axis=1)

    df.columns = ['Nombre','Genero','Edad','Equipo','Año','Temporada','Deporte','Medalla']

    df.loc[df["Medalla"] == 0, "Medalla"] = "Sin Medallala"
    df.loc[df["Medalla"] == 1, "Medalla"] = "Bronce"
    df.loc[df["Medalla"] == 2, "Medalla"] = "Plata"
    df.loc[df["Medalla"] == 3, "Medalla"] = "Oro"

    df.loc[df["Temporada"] == "Summer", "Temporada"] = "Verano"
    df.loc[df["Temporada"] == "Winter", "Temporada"] = "Invierno"

    return df

def print_tabulate(df):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))


if not os.path.isfile('./csv/All Year Olympic Dataset (with 2020 Tokyo Olympics).csv'):
    download_dataset('fearsomejockey/olympics-dataset-2020-tokyo-dataset','./')
    csv_unzip('./olympics-dataset-2020-tokyo-dataset.zip','./csv')
    os.remove('./olympics-dataset-2020-tokyo-dataset.zip')
df = df_from_csv('./csv/All Year Olympic Dataset (with 2020 Tokyo Olympics).csv')
df = clean_data(df)

#print_tabulate(df)
df.to_csv("csv/olimpicos_limpio.csv", index=False)
