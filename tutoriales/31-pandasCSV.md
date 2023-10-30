---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---
# Manejar archivos CSV con `pandas`

Para trabajar con archivos CSV de tamaño modesto, es suficiente (y recomendable) utilizar la librería `csv`, pero para poder trabajar con archivos CSV de gran tamaño y complejidad, es recomendado apelar a la librería `pandas`.

Esta librería fue creada por Wes McKinney en 2008 y es una de las más utilizadas en el mundo de la ciencia de datos. `pandas` es una librería de código abierto que provee estructuras de datos y herramientas de análisis de datos de alto rendimiento y fácil de usar. En particular, `pandas` provee estructuras de datos y operaciones para manipular tablas numéricas y series temporales. Además, `pandas` está construida sobre `numpy`, por lo que es posible utilizar las funciones de `numpy` en `pandas`.

En este curso, simplemente utilizaremos la librería `pandas` para leer y escribir archivos CSV. Para aprender más sobre `pandas`, te recomiendo explorar el libro de Wes McKinney, *Python for Data Analysis* {cite}`mckinney_python_2018`.

```{admonition} Nota
:class: warning
En muchos foros se suele comentar que utilizar `pandas` simplemente para leer y escribir archivos CSV es como utilizar un tanque para matar una mosca. Ten esto en cuenta para el momento de utilizar esta librería en un entorno de desarrollo profesional.
```

## Instalar `pandas`

Para instalar `pandas`, podemos utilizar `pip` o `conda`:

```shell
pip install pandas
```

```shell
conda install pandas
```

La versión actual (abril 2023) es la 2.0.1. Sin embargo, es posible que gran parte de los tutoriales que existen en la actualidad dependan de la versión 1.5 o anterior. Verifica cuál es la versión de tu instalación de `pandas` con el siguiente código:

```{code-cell} ipython3
import pandas as pd

print(pd.__version__)
```

La versión que ves arriba será la que utilizaremos en este tutorial.

## Leer archivos CSV

Para leer un archivo CSV con `pandas`, podemos utilizar el método `read_csv()`. Este método tiene muchos argumentos opcionales que permiten configurar la lectura del archivo CSV. Pasemos a leer nuestro archivo `inventario.csv` con `pandas`:

```{code-cell} ipython3
import pandas as pd
import os
import chardet

# usaremos en este ejemplo la librería chardet para detectar el encoding del archivo
raw = open(os.path.join(os.getcwd(), "inventario.csv"), 'rb').read()
encodign = chardet.detect(raw)['encoding']

df = pd.read_csv(os.path.join(os.getcwd(), "inventario.csv"), encoding=encodign)
print(df)
```

Como verás, únicamente requerimos de la función `read_csv` para leer el archivo CSV. Para poder hacer frente a una cantidad de posibles formas de creación del archivo, `pandas` cuenta con un buen número de parámetros que permiten solventar archivos con separadores diferentes a comas (`sep=";"`), con encabezados (`header=0`), con índices (`index_col=0`), con valores faltantes (`na_values=[""]`), etc. Para conocer todos los parámetros de la función `read_csv`, puedes consultar la [documentación oficial](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.read_csv.html).

El resultado de la lectura del archivo CSV es un objeto de tipo `DataFrame` de `pandas`. Un `DataFrame` es una estructura de datos bidimensional que puede contener datos de diferentes tipos (numéricos, de cadena de caracteres, booleanos, etc.). En este caso, el `DataFrame` contiene los datos del archivo CSV, con los tipos de datos que `pandas` consideró más adecuados para cada columna.

```{code-cell} ipython3
print(type(df))
```

## Escribir archivos CSV

Para escribir un archivo CSV con `pandas`, podemos utilizar el método `to_csv()`. Sin embargo, debemos convertir los datos que queremos a un formato de `DataFrame` para que puedan ser guardados en la tabla. Por ejemplo, si queremos guardar los datos de un diccionario, podemos convertirlo a un `DataFrame` y luego guardarlo en un archivo CSV:

```{code-cell} ipython3
import pandas as pd

diccionario = {
    "nombre": ["Juan", "María", "Pedro"],
    "edad": [25, 30, 40],
    "ciudad": ["Bogotá", "Medellín", "Cali"]
}

df = pd.DataFrame(diccionario)

df.to_csv("diccionario.csv", index=False, encoding="utf-8")
```

Y podemos compronbar que el archivo CSV se creó correctamente:

```{code-cell} ipython3
df = pd.read_csv("diccionario.csv")
print(df)
```

## Agregar datos a un CSV con `pandas`

En este caso, lo que debemos realizar es una lectura del archivo CSV, agregar los datos que queremos y luego escribir el archivo CSV. Por ejemplo, si queremos agregar una nueva fila al archivo `diccionario.csv`, podemos hacer lo siguiente:

```{code-cell} ipython3
import pandas as pd

df = pd.read_csv("diccionario.csv")

nueva_fila = {
    "nombre": "Luis",
    "edad": 35,
    "ciudad": "Barranquilla"
}

df = pd.concat([df, pd.DataFrame(nueva_fila, index=[0])])

df.to_csv("diccionario.csv", index=False, encoding="utf-8")
```

