import pandas as pd
import os
import chardet

RUTA = os.path.join(os.getcwd(), "inventario3.csv")

raw = open(RUTA, 'rb').read()
encoding = chardet.detect(raw)['encoding']

df = pd.read_csv(RUTA, encoding='utf-8')

""" # buscar loc y iloc
resultado = df.loc[df.autor.str.contains("Roberto")]
#print(resultado)

buscar_fecha = df.loc[(df['anio'] > 2000) & (df['anio'] < 2003)]
#print(buscar_fecha)

# buscar por iloc
ilocbusc = df.iloc[2:4, 1:3]
print(ilocbusc)

buscar_fecha.to_csv("resultado.csv", index=False, encoding='utf-8') """

df = pd.read_csv(RUTA, encoding='utf-8')

""" nuevo_libro = {
    "titulo": "El maestro y Margarita",
    "autor": "Mijail Bulgarov",
    "editorial": "DeBolsillo",
    "anio": 2004
}

df = pd.concat([df, pd.DataFrame(nuevo_libro, index=[0])])
df.to_csv(RUTA, index=False, encoding='utf-8') """

#df = df.loc[df['titulo'] != "El Quijote"]

#df.loc[df["autor"] == "Roberto Bolaño", 'anio'] = 2020

#df['ciudad_pub'] = ["Buenos Aires", "Madrid", "Barcelona", "Barcelona", "Madrid"]

#df['idioma'] = "es"

df = df.drop(columns=['idioma'])

df.to_csv(RUTA, index=False, encoding='utf-8')
