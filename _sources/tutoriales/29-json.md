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
# Archivos JSON

## ¿Qué es JSON?

JSON (JavaScript Object Notation) es un formato de texto sencillo para el intercambio de datos. Se trata de un subconjunto de la notación literal de objetos de JavaScript, aunque, debido a su amplia adopción como alternativa a XML, se considera un formato independiente del lenguaje.

Este formato es ampliamente utilizado para el intercambio de datos entre aplicaciones, especialmente en aplicaciones web. El formato JSON es muy sencillo y se basa en dos estructuras:

- Una colección de pares de nombre/valor. En varios lenguajes esto es conocido como un objeto, registro, estructura, diccionario, tabla hash, lista de claves o un arreglo asociativo.
- Una lista ordenada de valores. En la mayoría de los lenguajes, esto se implementa como arreglos, vectores, listas o sequencias.

De una manera burda, podríamos pensar en este formato de archivo como una lista de diccionarios, donde cada diccionario es un registro de datos.

Esta flexibilidad, fácil uso y disponibilidad en múltiples lenguajes, ha hecho que se desarrolle toda una tecnología alrededor de este formato, conocida como bases de datos no relacionales o NoSQL. AL contrario de las bases de datos relacionales, fundamentadas en tablas, las bases de datos NoSQL se basan en documentos, que son estructuras de datos similares a los diccionarios de Python.

En esta lección, veremos cómo podemos leer y escribir archivos JSON en Python, y para ello, vamos a retomar el archivo JSON que utilizamos para la actividad intermedia. Este archivo está ubicado en la ruta relativa `data/bibliografia.json` y desde esa ruta podremos leerlo.

Para poder leer el archivo JSON, primero debemos importar el módulo `json` de Python.

```{code-cell} ipython3
import os
import json
```

Este módulo nos proporciona dos funciones principales: `load` y `dump`. La primera nos permite leer un archivo JSON y convertirlo en un objeto de Python, mientras que la segunda nos permite convertir un objeto de Python en un archivo JSON.

## Lectura de archivos JSON

Para leer un archivo JSON, utilizamos la función `load` del módulo `json`. Esta función recibe como argumento un objeto de tipo archivo, que puede ser un archivo abierto o un objeto de tipo `StringIO`. En este caso, vamos a leer el archivo `data/bibliografia.json` y lo vamos a asignar a la variable `bibliografia`.

```{code-cell} ipython3
with open("../data/bibliografia.json", "r", encoding='utf-8') as archivo:
    bibliografia = json.load(archivo)
```

Si imprimimos el contenido de la variable `bibliografia`, veremos que se trata de una lista de diccionarios.

```{code-cell} ipython3
bibliografia[0:5]
```

```{admonition} load vs loads
:class: tip
Un error muy común consiste en confundir la función `load` con la función `loads`. La primera está diseñada para leer un archivo JSON, mientras que la segunda está diseñada para leer una cadena de texto en formato JSON. Si intentamos leer un archivo JSON con la función `loads`, obtendremos un error.
```

## Escritura de archivos JSON

Para escribir un archivo JSON, utilizamos la función `dump` del módulo `json`. Esta función recibe como argumento un objeto de tipo archivo, que puede ser un archivo abierto o un objeto de tipo `StringIO`, y un objeto de Python que queremos convertir en un archivo JSON. Por ejemplo, vamos a crear un diccionario en Python con los valores un libro y luego crearemos un archivo de prueba con este diccionario.

```{code-cell} ipython3
libro = {
  "id": "http://zotero.org/users/163570/items/DFIAXHAZ",
  "type": "book",
  "event-place": "Madrid",
  "ISBN": "978-84-460-0264-2",
  "language": "Spanish",
  "note": "OCLC: 40162792",
  "publisher": "Akal",
  "publisher-place": "Madrid",
  "source": "Open WorldCat",
  "title": "El problema de la incredulidad en el siglo XVI: la religión de Rabelais",
  "title-short": "El problema de la incredulidad",
  "author": [
   {
    "family": "Febvre",
    "given": "Lucien"
   }
  ],
  "translator": [
   {
    "family": "Balsinde",
    "given": "Isabel"
   }
  ],
  "issued": {
   "date-parts": [
    [
     "1993"
    ]
   ]
  }
 }
```

```{code-cell} ipython3
with open("../data/libro.json", "w", encoding='utf-8') as archivo:
    json.dump(libro, archivo)
```

