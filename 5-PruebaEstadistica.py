import pandas as pd
import matplotlib.pyplot as plt
import os
import statsmodels.api as sm
from statsmodels.formula.api import ols
import plotly.express as px


if not os.path.exists("./graficas/Practica5"):
    os.mkdir("./graficas/Practica5")


df_medallas_equipo = pd.read_csv("./csv/Practica3/medallas_equipo.csv")

fig = px.violin(df_medallas_equipo, x="Equipo", y="Medallas", color="Equipo",box=True,points='all',hover_data=['Juegos'])
fig.write_html('./graficas/Practica5/medallas_equipo.html', auto_open=True)

df_medallas_equipo = df_medallas_equipo.drop(['Juegos'], axis=1)
df_medallas_equipo = df_medallas_equipo.drop(['Año'], axis=1)

#Dataframe de las medallas conseguidas por cada equipo


modl = ols("Medallas ~ Equipo", data=df_medallas_equipo).fit()
anova_df = sm.stats.anova_lm(modl, typ=2)
if anova_df["PR(>F)"][0] < 0.005:
    print("\nSi hay diferencias en el número de medallas ganadas")
else:
    print("\nNo hay diferencias en el número de medallas ganadas")
print(anova_df)