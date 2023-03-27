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

# Actividad intermedia: Construye un programa real

En esta actividad vamos a construir un programa que nos permita consultar una biblioteca de referencias bibliográficas. El programa debe permitirnos consultar la bibliografía por título, autor, año de publicación y palabras claves.

## Sobre el conjunto de datos

Para realizar este ejercicio, les brindamos un [conjunto de referencias bibliográficas](https://www.zotero.org/groups/197065/humanidades_digitales/library) exportadas desde el programa [Zotero](https://www.zotero.org/) las cuales pueden visualizar en el [repositorio del curso](https://github.com/Taller-Abierto-de-Humanidades-Digitales/curso_python_extenso/blob/main/data/bibliografia.json).

Este conjunto de datos contiene la siguiente información:

```{code-cell} ipython
:tags: [remove-input]
from biblioteca import biblioteca # importar el conjunto de datos

# contar el número de elementos en la biblioteca
biblioteca  = biblioteca()
print(f'Número de elementos en la biblioteca: {len(biblioteca)}\n')

# imprimir las claves de todos los elementos:

claves = []

for elemento in biblioteca:
    for clave in elemento:
        if clave not in claves:
            claves.append(clave)

tipos_bibliograficos = []

for elemento in biblioteca:
    if elemento['type'] not in tipos_bibliograficos:
        tipos_bibliograficos.append(elemento['type'])

tipos_bibliograficos.sort()
claves.sort()

print(f'Tipos de elementos: {tipos_bibliograficos}\n')
print(f'Claves de los elementos: {claves}\n')
```

```{admonition} Importante
Es sumamente recomendable (por no decir *obligatorio*) que realicen una revisión de la estructura y contenido del conjunto de datos antes de iniciar la escritura del programa. Por ejemplo, cuántos elementos hay por cada tipo, qué claves tiene cada tipo de elemento, cuáles de estas claves son obligatorias, etc.
```

### Acceder al conjunto de datos

El archivo contiene una biblioteca de citas bibliográficas en formato CSL-JSON. La biblioteca está construida a partir de una exportación de elementos de Zotero en el formato [CSL-JSON](https://citeproc-js.readthedocs.io/en/latest/csl-json/markup.html). En esta estructura, cada elemento un diccionario dentro de una lista. Cada diccionario contiene una serie de pares clave-valor.

Para facilitar la recuperación de la información y evitar duplicar innecesariamente los datos, he creado el módulo biblioteca.py (ubicado en `codigo/actividad_intermedia/biblioteca.py`) que contiene una función llamada `biblioteca` que se encarga de descargar y leer el conjunto de datos.

Para usarlo, debes **copiar** el archivo `biblioteca.py` en tu carpeta de trabajo y luego importar la función `biblioteca` en un nuevo archivo de Python:

```{code-cell} ipython
from biblioteca import biblioteca
```

Prueba que la importación sea correcta. En caso de que no lo sea y obtengas un error de `ModuleNotFoundError` o `ImportError`, revisa que el archivo `biblioteca.py` se encuentre en la misma carpeta de trabajo que el archivo donde estás escribiendo el código.

```{admonition} Advertencia
:class: warning
No debes escribir en el código del módulo `biblioteca.py` ni borrar el archivo del directorio original. De otra manera puedes encontrar errores de importación o afectar el funcionamiento de los programas de tus compañeros.
```

### Acceder a los elementos de la biblioteca

Debido a que la biblioteca es una lista de diccionarios, podemos acceder a cada elemento de la biblioteca usando la sintaxis de listas.

Por ejemplo, para acceder al primer elemento de la biblioteca, podemos usar la siguiente sintaxis:

```{code-cell} ipython
from biblioteca import biblioteca

biblioteca = biblioteca()

print(biblioteca[0])
```

Y en este ejemplo, si queremos acceder al valor de la clave `title`, podemos usar la siguiente sintaxis:

```{code-cell} ipython
print(biblioteca[0]['title'])
```

En este sentido, un buscador deberá iterar sobre todo el diccionario y comparar el valor de cada clave con el valor de búsqueda. Por ejemplo, si queremos buscar un elemento por título, podemos usar la siguiente sintaxis para encontrar una coincidencia exacta:

```{code-cell} ipython
from biblioteca import biblioteca

titulo = '¿Qué son las Humanidades Digitales?'

for elemento in biblioteca():
    if elemento['title'].lower() == titulo.lower():
        print(elemento)
```

## Instrucciones

### 1. Construir el módulo de búsquedas

El primer paso es construir un módulo que permita realizar búsquedas en la biblioteca. Para esto, debes crear un nuevo archivo de Python en la carpeta de trabajo con el nombre `busqueda.py`.

Este archivo debe tener una función para realizar búsquedas con las siguientes condiciones:

* Debe buscar por título, autor, año de publicación y palabras claves.
* Debe tener la opción de buscar por libro, artículo, tesis o cualquier otro tipo de elemento.
* Debe tener la opción de buscar por coincidencia exacta o por coincidencia parcial.
* Debe tener la capacidad de formatear el resultado para hacerlo legible al usuario.
* Debe poder lidiar con el tipo de dato de los autores (`list`) y de las fechas (`dict`).

Este módulo debe tener un conjunto de funciones que permitan hacer estas tareas.

Debe tener por lo menos dos funciones:

* Una función que permita buscar por título, autor, año de publicación y palabras claves.
* Una función que permita formatear el resultado de la búsqueda.

El módulo debe estar en la capacidad de replicar un resultado como el siguiente:

```{code-cell} ipython
from busqueda import busqueda_simple, formar_result

# Buscar la palabra "Data" en el título de los libros
resultado = busqueda_simple('Data', 'title', 'book')
print(formar_result(resultado))
```

### 2. Construir el módulo de interfaz

El segundo paso es construir un módulo que permita interactuar con el usuario. Para esto, debes crear un nuevo archivo de Python en la carpeta de trabajo con el nombre `buscador.py`.

Este archivo debe tener una función que permita interactuar con el usuario. Esta función debe tener un menú que permita al usuario elegir entre las siguientes opciones:

* Ingresar la palabra clave de búsqueda.
* Seleccionar si se desea buscar por título, autor, fecha o palabra clave.
* Seleccionar si se desea filtrar por libro, artículo, tesis o cualquier otro tipo de elemento.

El módulo debe estar en la capacidad de replicar un resultado como el siguiente:

```bash

Ingrese los datos de la búsqueda
Palabra a buscar: Data
Tipos de búsqueda: [1] Título, [2] Autor, [3] Fecha, [4] Palabra clave
Tipo de búsqueda (1, 2, 3, 4): 1
Tipos de documento: [1] Libro, [2] Artículo, [3] Tesis, [4] Cualquiera
Tipo de documento (1, 2, 3, 4): 1
Buscando 'Data' en 'title' de tipo 'book'


[1]------------

id: AdrianCaballeroRoldan2019Bid
type: book
abstract: rare book
ISBN: 978-84-948972-0-7
language: Spanish
note: 00000
publisher: RC Libros
source: Amazon
title: Bid data con Python. Recolección, almacenamiento y proceso
author: Adrián Caballero Roldán, Rafael Caballero / Martín Martín
issued: 2019
-----------------

[2]------------

id: Hamidovic.etal2019Ancient
type: book
abstract: Ancient Manuscripts in Digital Culture presents an overview of the digital turn in Ancient Jewish and Christian manuscripts visualisation, data mining and communication. Edited by David Hamidović, Claire Clivaz and Sarah Bowen Savant, it gathers together the contributions of seventeen scholars involved in Biblical, Early Jewish and Christian studies. The volume attests to the spreading of digital humanities in these fields and presents fundamental analysis of the rise of visual culture as well as specific test-cases concerning ancient manuscripts. Sophisticated visualisation tools, stylometric analysis, teaching and visual data, epigraphy and visualisation belong notably to the varied overview presented in the volume.
collection-number: 3
collection-title: Digital Biblical Studies
edition: 1ª
event-place: Leiden - Boston
ISBN: 978-90-04-39929-7
language: English
note: ZSCC: 0000001
number-of-pages: xvi, 284
number-of-volumes: 1
publisher: Brill
publisher-place: Leiden - Boston
title: Ancient Manuscripts in Digital Culture. Visualisation, Data Mining, Communication
source: Library of Congress ISBN
title: The shape of data in the digital humanities: modeling texts and text-based resources
title-short: The shape of data in the digital humanities
editor: Flanders, Julia; Jannidis, Fotis
issued: 2019
-----------------

Se encontraron 4 resultados

```

## Envío de la actividad

Al igual que las actividades anteriores, envía tu código a través de Github.

Para entregar la actividad, debes hacer un `commit` de los modificados y hacer un `push` de tu brazo al repositorio remoto.

```bash
git add .
git commit -m "Entrega de la actividad intermedia"
git push -u origin nombre-del-brazo
```
