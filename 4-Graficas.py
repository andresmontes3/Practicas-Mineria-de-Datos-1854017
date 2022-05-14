
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as img
import plotly.express as px
import os


df = pd.read_csv('./csv/olimpicos_limpio.csv')
df_medallas_equipo = pd.read_csv("csv/Practica3/medallas_equipo.csv")
df_medallas_equipo_total = pd.read_csv("csv/Practica3/medallas_equipo_total.csv")
df_medallas_mexico = pd.read_csv("csv/Practica3/medallas_mexico.csv")



if not os.path.exists("./graficas"):
        os.mkdir("./graficas")
if not os.path.exists("./graficas/Practica4"):
        os.mkdir("./graficas/Practica4")

plt.hist(df.drop_duplicates(keep="first",subset=["Nombre","Edad"])["Edad"], bins = [15,20,25,30,35,40,45,50,55,60])
plt.ylabel("Cantidad de jugadores")
plt.xlabel("Edad")
plt.savefig("./graficas/Practica4/edad_jugadores.png")
plt.show()


plt.title("Medallas de México en los Juegos Olímpicos")
plt.bar(df_medallas_mexico["Juegos"], df_medallas_mexico["Medallas"])
plt.xticks(rotation='vertical',fontsize=5)
plt.savefig("./graficas/Practica4/medallas_mexico.png")
plt.show()


df_medallas_equipo2 = df_medallas_equipo.sort_values(by=["Año"]).reset_index(drop=True)


fig = px.strip(df_medallas_equipo2, x="Año", y="Medallas", color="Equipo",hover_data=['Equipo','Juegos'])
fig.write_html('./graficas/Practica4/medallas_equipo_año.html', auto_open=True)
