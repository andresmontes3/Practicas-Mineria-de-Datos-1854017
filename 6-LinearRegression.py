import numbers
import pandas as pd
import os
import matplotlib.pyplot as plt
from datetime import datetime
from tabulate import tabulate
import statsmodels.api as sm

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))


def transform_dates(df,x):
    if isinstance(df[x][0], numbers.Number):
        return df[x]
    else:
        return df_usa_año_int

def linear_regression(df,x,y):

    fixed_x = transform_dates(df, x)
    model= sm.OLS(df[y],sm.add_constant(fixed_x)).fit()
    print(model.summary())
    print(fixed_x)
    coef = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef']
    df.plot(x=x,y=y, kind='scatter')
    plt.plot(df[x],[pd.DataFrame.mean(df[y]) for _ in fixed_x.items()], color='green')
    plt.plot(df[x],[ coef.values[1] * x + coef.values[0] for _, x in fixed_x.items()], color='red')
    plt.title("Regresion Lineal: Medallas de oro de Estados Unidos")
    plt.xticks(rotation='vertical',fontsize=5)
    if not os.path.exists("./graficas/Practica6"):
        os.mkdir("./graficas/Practica6")
    plt.savefig("./graficas/Practica6/LR.png")
    plt.show()
    plt.close()

df = pd.read_csv('./csv/olimpicos_limpio.csv')
#df["Juegos"] = df["Año"].astype(str) + " " + df["Temporada"]

df = pd.get_dummies(df, drop_first=False, columns=['Medalla'])
df = df.drop(['Medalla_Sin Medalla'], axis=1)

df_usa = df[df["Equipo"]=="United States"]
df_usa = df_usa.groupby(["Año"])[["Medalla_Oro"]].aggregate(pd.DataFrame.sum)
if not os.path.exists("./csv/Practica6"):
    os.mkdir("./csv/Practica6")
df_usa.to_csv("csv/Practica6/usa_año_medallas_oro.csv")
df_usa = pd.read_csv("./csv/Practica6/usa_año_medallas_oro.csv")

print_tabulate(df_usa.head(50))

#años = [x in range(df_usa["Año"].min(),df_usa["Año"].max()),1]
#print(años)

df_usa_año_int = df_usa["Año"] 
#Almaceno los años como enteros para usar como los valores de X en la gráfica más adelante
df_usa["Año"] =[datetime.strptime(str(x),"%Y")for x in df_usa["Año"]]






linear_regression(df_usa, "Año", "Medalla_Oro")