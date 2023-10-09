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
# Leer y escribir archivos

Es muy frecuente en un programa que necesitemos almacenar y recuperar información que debe estar disponible incluso cuando el programa no se esté ejecutando. En este apartado, veremos cómo hacerlo con archivos de texto, que corresponden a la manera más básica de almacenar información en un disco.

## Abrir un archivo

Para abrir un archivo, debemos usar la función `open()`. 

La sintaxis de `open()` es la siguiente:

``` python
objeto = open(nombre_archivo, modo)
```

La variable `objeto` es un objeto de tipo `file` que representa el archivo. Este objeto "prepara" el texto para poder ser leído o escrito.

El parámetro `nombre_archivo` es una cadena de caracteres que contiene el nombre del archivo que se va a abrir. Si el archivo no existe, `open()` lo crea. Si el archivo ya existe, `open()` lo sobreescribe. Es relevante señalar que el nombre del archivo corresponde a una ruta en el directorio, de tal manera que si es un nombre simple, indica que el archivo se encuentra en el directorio actual desde el cual se ejecuta el programa.

El parámetro `modo` puede ser `r` para abrir el archivo en modo lectura, `w` para abrirlo en modo escritura, o `a` para abrirlo en modo de anexión. Si se omite el parámetro `modo`, se asume que el archivo se abre en modo lectura.

Veamos un ejemplo muy sencillo:

```{code-cell} ipython3

f = open("../archivos/txt/ejemplo.txt", "r")
print(f)
```

Notemos dos cosas en este ejemplo:

1. El archivo `ejemplo.txt` se encuentra en el directorio `archivos/txt`, que es un subdirectorio del directorio raíz desde el cual se ejecuta el programa. Los dos puntos le indican a Python que la ruta se encuentra en el directorio "padre" del programa. Por lo tanto, el nombre del archivo es `../archivos/txt/ejemplo.txt`.
2. La variable `f` es un objeto de tipo `file`. Este tipo de objetos tiene métodos que permiten leer y escribir en el archivo. Por esa razón, cuando hacemos un `print(f)`, se imprime la información del objeto `file`, la cual es fácil de reconocer porque comienza con `_io.TextIOWrapper`.

## Leer un archivo

Para leer un archivo, debemos usar el método `read()` del objeto `file`.

La sintaxis de `read()` es la siguiente:

``` python
objeto.read()
```

Usemos el método `read()` para leer el archivo `ejemplo.txt`:

```{code-cell} ipython3
print(f.read())
```

¿Por qué se muestra este `UnicodeDecodeError`? Este es un error muy común cuando trabajamos con archivos de texto. El problema es que el archivo `ejemplo.txt` no está codificado en UTF-8, sino en cp1252. Para solucionar este problema, debemos especificar el tipo de codificación al abrir el archivo:

```{code-cell} ipython3
f = open("../archivos/txt/ejemplo.txt", "r", encoding="utf-8")
print(f.read())
```

La codificación UTF-8 es la más común, sobre todo porque abarca una amplitud de símbolos como acentos, diéresis, virgulillas, etc. que no se pueden representar con el conjunto de caracteres ASCII. Sin embargo, hay otros tipos de codificación, como cp1252, que es la que utiliza Windows para representar los caracteres latinos.

```{admonition} Nota
:class: tip
Un archivo de texto es en realidad un archivo binario. El texto se almacena en el archivo como una secuencia de bytes. Cada byte representa un caracter. La codificación es la forma en que se asigna un byte a un caracter. Por ejemplo, la codificación ASCII asigna un byte a cada caracter. La codificación UTF-8 asigna uno o más bytes a cada caracter. La codificación cp1252 asigna un byte a cada caracter.

Dependiendo de la máquina en la que se ejecuta el programa, la codificación puede ser diferente. Por ejemplo, en Windows, la codificación por defecto es cp1252, mientras que en Linux, la codificación predeterminada es UTF-8. Por esa razón, es importante especificar la codificación al abrir un archivo de texto.
```

## Escribir en un archivo

Para escribir en un archivo, debemos usar el método `write()` del objeto `file`.

La sintaxis de `write()` es la siguiente:

``` python
objeto.write(cadena)
```

El parámetro `cadena` es una cadena de caracteres que contiene el texto que se va a escribir en el archivo.