Si abrimos el archivo `data/libro.json`, veremos que se trata de un archivo JSON con el contenido del diccionario que hemos creado.

```{code-cell} ipython3
with open("../data/libro.json", "r", encoding='utf-8') as archivo:
    print(archivo.read())
```

```{admonition} Atención
:class: warning
Para hacer una visualización rápida del contenido del archivo utilizamos la función `read()`, pero debemos tener en cuenta que en este caso no se retorna un diccionario sino un tipo `str`.
```

### Crear un archivo JSON a partir de una lista de diccionarios

En el caso anterior, hemos creado un archivo JSON a partir de un diccionario, pero también podemos crear un archivo JSON a partir de una lista de diccionarios. Para ello, vamos a crear una lista de diccionarios con los datos de dos libros de la bibliografía.

```{code-cell} ipython3
libros = [
 {
  "id": "http://zotero.org/users/163570/items/KM78SEUK",
  "type": "book",
  "event-place": "Madrid",
  "ISBN": "978-84-206-4775-3",
  "language": "Spanish",
  "note": "OCLC: 187040016",
  "number-of-pages": "302",
  "publisher": "Alianza",
  "publisher-place": "Madrid",
  "source": "Open WorldCat",
  "title": "Formas de historia cultural",
  "author": [
   {
    "family": "Burke",
    "given": "Peter"
   }
  ],
  "translator": [
   {
    "family": "Urrutia",
    "given": "Belén"
   }
  ],
  "issued": {
   "date-parts": [
    [
     "2006"
    ]
   ]
  }
 },
 {
  "id": "http://zotero.org/users/163570/items/LKAU7WRX",
  "type": "book",
  "edition": "Kindle",
  "event-place": "Madrid",
  "language": "es",
  "number-of-pages": "600",
  "publisher": "Taurus",
  "publisher-place": "Madrid",
  "title": "El miedo en Occidente (Siglos XIV-XVIII) Una ciudad sitiada",
  "title-short": "El miedo en Occidente",
  "author": [
   {
    "family": "Delumeau",
    "given": "Jean"
   }
  ],
  "translator": [
   {
    "family": "Armiño",
    "given": "Mauro"
   }
  ],
  "contributor": [
   {
    "family": "Gutiérrez",
    "given": "Francisco"
   }
  ],
  "issued": {
   "date-parts": [
    [
     "2012"
    ]
   ]
  }
 }
]

# Abrimos el archivo libros.json en modo escritura y volcamos el contenido de la lista libros

with open("../data/libros.json", "w", encoding='utf-8') as archivo:
    json.dump(libros, archivo)
```

Si abrimos el archivo `data/libros.json`, veremos que se trata de un archivo JSON con el contenido de la lista de diccionarios que hemos creado.

```{code-cell} ipython3
with open("../data/libros.json", "r", encoding='utf-8') as archivo:
   libros = json.load(archivo)

for libro in libros:
    print(libro["title"])
```

## Añadir elementos a un archivo JSON

Ahora, hagamos el ejercicio de agregar el contenido de nuestro archivo `libros.json` al archivo `bibliografia.json`. Para ello, vamos a leer el contenido del archivo `libros.json` y luego vamos a agregarlo al archivo `bibliografia.json` con la ayuda de la función `extend()`.

```{code-cell} ipython3
# Leemos el archivo libros.json y lo guardamos en la variable libros

with open("../data/libros.json", "r", encoding='utf-8') as archivo:
   libros = json.load(archivo)

# Leemos el archivo bibliografia.json y lo guardamos en la variable bibliografia

with open("../data/bibliografia.json", "r", encoding='utf-8') as archivo:
   bibliografia = json.load(archivo)

# Agregamos el contenido de la variable libros a la variable bibliografia

bibliografia.extend(libros)

# Abrimos el archivo bibliografia.json en modo escritura y volcamos el contenido de la variable bibliografia

with open("../data/bibliografia.json", "w", encoding='utf-8') as archivo:
    json.dump(bibliografia, archivo)
```

Comprobemos que el archivo `bibliografia.json` contiene el contenido de los dos archivos.

```{code-cell} ipython3
with open("../data/bibliografia.json", "r", encoding='utf-8') as archivo:
   bibliografia = json.load(archivo)

title = "El miedo en Occidente (Siglos XIV-XVIII) Una ciudad sitiada"

for libro in bibliografia:
    if libro["title"] == title:
        print(libro)
```