Y podemos comprobar que el archivo CSV se creó correctamente:

```{code-cell} ipython3
df = pd.read_csv("diccionario.csv")
print(df)
```

Paradójicamente, si queremos simplemente agregar una fila al archivo CSV, es más eficiente utilizar la librería `csv` que `pandas`. Sin embargo, si queremos agregar varias filas, es mucho mejor utilizar `pandas`. Depende de las necesidades del programa que utilicemos o no `pandas` para agregar datos a un archivo CSV.

## Eliminar datos de un CSV con `pandas`

En este caso, lo que debemos realizar es una lectura del archivo CSV, eliminar los datos que queremos y luego escribir el archivo CSV. Por ejemplo, si queremos eliminar la fila con nombre "María" del archivo `diccionario.csv`, podemos hacer lo siguiente:

```{code-cell} ipython3
import pandas as pd

df = pd.read_csv("diccionario.csv")

df = df[df["nombre"] != "María"]

df.to_csv("diccionario.csv", index=False, encoding="utf-8")
```

Y podemos comprobar que el archivo CSV se creó correctamente:

```{code-cell} ipython3
df = pd.read_csv("diccionario.csv")
print(df)
```

## Actualizar datos de un CSV con `pandas`

En este caso, lo que debemos realizar es una lectura del archivo CSV, actualizar los datos que queremos y luego escribir el archivo CSV. Por ejemplo, si queremos actualizar la edad de la fila con nombre "Pedro" del archivo `diccionario.csv`, podemos hacer lo siguiente:

```{code-cell} ipython3
import pandas as pd

df = pd.read_csv("diccionario.csv")

df.loc[df["nombre"] == "Pedro", "edad"] = 45

df.to_csv("diccionario.csv", index=False, encoding="utf-8")
```

Y podemos comprobar que el archivo CSV se creó correctamente:

```{code-cell} ipython3
df = pd.read_csv("diccionario.csv")
print(df)
```

La gran ventaja de los dos ejemplos anteriores con respecto a la librería `csv` es que no tenemos que crear un archivo temporal para luego renombrarlo. `pandas` se encarga de todo esto por nosotros.

## Crear una nueva columna en un CSV con `pandas`

En este caso, lo que debemos realizar es una lectura del archivo CSV, crear la nueva columna y luego escribir el archivo CSV. Por ejemplo, si queremos crear una nueva columna con el nombre "pais_nacimiento" en el archivo `diccionario.csv`, podemos hacer lo siguiente:

```{code-cell} ipython3
import pandas as pd

df = pd.read_csv("diccionario.csv")

df["pais_nacimiento"] = ["Colombia", "Perú", "Colombia"]

df.to_csv("diccionario.csv", index=False, encoding="utf-8")
```

Y podemos comprobar que el archivo CSV se creó correctamente:

```{code-cell} ipython3
df = pd.read_csv("diccionario.csv")
print(df)
```

## Eliminar una columna de un CSV con `pandas`

En este caso, lo que debemos realizar es una lectura del archivo CSV, eliminar la columna y luego escribir el archivo CSV. Por ejemplo, si queremos eliminar la columna "pais_nacimiento" del archivo `diccionario.csv`, podemos hacer lo siguiente:

```{code-cell} ipython3
import pandas as pd

df = pd.read_csv("diccionario.csv")

df = df.drop(columns=["pais_nacimiento"])

df.to_csv("diccionario.csv", index=False, encoding="utf-8")
```

Y podemos comprobar que el archivo CSV se creó correctamente:

```{code-cell} ipython3
df = pd.read_csv("diccionario.csv")
print(df)
```

## Actualizar una columna de un CSV con `pandas`

En este caso, lo que debemos realizar es una lectura del archivo CSV, actualizar la columna y luego escribir el archivo CSV. Por ejemplo, si queremos actualizar la columna "ciudad" del archivo `diccionario.csv`, podemos hacer lo siguiente:

```{code-cell} ipython3
import pandas as pd

df = pd.read_csv("diccionario.csv")

df["ciudad"] = ["Barranquilla", "Cali", "Tunja"]

df.to_csv("diccionario.csv", index=False, encoding="utf-8")
```

Y podemos comprobar que el archivo CSV se creó correctamente:

```{code-cell} ipython3
df = pd.read_csv("diccionario.csv")
print(df)
```

## Conclusión

En este tutorial apenas arañamos la superficie de lo que se puede hacer con `pandas`. Sin embargo, es suficiente para que puedas empezar a utilizar esta librería para leer, escribir y actualizar archivos CSV.

## Ejercicios

1. Crea un archivo CSV con los datos de tu biblioteca personal. Cada fila debe tener los siguientes datos: título, autor, editorial, año de publicación, género y número de páginas. Luego, crea un programa que lea el archivo CSV y muestre los datos de todos los libros que sean de un género específico.

2. Crea una pequeña interface que permita agregar, eliminar y actualizar los datos del archivo CSV. Puedes aprovechar la librería `csv` o `pandas` para realizar esta tarea.
