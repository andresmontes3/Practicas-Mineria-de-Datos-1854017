import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import matplotlib.pyplot as plt
import os
from datetime import datetime
#import pycountry

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

def analysis(df: pd.DataFrame):

    


    ##
    df["Juegos"] = df["Año"].astype(str) + " " + df["Temporada"]
    
    df["Año"] =[datetime.strptime(str(x),"%Y")for x in df["Año"]]
    #Debido a que no cuento con la fecha exacta, utilicé solo el año, es por
    #esto que no lo incluyo en DataCleaning
    
    #df["Fecha"] = [datetime.strptime("01"+x[:4],"%m%Y") if x[5:]=="Invierno"
       #         else datetime.strptime("07"+x[:4],"%m%Y") for x in df["Juegos"] ]

    print_tabulate(df.head(50))

    df = pd.get_dummies(df, drop_first=False, columns=['Medalla'])
    df = df.drop(['Medalla_Sin Medalla'], axis=1)
    ##

    if not os.path.exists("./csv/Practica3"):
        os.mkdir("./csv/Practica3")

    df_bronce_equipo = df.groupby(["Equipo", "Juegos","Año"])[["Medalla_Bronce"]].aggregate(pd.DataFrame.sum)
    print_tabulate(df_bronce_equipo.head(50))
    df_bronce_equipo.to_csv("csv/Practica3/bronce_equipo.csv")

    df_plata_equipo = df.groupby(["Equipo", "Juegos","Año"])[["Medalla_Plata"]].aggregate(pd.DataFrame.sum)
    print_tabulate(df_plata_equipo.head(50))
    df_plata_equipo.to_csv("csv/Practica3/plata_equipo.csv")
    
    df_oro_equipo = df.groupby(["Equipo", "Juegos","Año"])[["Medalla_Oro"]].aggregate(pd.DataFrame.sum)
    print_tabulate(df_oro_equipo.head(50))
    df_oro_equipo.to_csv("csv/Practica3/oro_equipo.csv")

    df_oro_equipo_total = df.groupby(["Equipo"])[["Medalla_Oro"]].aggregate(pd.DataFrame.sum)
    print_tabulate(df_oro_equipo_total.head(50))
    df_oro_equipo_total.to_csv("csv/Practica3/oro_equipo_total.csv")

    df_suma_medallas = df_bronce_equipo["Medalla_Bronce"]+df_plata_equipo["Medalla_Plata"]+df_oro_equipo["Medalla_Oro"]
    df_medallas_equipo = df_oro_equipo
    df_medallas_equipo["Medalla_Oro"] = df_suma_medallas
    df_medallas_equipo.rename(columns = {'Medalla_Oro':'Medallas'}, inplace = True)
    print_tabulate(df_medallas_equipo.head(50))
    df_medallas_equipo.to_csv("csv/Practica3/medallas_equipo.csv")


    df_medallas_equipo_total = df_medallas_equipo.groupby(["Equipo"])[["Medallas"]].aggregate(pd.DataFrame.sum)
    print_tabulate(df_medallas_equipo_total.head(50))
    df_medallas_equipo_total.to_csv("csv/Practica3/medallas_equipo_total.csv")

    df_medallas_equipo = pd.read_csv("csv/Practica3/medallas_equipo.csv")
    df_medallas_mexico = df_medallas_equipo[df_medallas_equipo["Equipo"]=="Mexico"]
    
    
    print_tabulate(df_medallas_mexico.head(50))
    df_medallas_mexico.to_csv("csv/Practica3/medallas_mexico.csv",index=False)


    df_edad_mean = df.dropna(subset=["Edad"])
    df_edad_mean = df_edad_mean.drop_duplicates(keep="first",subset=["Nombre","Edad"])
    df_edad_mean = df_edad_mean.groupby(["Juegos"])[["Edad"]].aggregate(pd.DataFrame.mean)
    print_tabulate(df_edad_mean.head(50))
    df_edad_mean.to_csv("csv/Practica3/edad_mean.csv")

    df_mexico = df[df["Equipo"]=="Mexico"]
    df_mexico_deportes_oro = df_mexico.groupby(["Deporte"])[["Medalla_Oro"]].aggregate(pd.DataFrame.sum)
    df_mexico_deportes_plata = df_mexico.groupby(["Deporte"])[["Medalla_Plata"]].aggregate(pd.DataFrame.sum)
    df_mexico_deportes_bronce = df_mexico.groupby(["Deporte"])[["Medalla_Bronce"]].aggregate(pd.DataFrame.sum)

    df_mexico_deportes_medallas = df_mexico_deportes_oro
    df_mexico_deportes_medallas["Medalla_Plata"] = df_mexico_deportes_plata["Medalla_Plata"]
    df_mexico_deportes_medallas["Medalla_Bronce"] = df_mexico_deportes_bronce["Medalla_Bronce"]

    df_mexico_deportes_medallas["Total"] = df_mexico_deportes_oro["Medalla_Oro"]+df_mexico_deportes_plata["Medalla_Plata"]+df_mexico_deportes_bronce["Medalla_Bronce"]

    print_tabulate(df_mexico_deportes_medallas)
    df_mexico_deportes_medallas.to_csv("csv/Practica3/mexico_deportes_medallas.csv")

    df_medallas_oro_edad = df.dropna(subset=["Edad"]).groupby(["Edad"])[["Medalla_Oro"]].aggregate(pd.DataFrame.sum)
    
    print_tabulate(df_medallas_oro_edad)
    df_medallas_oro_edad.to_csv("csv/Practica3/medallas_oro_edad.csv")




    df_max_edad = df.dropna(subset=["Edad"])
    df_max_edad = df.groupby(["Equipo"])[["Edad"]].max()
    df_max_edad = df_max_edad.dropna(subset=["Edad"])
    print_tabulate(df_max_edad.head(50))
    df_max_edad.to_csv("csv/Practica3/max_edad.csv")

    df_min_edad = df.dropna(subset=["Edad"])
    df_min_edad = df.groupby(["Equipo"])[["Edad"]].min()
    df_min_edad = df_min_edad.dropna(subset=["Edad"])
    print_tabulate(df_min_edad.head(50))
    df_min_edad.to_csv("csv/Practica3/min_edad.csv")


    

    

    moda_edad = df.dropna(subset=["Edad"]).drop_duplicates(keep="first",subset=["Nombre","Edad"]) #Para eliminar valores nulos y jugadores repetidos
    moda_edad = moda_edad["Edad"].mode()[0]
    print(f"\nLa moda de las edades es de: {moda_edad}")

    varianza_edad = df.dropna(subset=["Edad"]).drop_duplicates(keep="first",subset=["Nombre","Edad"])
    varianza_edad = varianza_edad["Edad"].var()
    print(f"\nLa varianza de las edades es de: {varianza_edad}")

    desviacionestandar_edad = df.dropna(subset=["Edad"]).drop_duplicates(keep="first",subset=["Nombre","Edad"])
    desviacionestandar_edad = desviacionestandar_edad["Edad"].std()
    print(f"\nLa desviacion estandar de las edades es de: {desviacionestandar_edad}")

    curtosis_edad = df.dropna(subset=["Edad"]).drop_duplicates(keep="first",subset=["Nombre","Edad"])
    curtosis_edad = curtosis_edad["Edad"].kurtosis()
    print(f"\nLa curtosis de las edades es de: {curtosis_edad}")

    
    df_jugadores_oro_mx = df_mexico.groupby(["Nombre","Genero"])[["Medalla_Oro"]].aggregate(pd.DataFrame.sum)
    df_jugadores_plata_mx = df_mexico.groupby(["Nombre","Genero"])[["Medalla_Plata"]].aggregate(pd.DataFrame.sum)
    df_jugadores_bronce_mx = df_mexico.groupby(["Nombre","Genero"])[["Medalla_Bronce"]].aggregate(pd.DataFrame.sum)

    df_jugadores_medallas_mx = df_jugadores_oro_mx

    df_jugadores_medallas_mx["Medallas"] = df_jugadores_bronce_mx["Medalla_Bronce"]+df_jugadores_plata_mx["Medalla_Plata"]+df_jugadores_oro_mx["Medalla_Oro"]
    df_jugadores_medallas_mx = df_jugadores_medallas_mx.drop(['Medalla_Oro'], axis=1)

    print_tabulate(df_jugadores_medallas_mx.head(100))
    df_jugadores_medallas_mx.to_csv("csv/Practica3/jugadores_medallas_mx.csv")

    

   

    df_jugadores_oro = df.groupby(["Nombre","Equipo"])[["Medalla_Oro"]].aggregate(pd.DataFrame.sum)
    df_jugadores_plata = df.groupby(["Nombre","Equipo"])[["Medalla_Plata"]].aggregate(pd.DataFrame.sum)
    df_jugadores_bronce = df.groupby(["Nombre","Equipo"])[["Medalla_Bronce"]].aggregate(pd.DataFrame.sum)

    df_jugadores_medallas = df_jugadores_oro

    df_jugadores_medallas["Medallas"] = df_jugadores_bronce["Medalla_Bronce"]+df_jugadores_plata["Medalla_Plata"]+df_jugadores_oro["Medalla_Oro"]
    df_jugadores_medallas = df_jugadores_medallas.drop(['Medalla_Oro'], axis=1)

    print_tabulate(df_jugadores_medallas.head(100))
    df_jugadores_medallas.to_csv("csv/Practica3/jugadores_medallas.csv")
   


    
    
df = pd.read_csv('./csv/olimpicos_limpio.csv')
analysis(df)