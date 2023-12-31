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

# Manejo de datos en archivos CSV

Los archivos CSV (Comma Separated Values) son archivos de texto plano que contienen datos separados por comas. Los archivos CSV son muy utilizados para el intercambio de datos entre aplicaciones porque se escriben como texto plano, no dependen de una plataforma o software específico y replican la estructura de una hoja de cálculo.

En Python podemos leer y escribir archivos CSV utilizando el módulo `csv`. Este módulo nos permite leer y escribir archivos CSV de forma muy sencilla.

Por ejemplo, supongamos que queremos llevar nuestro inventario de la biblioteca a un archivo CSV. Para ello, podemos crear un archivo CSV con el siguiente contenido:

```text
titulo,autor,editorial,anio
El Aleph,Jorge Luis Borges,Emece,1949
El Quijote,Miguel de Cervantes,Alfaguara,2005
El desbarrancadero,Fernando Vallejo,Planeta,2001
Una novelita Lumpen,Roberto Bolaño,Anagrama,2002
El amante,Marguerite Duras,Tusquets,1984
```

Para crear el csv debemos importar la librería `csv` y utilizar el método `writer`:

```{code-cell} ipython3
import os
import csv

with open(os.path.join(os.getcwd(), "inventario.csv"), "w", newline="") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["titulo", "autor", "editorial", "anio"])
    writer.writerow(["El Aleph", "Jorge Luis Borges", "Emece", 1949])
    writer.writerow(["El Quijote", "Miguel de Cervantes", "Alfaguara", 2005])
    writer.writerow(["El desbarrancadero", "Fernando Vallejo", "Planeta", 2001])
    writer.writerow(["Una novelita Lumpen", "Roberto Bolaño", "Anagrama", 2002])
    writer.writerow(["El amante", "Marguerite Duras", "Tusquets", 1984])
```

Notarás como utilizamos, en principio, la misma lógica que con los archivos de texto con el método `open`, pero para realizar la escritura del archivo utilizamos el método `writer` del módulo `csv`. Este método nos permite escribir en el archivo fila por fila. Para ello, utilizamos el método `writerow` que recibe una lista con los elementos de la fila.

Debemos prestar atención a la manera como está escrito el valor dentro de la función `writerow`, es decir, se incluye como una lista de elementos de cualquier tipo. En el caso de los valores numéricos, no se incluyen entre comillas.

De forma que si tuviéramos una lista de listas con los datos de nuestro inventario, podríamos escribir el archivo CSV de la siguiente manera:

```{code-cell} ipython3
inventario = [
    ["titulo", "autor", "editorial", "anio"],
    ["El Aleph", "Jorge Luis Borges", "Emece", 1949],
    ["El Quijote", "Miguel de Cervantes", "Alfaguara", 2005],
    ["El desbarrancadero", "Fernando Vallejo", "Planeta", 2001],
    ["Una novelita Lumpen", "Roberto Bolaño", "Anagrama", 2002],
    ["El amante", "Marguerite Duras", "Tusquets", 1984],
]

with open(os.path.join(os.getcwd(), "inventario.csv"), "w", newline="") as archivo:
    writer = csv.writer(archivo)
    for fila in inventario:
        writer.writerow(fila)
```

## Lectura de archivos CSV

Para leer un archivo CSV, utilizamos el método `reader` del módulo `csv`. Este método nos permite leer el archivo fila por fila. Para ello, utilizamos el método `readrow` que recibe una lista con los elementos de la fila.

```{code-cell} ipython3
import os
import csv

with open(os.path.join(os.getcwd(), "inventario.csv"), "r") as archivo:
    reader = csv.reader(archivo)
    for fila in reader:
        print(fila)
```

Notarás que el método `reader` nos devuelve una lista con los elementos de la fila. De esta forma, podemos acceder a los elementos de la fila por su índice.

```{code-cell} ipython3
import os
import csv

with open(os.path.join(os.getcwd(), "inventario.csv"), "r") as archivo:
    reader = csv.reader(archivo)
    for fila in reader:
        print(fila[0])
```

## Lectura de archivos CSV con encabezados

En el caso de que nuestro archivo CSV tenga encabezados (como es el caso de nuestro csv), podemos utilizar el método `DictReader` del módulo `csv`. Este método nos permite leer el archivo fila por fila. Para ello, utilizamos el método `readrow` que recibe una lista con los elementos de la fila.

```{code-cell} ipython3
import os
import csv

with open(os.path.join(os.getcwd(), "inventario.csv"), "r") as archivo:
    reader = csv.DictReader(archivo)
    for fila in reader:
        print(fila)
```

## Agregar nuevas filas

Para agregar nuevas filas a un archivo CSV, debemos abrir el archivo en modo de escritura y utilizar el método `writer` del módulo `csv`. Este método nos permite escribir en el archivo fila por fila. Para ello, utilizamos el método `writerow` que recibe una lista con los elementos de la fila.

```{code-cell} ipython3
import os
import csv

with open(os.path.join(os.getcwd(), "inventario.csv"), "a", newline="") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["El jugador", "Fiodor Dostoievsky", "Salvat", 1969])
```

Comprobemos que se agregó la nueva fila:

```{code-cell} ipython3
import os
import csv

with open(os.path.join(os.getcwd(), "inventario.csv"), "r") as archivo:
    reader = csv.reader(archivo)
    for fila in reader:
        print(fila)
```

## Crear un CSV a partir de un diccionario

Supongamos que tenemos un diccionario con los datos de nuestro inventario:

```{code-cell} ipython3
inventario = [
    {"titulo": "El Aleph", "autor": "Jorge Luis Borges", "editorial": "Emece", "anio": 1949},
    {"titulo": "El Quijote", "autor": "Miguel de Cervantes", "editorial": "Alfaguara", "anio": 2005},
    {"titulo": "El desbarrancadero", "autor": "Fernando Vallejo", "editorial": "Planeta", "anio": 2001},
    {"titulo": "Una novelita Lumpen", "autor": "Roberto Bolaño", "editorial": "Anagrama", "anio": 2002},
    {"titulo": "El amante", "autor": "Marguerite Duras", "editorial": "Tusquets", "anio": 1984},
]
```

Para crear el csv debemos importar la librería `csv` y utilizar el método `DictWriter`:

```{code-cell} ipython3
import os
import csv

with open(os.path.join(os.getcwd(), "inventario.csv"), "w", newline="") as archivo:
    writer = csv.DictWriter(archivo, fieldnames=["titulo", "autor", "editorial", "anio"])
    writer.writeheader()
    for libro in inventario:
        writer.writerow(libro)
```

Y comprobamos que se creó correctamente el archivo CSV:

```{code-cell} ipython3
with open(os.path.join(os.getcwd(), "inventario.csv"), "r") as archivo:
    reader = csv.reader(archivo)
    for fila in reader:
        print(fila)
```

Notarás que utilizamos el método `writeheader` para escribir la primera fila con los encabezados.

## Ejercicios

### Ejercicio 1

Crear un archivo CSV con los datos de los libros de la biblioteca. El archivo debe tener las siguientes columnas: `titulo`, `autor`, `editorial`, `anio`. El archivo debe tener como encabezados: `Título`, `Autor`, `Editorial`, `Año`.

### Ejercicio 2

Crear un programa que permita a los usuarios agregar nuevos libros al archivo CSV.
