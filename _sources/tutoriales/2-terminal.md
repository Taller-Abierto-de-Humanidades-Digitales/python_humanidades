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

# Terminal

## ¿Qué es?

El terminal es una herramienta que nos permite interactuar con el sistema operativo a través de comandos. Estos comandos son similares a los que usamos en el lenguaje natural, pero en vez de palabras usamos comandos que el sistema operativo entiende.

## ¿Cómo abrir el terminal?

### Windows

1. Presionar la tecla `Windows` + `R` para abrir el cuadro de ejecución.
2. Escribir `cmd` y presionar `Enter`.

### Mac

1. Presionar `Command` + `Espacio` para abrir Spotlight.
2. Escribir `terminal` y presionar `Enter`.

## Probar Python desde el terminal

### Windows

1. Abrir el terminal.
2. Escribir `python` y presionar `Enter`.
3. Escribir `print("Hola mundo")` y presionar `Enter`.
4. Escribir `exit()` y presionar `Enter` para salir.

```{code-cell}
C:\Users\Usuario>python
Python 3.11.0 (tags/v3.11.0:1a79785, Oct  5 2021, 19:00:00) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hola mundo")
Hola mundo
>>> exit()
```

### Mac

1. Abrir el terminal.
2. Escribir `python3` y presionar `Enter`.
3. Escribir `print("Hola mundo")` y presionar `Enter`.
4. Escribir `exit()` y presionar `Enter` para salir.

```{code-cell}
$ python3
Python 3.11.0 (tags/v3.11.0:1a79785, Oct  5 2021, 19:00:00) [Clang 13.0.0 (clang-1300.0.29.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hola mundo")
Hola mundo
>>> exit()
```
