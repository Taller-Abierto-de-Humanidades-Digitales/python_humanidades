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

# Introducción a Python

## ¿Qué es Python?

Python es un lenguaje de programación interpretado, de alto nivel y multiplataforma. Es un lenguaje de programación **interpretado**, lo que significa que no es necesario compilar el código fuente para ejecutarlo. Es un lenguaje de programación de **alto nivel**, lo que significa que no es necesario preocuparse por detalles de bajo nivel como la gestión de memoria. Es un lenguaje de programación **multiplataforma**, lo que significa que se puede ejecutar en diferentes sistemas operativos como Windows, Mac y Linux.

## Ventajas de Python

* Es un lenguaje de programación fácil de aprender y de utilizar.
* Es un lenguaje muy popular y tiene una gran comunidad de usuarios.
* Es un lenguaje que permite escribir código de forma rápida y eficiente, es decir, con menos líneas de código.
* Python cuenta con una extensa biblioteca estándar que nos permite resolver problemas de forma rápida y sencilla.
* Los programas escritos en Python son fáciles de mantener y de depurar.

## ¿Para qué se usa Python?

Python es un lenguaje de programación enfocado en el desarrollo de software de aplicación. Es decir, se utiliza para crear aplicaciones de escritorio, aplicaciones web, aplicaciones móviles, etc. También es un lenguaje ampliamente utilizado en la investigación científica, la ciencia de datos y en el desarrollo de inteligencia artificial. En las aplicaciones Web, Python es especialmente utilizado en el backend, es decir, en el servidor.

En general, es un muy buen lenguaje para aprender a programar y es posible desarrollar una carrera enfocada en el procesamiento y análisis de información. Por otra parte, después de conocer los conceptos básicos de programación, es posible aprender otros lenguajes de programación con otros propósitos como JavaScript, C++, Rust, etc.

## Sintaxis básica de Python

### Comentarios

Los comentarios son líneas de código que no se ejecutan. Se utilizan para documentar el código y explicar qué hace cada parte del programa. En Python, los comentarios se escriben utilizando el símbolo `#` al principio de la línea.

```{code-cell}
# Esto es un comentario
print("Hola mundo") # Esto también es un comentario
```

### Indentación

Python utiliza la indentación para definir bloques de código. Un bloque de código es un conjunto de líneas de código que se ejecutan juntas. En Python, los bloques de código se definen utilizando la indentación. La indentación es la sangría que se agrega al principio de una línea de código. 

```{code-cell}
# Esto es un bloque de código
nombre = "Ada"
apellido = "Lovelace"

# Esto es otro bloque de código
print(nombre)

# Esto es otro bloque de código

if nombre == "Ada":
    print("Hola Ada")
else:
    print("Hola desconocido")
```

Con el tiempo iremos familiarizándonos con la indentación y aprenderemos a identificar los bloques de código. Por ahora, solo debes saber que la indentación es importante en Python y que debes utilizarla correctamente.