Utilicemos este método para escribir el primer párrafo del cuento "El guardagujas" de Juan José Arreola:

```{code-cell} ipython3
:tags: [remove-output]
f = open("../archivos/txt/arreola.txt", "w", encoding="utf-8")
texto = "El guardagujas\n\nJuan José Arreola\n\nEl forastero llegó sin aliento a la estación desierta. Su gran valija, que nadie quiso cargar, le había fatigado en extremo. Se enjugó el rostro con un pañuelo, y con la mano en visera miró los rieles que se perdían en el horizonte. Desalentado y pensativo consultó su reloj: la hora justa en que el tren debía partir.\n"
f.write(texto)
```

```{admonition} Nota
:class: tip
El método `write()` no agrega un salto de línea al final de la cadena de caracteres. Por lo tanto, si queremos escribir varias líneas en el archivo, debemos agregar el salto de línea explícitamente con el caracter `\n`.
```

También es muy común utilizar la palabra reservada `with` para abrir un archivo. La palabra reservada `with` permite que el archivo se cierre automáticamente al finalizar el bloque de código. Por ejemplo:

```{code-cell} ipython3
with open("../archivos/txt/arreola.txt", "w", encoding="utf-8") as f:
    f.write(texto)
```

En caso de que no utilicemos esta sintaxis, es recomendable cerrar el archivo con el método `close()`:

``` python
f = open("../archivos/txt/arreola.txt", "w", encoding="utf-8")
f.write(texto)
f.close()
```

## Agregar texto al archivo

Cuando utilizamos el modo `w` se sobreescribe el archivo, lo cual tendrá consecuencias inesperadas si no es esa nuestra intención original. Por ejemplo, si tenemos este segundo párrafo:

```{code-cell} ipython3
segundoparrafo = "Alguien, salido de quién sabe dónde, le dio una palmada muy suave. Al volverse el forastero se halló ante un viejecillo de vago aspecto ferrocarrilero. Llevaba en la mano una linterna roja, pero tan pequeña, que parecía de juguete. Miró sonriendo al viajero, que le preguntó con ansiedad:\n"
```

Si lo agregamos con el modo `w` tendremos este resultado:

```{code-cell} ipython3
with open("../archivos/txt/arreola.txt", "w", encoding="utf-8") as f:
  f.write(segundoparrafo)

print(open("../archivos/txt/arreola.txt", "r", encoding="utf-8").read())
```

¡Se ha eliminado nuestro primer texto!

Para evitar esto, debemos utilizar el modo `a` (append) para agregar texto al final del archivo:

```{code-cell} ipython3
:tags: [remove-cell]
with open("../archivos/txt/arreola.txt", "w", encoding="utf-8") as f:
  f.write(texto)
```

```{code-cell} ipython3
with open("../archivos/txt/arreola.txt", "a", encoding="utf-8") as f:
  f.write(segundoparrafo)

print(open("../archivos/txt/arreola.txt", "r", encoding="utf-8").read())
```

En este caso, el archivo no se sobreescribe, sino que se agrega el texto al final.

## Leer líneas

En este momento, si leemos el archivo `arreola.txt`, veremos que el texto se encuentra todo en una sola línea. Para leer una línea del archivo, debemos usar el método `readline()` del objeto `file`.

La sintaxis de `readline()` es la siguiente:

``` python
objeto.readline()
```

Usemos este método para leer la primera línea del archivo `arreola.txt`:

```{code-cell} ipython3
f = open("../archivos/txt/arreola.txt", "r", encoding="utf-8")
print(f.readline())
```

También podemos construir una iteración para leer todas las líneas del archivo:

```{code-cell} ipython3
for linea in f:
    print(linea)
```

Python también dispone de la función `readlines()` que lee todas las líneas del archivo y las almacena en una lista:

```{code-cell} ipython3
f = open("../archivos/txt/arreola.txt", "r", encoding="utf-8")
print(f.readlines())
```

## Conclusión

Como hemos visto, hay una serie de métodos que nos permiten manipular archivos de texto. Este tipo de métodos pueden extenderse a prácticamente cualquier tipo de archivo, incluso a archivos binarios. No obstante, entre más complejo sea el archivo, más compleja será la manipulación.