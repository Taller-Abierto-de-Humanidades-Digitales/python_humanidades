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

En esta actividad vamos a construir un programa que nos permita consultar una biblioteca de citas bibliográficas. El programa debe permitirnos consultar la biblioteca de citas bibliográficas por título, autor, año de publicación y palabras claves.

## Sobre el conjunto de datos

Para realizar este ejercicio, les brindamos un conjunto de citas bibliográficas exportadas desde el programa [Zotero](https://www.zotero.org/) las cuales pueden visualizar en el [repositorio del curso](https://github.com/Taller-Abierto-de-Humanidades-Digitales/curso_python_extenso/blob/main/data/bibliografia.json).

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

titulo = 'What Do You Do With A Million Readers?'

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

id: http://zotero.org/users/163570/items/897DPHEI
type: book
call-number: P96.N35 D38 2018
collection-title: A K Peters Visualization Series
event-place: Boca Raton, Florida
ISBN: 978-1-138-19710-7
number-of-pages: 296
publisher: CRC Press/Taylor & Francis Group
publisher-place: Boca Raton, Florida
source: Library of Congress ISBN
title: Data-driven storytelling
editor: Riche, Nathalie Henry; Hurter, Christophe; Diakopoulos, Nicholas; Carpendale, Sheelagh
issued: 2018
-----------------

[2]------------

id: http://zotero.org/users/163570/items/NGAJFMZ6
type: book
event-place: Madrid
ISBN: 978-84-15832-10-2
language: English
note: OCLC: 892201485
publisher: Turner
publisher-place: Madrid
source: Open WorldCat
title: Big data: la revolución de los datos masivos
title-short: Big data
author: Mayer-Schönberger, Viktor; Cukier, Kenneth; Iriarte, Antonio
issued: 2013
-----------------

[3]------------

id: http://zotero.org/users/163570/items/TKF3IK4J
type: book
abstract: "Data and its technologies now play a large and growing role in humanities research and teaching. This book addresses the needs of humanities scholars who seek deeper expertise in the area of data modeling and representation. The authors, all experts in digital humanities, offer a clear explanation of key technical principles, a grounded discussion of case studies, and an exploration of important theoretical concerns. The book opens with an orientation, giving the reader a history of data modeling in the humanities and a grounding in the technical concepts necessary to understand and engage with the second part of the book. The second part of the book is a wide-ranging exploration of topics central for a deeper understanding of data modeling in digital humanities. Chapters cover data modeling standards and the role they play in shaping digital humanities practice, traditional forms of modeling in the humanities and how they have been transformed by digital approaches, ontologies which seek to anchor meaning in digital humanities resources, and how data models inhabit the other analytical tools used in digital humanities research. It concludes with a glossary chapter that explains specific terms and concepts for data modeling in the digital humanities context. This book is a unique and invaluable resource for teaching and practising data modeling in a digital humanities context"--
call-number: AZ105 .S43 2019
collection-title: Digital research in the arts and humanities
event-place: London ; New York
ISBN: 978-1-4724-4324-3
number-of-pages: 341
publisher: Routledge, Taylor & Francis Group
publisher-place: London ; New York
source: Library of Congress ISBN
title: The shape of data in the digital humanities: modeling texts and text-based resources
title-short: The shape of data in the digital humanities
editor: Flanders, Julia; Jannidis, Fotis
issued: 2019
-----------------

[4]------------

id: http://zotero.org/users/163570/items/Z8VUPBD6
type: book
call-number: Q355 .R385 2013
collection-title: Infrastructures series
event-place: Cambridge, Massachusetts ; London, England
ISBN: 978-0-262-51828-4
number-of-pages: 182
publisher: The MIT Press
publisher-place: Cambridge, Massachusetts ; London, England
source: Library of Congress ISBN
title: "Raw data" is an oxymoron
editor: Gitelman, Lisa
issued: 2013
-----------------

[5]------------

id: http://zotero.org/users/163570/items/PIYZREFG
type: book
abstract: "The use of quantitative methods in the humanities and related social sciences has increased considerably in recent years, allowing researchers to discover patterns in a vast range of source materials. Despite this growth, there are few resources addressed to students and scholars who wish to take advantage of these powerful tools. Humanities Data Analysis offers the first intermediate-level guide to quantitative data analysis for humanities students and scholars using the Python programming language. This practical textbook, which assumes a basic knowledge of Python, teaches readers the necessary skills for conducting humanities research in the rapidly developing digital environment. The book begins with an overview of the place of data science in the humanities, and proceeds to cover data carpentry: the essential techniques for gathering, cleaning, representing, and transforming textual and tabular data. Then, drawing from real-world, publicly available data sets that cover a variety of scholarly domains, the book delves into detailed case studies. Focusing on textual data analysis, the authors explore such diverse topics as network analysis, genre theory, onomastics, literacy, author attribution, mapping, stylometry, topic modeling, and time series analysis. Exercises and resources for further reading are provided at the end of each chapter. An ideal resource for humanities students and scholars aiming to take their Python skills to the next level, Humanities Data Analysis illustrates the benefits that quantitative methods can bring to complex research questions. Appropriate for advanced undergraduates, graduate students, and scholars with a basic knowledge of Python. Applicable to many humanities disciplines, including history, literature, and sociology. Offers real-world case studies using publicly available data sets. Provides exercises at the end of each chapter for students to test acquired skills. Emphasizes visual storytelling via data visualizations"--
call-number: AZ186 .K37 2021
event-place: Princeton
ISBN: 978-0-691-17236-1
publisher: Princeton University Press
publisher-place: Princeton
source: Library of Congress ISBN
title: Humanities data analysis: case studies with Python
title-short: Humanities data analysis
author: Karsdorp, Folgert; Kestemont, Mike; Riddell, Allen
issued: 2021
-----------------

Se encontraron 5 resultados

```

## Envío de la actividad

Al igual que las actividades anteriores, envía tu código a través de Github.

Para entregar la actividad, debes hacer un `commit` de los modificados y hacer un `push` de tu brazo al repositorio remoto.

```bash
git add .
git commit -m "Entrega de la actividad intermedia"
git push -u origin nombre-del-brazo
```
