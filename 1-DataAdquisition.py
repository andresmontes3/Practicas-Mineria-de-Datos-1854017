
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

    



def print_tabulate(df):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))


if not os.path.isfile('./csv/All Year Olympic Dataset (with 2020 Tokyo Olympics).csv'):
    download_dataset('fearsomejockey/olympics-dataset-2020-tokyo-dataset','./')
    csv_unzip('./olympics-dataset-2020-tokyo-dataset.zip','./csv')
    os.remove('./olympics-dataset-2020-tokyo-dataset.zip')


#print_tabulate(df)

