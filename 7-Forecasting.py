from datetime import datetime
import os
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
from tabulate import tabulate
from statsmodels.stats.outliers_influence import summary_table
from typing import Tuple, Dict
import numpy as np


def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt="orgtbl"))

def linear_regression(df,x,y):
    model= sm.OLS(df[y],sm.add_constant(df_usa_año_int)).fit()
    print(model.summary())

    bands = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]
    coef = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef']
    
    m=coef.values[1]
    b=coef.values[0]
    print(bands)
    low=bands['[0.025'][0]
    high=bands['0.975]'][0]

    df.plot(x=x,y=y, kind='scatter')
    plt.plot(df[x],[ m * x + b for _, x in df_usa_año_int.items()], color="green")
    plt.fill_between(df[x],
                     [ m * x  + low for _, x in df_usa_año_int.items()],
                     [ m * x + high for _, x in df_usa_año_int.items()], alpha=0.2, color="blue")

    plt.title("Forecasting: Medallas de oro de Estados Unidos")
    plt.xticks(rotation='vertical',fontsize=5)
    if not os.path.exists("./graficas/Practica7"):
        os.mkdir("./graficas/Practica7")
    plt.savefig("./graficas/Practica7/Forecasting.png")
    plt.show()
    plt.close()

df = pd.read_csv('./csv/olimpicos_limpio.csv')


df = pd.get_dummies(df, drop_first=False, columns=['Medalla'])
df = df.drop(['Medalla_Sin Medalla'], axis=1)

df_usa = df[df["Equipo"]=="United States"]
df_usa = df_usa.groupby(["Año"])[["Medalla_Oro"]].aggregate(pd.DataFrame.sum)
if not os.path.exists("./csv/Practica7"):
    os.mkdir("./csv/Practica7")
df_usa.to_csv("csv/Practica7/usa_año_medallas_oro.csv")
df_usa = pd.read_csv("./csv/Practica7/usa_año_medallas_oro.csv")

df_usa_año_int = df_usa["Año"] 
#Almaceno los años como enteros para usar como los valores de X en la gráfica más adelante
df_usa["Año"] =[datetime.strptime(str(x),"%Y")for x in df_usa["Año"]]

linear_regression(df_usa, "Año", "Medalla_Oro")