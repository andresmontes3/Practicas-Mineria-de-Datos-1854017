import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import matplotlib.pyplot as plt


def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

def analysis(df: pd.DataFrame):
    df["Juegos"] = df["Año"].astype(str) + " " + df["Temporada"]

    df = pd.get_dummies(df, drop_first=False, columns=['Medalla'])
    df = df.drop(['Medalla_Sin Medalla'], axis=1)
    

    df_bronce_equipo = df.groupby(["Equipo", "Juegos"])[["Medalla_Bronce"]].aggregate(pd.DataFrame.sum)
    print_tabulate(df_bronce_equipo.head(50))

    df_plata_equipo = df.groupby(["Equipo", "Juegos"])[["Medalla_Plata"]].aggregate(pd.DataFrame.sum)
    print_tabulate(df_plata_equipo.head(50))
    
    df_oro_equipo = df.groupby(["Equipo", "Juegos"])[["Medalla_Oro"]].aggregate(pd.DataFrame.sum)
    print_tabulate(df_oro_equipo.head(50))

    df_edad_mean = df.dropna(subset=["Edad"])
    df_edad_mean = df_edad_mean.drop_duplicates(keep="first",subset=["Nombre","Edad"])
    df_edad_mean = df_edad_mean.groupby(["Juegos"])[["Edad"]].aggregate(pd.DataFrame.mean)
    print_tabulate(df_edad_mean.head(50))

    df_mexico = df[df["Equipo"]=="Mexico"]
    df_mexico_deportes_oro = df_mexico.groupby(["Deporte"])[["Medalla_Oro"]].aggregate(pd.DataFrame.sum)
    print_tabulate(df_mexico_deportes_oro)
    
    

df = pd.read_csv('./csv/olimpicos_limpio.csv')
analysis(df)