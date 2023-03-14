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

# Pasar cantidades arbitrarias de argumentos

Debido a que los parámetros en Python se comportan de manera similar a un tuple, podemos pasar una cantidad arbitraria de argumentos para una función. Para hacer esto, debemos agregar un asterisco (`*`) antes del nombre del parámetro. Por ejemplo, podemos tener una función que nos pida cuáles libros nuevos hemos comprado:

```{code-cell} ipython3
def libros_nuevos(*libros):
    """Imprime los libros nuevos que se han comprado.
    
    Parámetros
    ----------
    libros: tuple
        Lista de libros nuevos que se han comprado
    """
    print("Los libros nuevos que se han comprado son:")
    for libro in libros:
        print(f"- {libro}")
```

Ahora podemos llamar a la función `libros_nuevos()` con una cantidad arbitraria de argumentos:

```{code-cell} ipython3
libros_nuevos("El principito", "El señor de los anillos", "El quijote", "Ser y tiempo", "El aleph", "Vigilar y castigar", "Elogio de la locura")

```

En este caso, no importa si compramos un libro o 100 libros, la función `libros_nuevos()` imprimirá todos los libros que se han comprado.

## Mezclar argumentos posicionales y arbitrarios

Ahora, podemos modificar esta función para que reciba un argumento posicional y un argumento arbitrario. Por ejemplo, si queremos agregar el nombre de la persona que compró los libros, podemos hacer lo siguiente:

```{code-cell} ipython3
def libros_nuevos(nombre, *libros):
    """Imprime los libros nuevos que se han comprado.
    
    Parámetros
    ----------
    nombre: str
        Nombre de la persona que compró los libros
    libros: tuple
        Lista de libros nuevos que se han comprado
    """
    print(f"Hola {nombre}. Has comprado los siguientes libros:")
    for libro in libros:
        print(f"- {libro}")
```

Ahora podemos llamar a la función `libros_nuevos()` con un argumento posicional y una cantidad arbitraria de argumentos:

```{code-cell} ipython3
usuario = "Juan"
libros_nuevos(usuario, "El principito", "El señor de los anillos", "El quijote", "Ser y tiempo", "El aleph", "Vigilar y castigar", "Elogio de la locura")
```

```{admonition} Observación
:class: warning
El argumento arbitrario es de tipo `tuple`, no listado. Si pasamos como argumento una lista la función no iterará sobre cada elemento, para ello debemos desempaquetar la lista con el operador `*`.

Por ejemplo:

usuario = "Juan"
listado_libros = ["El señor de los anillos", "El principito", "El quijote"]

libros_nuevos(usuario, *listado_libros)
```

## Pasar cantidades arbitrarias de argumentos con palabras clave

Debido a que los parámetros en Python se comportan de manera similar a un diccionario, podemos pasar una cantidad arbitraria de argumentos con palabras clave para una función. Para hacer esto, debemos agregar dos asteriscos (`**`) antes del nombre del parámetro. Por ejemplo, podemos tener una función que nos pida cuáles libros nuevos hemos comprado:

```{code-cell} ipython3
def libros_nuevos(**libros):
    """Imprime los libros nuevos que se han comprado.
    
    Parámetros
    ----------
    libros: dict
        Diccionario con los libros nuevos que se han comprado
    """
    print("Los libros nuevos que se han comprado son:")
    for libro, autor in libros.items():
        print(f"- {libro} ({autor})")
```

Ahora podemos llamar a la función `libros_nuevos()` con una cantidad arbitraria de argumentos con palabras clave:

```{code-cell} ipython3
libros_nuevos(
    El_principito="Antoine de Saint-Exupéry",
    El_señor_de_los_anillos="J. R. R. Tolkien",
    El_quijote="Miguel de Cervantes",
    Ser_y_tiempo="Martin Heidegger",
    El_aleph="Jorge Luis Borges",
    Vigilar_y_castigar="Michel Foucault",
    Elogio_de_la_locura="Erasmo de Rotterdam",
)
```

Podemos, de la misma manera, pasar argumentos posicionales y argumentos con palabras clave a la función `libros_nuevos()`:

```{code-cell} ipython3
def libros_nuevos(autor, titulo, **atributos):
    atributos["autor"] = autor
    atributos["titulo"] = titulo
    return atributos
```

```{code-cell} ipython3
libros_nuevos(
    "Antoine de Saint-Exupéry",
    "El principito",
    editorial="Salamandra",
    año=1943,
    genero="Ciencia ficción",
    idioma="Francés",
)
```

En general, el uso de argumentos arbitrarios es útil cuando no sabemos cuántos argumentos se pasarán a una función. No es algo que utilicemos a menudo, pero es ampliamente usado en librerías de terceros, por eso es importante conocerlo y aprender a utilizarlo.
