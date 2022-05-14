import numbers
import pandas as pd
import os
import matplotlib.pyplot as plt
from datetime import datetime
from tabulate import tabulate
import statsmodels.api as sm

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))




def linear_regression(df,x,y):

    model= sm.OLS(df[y],sm.add_constant(df_usa_año_int)).fit()
    print(model.summary())

    coef = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef']
    df.plot(x=x,y=y, kind='scatter')
    plt.plot(df[x],[pd.DataFrame.mean(df[y]) for _ in df_usa_año_int.items()], color='green')
    plt.plot(df[x],[ coef.values[1] * x + coef.values[0] for _, x in df_usa_año_int.items()], color='red')
    plt.title("Regresion Lineal: Medallas de oro de Estados Unidos")
    plt.xticks(rotation='vertical',fontsize=5)
    if not os.path.exists("./graficas/Practica6"):
        os.mkdir("./graficas/Practica6")
    plt.savefig("./graficas/Practica6/LR.png")
    plt.show()
    plt.close()

df = pd.read_csv('./csv/olimpicos_limpio.csv')


df = pd.get_dummies(df, drop_first=False, columns=['Medalla'])
df = df.drop(['Medalla_Sin Medalla'], axis=1)

df_usa = df[df["Equipo"]=="United States"]
df_usa = df_usa.groupby(["Año"])[["Medalla_Oro"]].aggregate(pd.DataFrame.sum)
if not os.path.exists("./csv/Practica6"):
    os.mkdir("./csv/Practica6")
df_usa.to_csv("csv/Practica6/usa_año_medallas_oro.csv")
df_usa = pd.read_csv("./csv/Practica6/usa_año_medallas_oro.csv")



df_usa_año_int = df_usa["Año"] 
#Almaceno los años como enteros para usar como los valores de X en la gráfica más adelante
df_usa["Año"] =[datetime.strptime(str(x),"%Y")for x in df_usa["Año"]]


linear_regression(df_usa, "Año", "Medalla_Oro")