## Eliminar elementos de un archivo JSON

Para eliminar un elemento de la lista de diccionarios que hemos creado, vamos a utilizar la función `remove()`. En este ejemplo, quitaremos el libro *El miedo en Occidente (Siglos XIV-XVIII) Una ciudad sitiada* de la lista de diccionarios.

```{code-cell} ipython3
# Leemos el archivo bibliografia.json y lo guardamos en la variable bibliografia

with open("../data/bibliografia.json", "r", encoding='utf-8') as archivo:
   bibliografia = json.load(archivo)

# Eliminamos el libro "El miedo en Occidente (Siglos XIV-XVIII) Una ciudad sitiada" de la variable bibliografia

title = "El miedo en Occidente (Siglos XIV-XVIII) Una ciudad sitiada"

for libro in bibliografia:
    if libro["title"] == title:
        bibliografia.remove(libro)

# Abrimos el archivo bibliografia.json en modo escritura y volcamos el contenido de la variable bibliografia

with open("../data/bibliografia.json", "w", encoding='utf-8') as archivo:
    json.dump(bibliografia, archivo)

# Comprobamos que el libro ha sido eliminado

with open("../data/bibliografia.json", "r", encoding='utf-8') as archivo:
   bibliografia = json.load(archivo)

for libro in bibliografia:
    if libro["title"] == title:
        print(libro)
```

Como no se ha impreso nada, podemos comprobar que el libro ha sido eliminado.

## Modificar elementos de un archivo JSON

Para modificar un elemento de la lista de diccionarios que hemos creado, vamos a utilizar la función `update()`. En este ejemplo, modificaremos el libro *Formas de historia cultural* de la lista de diccionarios, cambiaremos la fecha del libro de 2006 a 2020.

```{code-cell} ipython3
# Leemos el archivo bibliografia.json y lo guardamos en la variable bibliografia

with open("../data/bibliografia.json", "r", encoding='utf-8') as archivo:
   bibliografia = json.load(archivo)

# Modificamos el libro "Formas de historia cultural" de la variable bibliografia

title = "Formas de historia cultural"

for libro in bibliografia:
    if libro["title"] == title:
        libro["issued"]["date-parts"] = [["2020"]]
        libro["edition"] = "2ª edición"

# Abrimos el archivo bibliografia.json en modo escritura y volcamos el contenido de la variable bibliografia

with open("../data/bibliografia.json", "w", encoding='utf-8') as archivo:
    json.dump(bibliografia, archivo)

# Comprobamos que el libro ha sido modificado

with open("../data/bibliografia.json", "r", encoding='utf-8') as archivo:
   bibliografia = json.load(archivo)

for libro in bibliografia:
    if libro["title"] == title:
        print(libro)

```

## Formatear un archivo JSON

Si abrimos el archivo JSON que hemos creado, veremos que está escrito de manera continua, sin saltos de línea ni sangrías. Para que sea más fácil de leer, podemos utilizar la función `dump()` con el parámetro `indent` para que el archivo se escriba con sangrías y saltos de línea.

```{code-cell} ipython3
with open("../data/bibliografia.json", "r", encoding='utf-8') as archivo:
   bibliografia = json.load(archivo)

# guardar el archivo con formato

with open("../data/bibliografia.json", "w", encoding='utf-8') as archivo:
    json.dump(bibliografia, archivo, indent=4)
```

Si abrimos el archivo `bibliografia.json`, veremos que ahora está escrito con sangrías y saltos de línea.

En ocasiones, también será necesario que aseguremos que la codificación sea correcta, sobre todo cuando trabajamos con textos diferentes al inglés. La función `dump()` no trae incorporado el parámetro 'encoding', pero podemos utilizar el parámetro `ensure_ascii` el cual recibe un valor booleano (True|False) para determinar si debe codificarse en ASCII o en otra codificación. En nuesto caso, el idioma español, es recomendable usar el modo `ensure_ascii=False`. Nuestro código quedaría así;

```{code-cell} ipython3
with open("../data/bibliografia.json", "w", encoding='utf-8') as archivo:
    json.dump(bibliografia, archivo, indent=4, ensure_ascii=False)
```

## Conclusión

Como habrás notado, trabajar con archivos JSON es muy similar a hacerlo con diccionarios. Solamente debemos tener en cuenta que el objeto que se está recibiendo es una lista de diccionarios y que, por lo tanto, debemos iterar sobre ella para poder acceder a los elementos que contiene.
