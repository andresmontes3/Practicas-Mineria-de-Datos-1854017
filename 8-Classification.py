import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import mode

df = pd.read_csv("./csv/olimpicos_limpio.csv")
df = pd.get_dummies(df, drop_first=False, columns=['Medalla'])

df_mx = df[df["Equipo"]=="Mexico"]
df_usa = df[df["Equipo"]=="United States"]

df_mx = df_mx.groupby(["Año"])[["Medalla_Oro"]].aggregate(pd.DataFrame.sum)
df_usa = df_usa.groupby(["Año"])[["Medalla_Oro"]].aggregate(pd.DataFrame.sum)

if not os.path.exists("./csv/Practica8"):
    os.mkdir("./csv/Practica8")

df_mx.to_csv("csv/Practica8/mx_año_medallas_oro.csv")
df_usa.to_csv("csv/Practica8/usa_año_medallas_oro.csv")


df_mx = pd.read_csv("./csv/Practica8/mx_año_medallas_oro.csv")
df_usa = pd.read_csv("./csv/Practica8/usa_año_medallas_oro.csv")

#Genero un df de Mexico y Estados Unidos con las medallas de oro ganadas
#por cada año, luego los concateno con la etiqueta de su nombre de país
#para poder enviar los puntos al KNN y clasificar las entradas como
#México o Estados Unidos

df_mx["Pais"]=["Mexico" for x in df_mx["Año"]]
df_usa["Pais"]=["Estados Unidos" for x in df_usa["Año"]]

df = pd.concat([df_mx, df_usa], ignore_index=True)

#df.drop(df[df['Medalla_Oro'] == 0].index, inplace = True)

print(df)

plt.scatter(df_mx["Año"], df_mx["Medalla_Oro"], c='red', label ='Mexico')
plt.scatter(df_usa["Año"], df_usa["Medalla_Oro"], c='blue', label ='Estados Unidos')
plt.ylabel("Medallas de Oro")
plt.xlabel("Año")
plt.legend()

def distancia_euclidiana(p1: np.array, p2: np.array):
    return np.sqrt(np.sum((p2 - p1) ** 2))


def KNN(points, labels,input_data,k):
    #print(points)
    #print(labels)
    input_distances = [
        [distancia_euclidiana(input_point, point) for point in points]
        for input_point in input_data
    ]
    points_k_nearest = [
        np.argsort(input_point_dist)[:k] for input_point_dist in input_distances
    ]
    return [
        mode([labels[index] for index in point_nearest])
        for point_nearest in points_k_nearest
    ]




list_t = [
    (np.array(tuples[0:2]), tuples[2])
    for tuples in df.itertuples(index=False, name=None)
]
points = [point for point, _ in list_t]
labels = [label for _, label in list_t]


kn = KNN(
    points,
    labels,
    [np.array([2020, 90]), np.array([2016, 5]), np.array([2000, 0])],4)
print(kn) 
#Clasifica como Estados Unidos la primer entrada y como
#México las siguientes 2 por tener menos medallas

plt.scatter([2020,2016,2000], [90,5,0], c='yellow', label ='Entradas')
plt.title("Clasificación México o Estados Unidos en los Juegos Olímpicos")
if not os.path.exists("./graficas/Practica8"):
        os.mkdir("./graficas/Practica8")

plt.savefig("./graficas/Practica8/medallas_oro_mx_usa.png")
plt.show()