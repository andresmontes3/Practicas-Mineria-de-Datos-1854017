import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("./csv/olimpicos_limpio.csv")
df = pd.get_dummies(df, drop_first=False, columns=['Medalla'])

df_mx = df[df["Equipo"]=="Mexico"]
df_usa = df[df["Equipo"]=="United States"]

df_mx = df_mx.groupby(["Año"])[["Medalla_Oro"]].aggregate(pd.DataFrame.sum)
df_usa = df_usa.groupby(["Año"])[["Medalla_Oro"]].aggregate(pd.DataFrame.sum)

if not os.path.exists("./csv/Practica9"):
    os.mkdir("./csv/Practica9")

df_mx.to_csv("csv/Practica9/mx_año_medallas_oro.csv")
df_usa.to_csv("csv/Practica9/usa_año_medallas_oro.csv")

df_mx = pd.read_csv("./csv/Practica9/mx_año_medallas_oro.csv")
df_usa = pd.read_csv("./csv/Practica9/usa_año_medallas_oro.csv")

#Genero un df de Mexico y Estados Unidos con las medallas de oro ganadas
#por cada año, luego los concateno con la etiqueta de su nombre de país

#Este algoritmo agrupa los datos, y para este caso utilicé
#solo la información de estos dos países para que se
#visualizara de manera mas clara, aunque en otro tipo de
#conjuntos de datos se puede observar mejor su funcionamiento

df_mx["Pais"]=["Mexico" for x in df_mx["Año"]]
df_usa["Pais"]=["Estados Unidos" for x in df_usa["Año"]]

df = pd.concat([df_mx, df_usa], ignore_index=True)


print(df)


def distancia_euclidiana(p1: np.array, p2: np.array):
    return np.sqrt(np.sum((p2 - p1) ** 2))


def k_means(points,k):
    DIM = len(points[0])
    N = len(points)
    num_cluster = k
    iterations = 15

    x = np.array(points)
    y = np.random.randint(0, num_cluster, N)

    mean = np.zeros((num_cluster, DIM))
    for t in range(iterations):
        for k in range(num_cluster):
            mean[k] = np.mean(x[y == k], axis=0)
        for i in range(N):
            dist = np.sum((mean - x[i]) ** 2, axis=1)
            pred = np.argmin(dist)
            y[i] = pred

    for kl in range(num_cluster):
        xp = x[y == kl, 0]
        yp = x[y == kl, 1]
        plt.scatter(xp, yp)
    if not os.path.exists("./graficas/Practica9"):
        os.mkdir("./graficas/Practica9")
    plt.savefig("./graficas/Practica9/kmeans.png")
    plt.ylabel("Medallas de Oro")
    plt.xlabel("Año")
    plt.show()
    plt.close()
    return mean




list_t = [
    (np.array(tuples[0:2]), tuples[2])
    for tuples in df.itertuples(index=False, name=None)
]
points = [point for point, _ in list_t]
labels = [label for _, label in list_t]



print(k_means(points,2))  
#Se elige 2 por que es la cantidad de países real, aunque si se desconocen
#los grupos originales se puede usar un algoritmo para obetener el mejor valor para utilizar,
#como el método del "codo"



'''
plt.scatter([2020,2016,2000], [90,5,0], c='yellow', label ='Entradas')
plt.title("Clasificación México o Estados Unidos en los Juegos Olímpicos")
if not os.path.exists("./graficas/Practica8"):
        os.mkdir("./graficas/Practica8")

plt.savefig("./graficas/Practica8/medallas_oro_mx_usa.png")
plt.show()
'''
