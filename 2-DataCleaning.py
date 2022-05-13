
import pandas as pd


def clean_data(df):
    

    df = df.drop(['Games'], axis=1)
    df = df.drop(['Unnamed: 0'], axis=1)

    df.columns = ['Nombre','Genero','Edad','Equipo','Año','Temporada','Deporte','Medalla']

    df.loc[df["Medalla"] == 0, "Medalla"] = "Sin Medalla"
    df.loc[df["Medalla"] == 1, "Medalla"] = "Bronce"
    df.loc[df["Medalla"] == 2, "Medalla"] = "Plata"
    df.loc[df["Medalla"] == 3, "Medalla"] = "Oro"

    df.loc[df["Temporada"] == "Summer", "Temporada"] = "Verano"
    df.loc[df["Temporada"] == "Winter", "Temporada"] = "Invierno"
    
    df.loc[df["Genero"] == "M", "Genero"] = "Masculino"
    df.loc[df["Genero"] == "F", "Genero"] = "Femenino"
    
    return df


df = pd.read_csv('./csv/All Year Olympic Dataset (with 2020 Tokyo Olympics).csv')
df = clean_data(df)

df.to_csv("csv/olimpicos_limpio.csv", index=False)