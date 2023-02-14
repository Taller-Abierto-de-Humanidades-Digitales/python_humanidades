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

# Sintaxis, variables y tipos de datos básicos

Vamos a entrar en algunos detalles relacionados con lo que hicimos en la sección anterior.

## Sintaxis básica

Python es un lenguaje con una sintaxis muy sencilla. Básicamente comprende los siguientes aspectos:

### Indentación

Cada bloque de código se escribe con espacios o tabuladores. Por ejemplo:

```{code-cell}
if 1 > 0:
    print("1 es mayor que 0")
```

Nota que hay cinco espacios entre la primera instrucción `if 5 > 2:` y la segunda instrucción `print("5 es mayor que 2")`. Si utilizamos otro "formato" vamos a encontrar un error:

```{code-cell}
if 5 > 2: 
print("5 es mayor que 2")
```

Notas que inmediatamente Python identifica este error como un error de indentación. Más adelante veremos algunos casos donde la indentación puede ser "correcta" en términos sintácticos pero no en términos de lógica.

### Comentarios

Un aspecto fundamental en la escritura de código es la escritura de comentarios para documentar nuestro código. Los comentarios son líneas de texto que no son interpretadas por Python. Por lo tanto, no afectan el funcionamiento del código. Por ejemplo:

```{code-cell}
'''
Esto es un comentario de varias líneas.
Lo cual permite describir el código de manera más detallada.
'''
print("Hola mundo") # Esto es un comentario de línea simple
```

Notarás que solamente el código de la línea `print("Hola mundo")` es interpretado por Python. El resto de las líneas se ignoran, pero son fundamentales para que otras personas puedan entender qué estás haciendo en tu código.

## Variables

En términos muy simples, una variable es un "valor" que se asigna a un nombre. Por ejemplo, si yo quiero "guardar" el número 5 en una variable, puedo hacerlo así:

```{code-cell}
numero = 5
```

La utilidad de una variable está marcada en que es posible utilizarla posteriormente en el código para realizar operaciones. Por ejemplo, si quiero sumarle 2 a la variable `numero`, puedo hacerlo así:

```{code-cell}
numero = numero + 2
```

Ahora, la variable `numero` tiene un valor de 7.

De la misma manera lo podemos hacer con cadenas de texto:

```{code-cell}
nombre = "Juan"
apellido = "Pérez"
```

Ahora, si quiero **concatenar** (unir) las variables `nombre` y `apellido`, puedo hacerlo así:

```{code-cell}
nombre_completo = nombre + " " + apellido
```

Esta es una forma simple de entender las variables, porque estamos asignando los valores directamente desde nuestro código. Sin embargo, en la práctica, es muy común que los valores de las variables provengan de otras fuentes, como por ejemplo, de un archivo de texto o de una base de datos. En estos casos, la forma de asignar los valores implica ciertas operaciones, que veremos más adelante.

### ¿cómo nombro una variable?

En general, es recomendable que los nombres de las variables sean descriptivos, es decir, que permitan entender a qué se refiere la variable. Por ejemplo, si quiero guardar el nombre de una persona, es mejor que el nombre de la variable sea `nombre` que `n`. Esto es especialmente importante cuando el código es compartido con otras personas, porque permite que el código sea más legible.

En Python, los nombres de las variables pueden contener letras, números y el símbolo `_`. Sin embargo, no pueden comenzar con un número. Por ejemplo, los siguientes nombres de variables son válidos:

```{code-cell}
nombre = "nombre"
nombre1 = "nombre"
nombre_1 = "nombre"
```

Los siguientes nombres de variables no son válidos:

```{code-cell}
1nombre = "nombre"
nombre-1 = "nombre"
```

Notarás que este código nos ha marcado un error de sintáxis (`SyntaxError: invalid syntax`), lo cual indica que no es un nombre de variable válida.

Respecto a las mayúsculas y minúsculas, Python no realiza ninguna distinción. Por ejemplo, las siguientes variables son correctas:

```{code-cell}
nombre = "nombre"
Nombre = "nombre"
NOMBRE = "nombre"
```

Sin embargo, hay que tener en cuenta que existe una especie de acuerdo entre la comunidad de programadores, que consiste en que los nombres de las variables se escriban en minúsculas, y que las palabras que componen el nombre de la variable se separen con un guión bajo (`_`). Por ejemplo, `nombre_completo` es un nombre de variable con un estulo adecuado, mientras que `nombreCompleto` no lo es. Esto hace que el código sea más legible y nos permite distinguir fácilmente las variables de las funciones o las clases [^var_global].

Nombrar variables es una habilidad importante, porque aunque técnicamente no sea compleja, evita cometer errores. Por ejemplo, si queremos guardar el nombre de una persona, es muy fácil escribir `nombre` en lugar de `nombre_completo`. En este caso, el código no va a fallar, pero el resultado no va a ser el esperado. Por eso, es importante que los nombres de las variables sean descriptivos.

## Tipos de datos

Python tiene una gran ventaja con respecto a otros lenguajes de programación y es que no es necesario declarar el tipo de dato que se va a utilizar. Es decir, que el mismo lenguaje puede identificar si me estoy refiriendo a un número, a una cadena de texto, a una lista, etc. Esto es muy útil porque nos permite ahorrar tiempo y esfuerzo en la programación.

Veámos entonces qué tipos de datos básicos existen en Python.

### Números

Los números pueden ser enteros o decimales. Por ejemplo, los siguientes son números enteros (*integers*):

```{code-cell}
uno = 1
dos = 2
tres = 3
```

Los siguientes son números decimales (*floats*):

```{code-cell}
uno_cero = 1.0
dos_cero = 2.0
tres_cero = 3.0
```

Con estos tipos de datos podemos realizar operaciones aritméticas básicas:

```{code-cell}
suma = uno + dos
resta = tres_cero - uno_cero
multiplicacion = dos * tres_cero
division = tres / dos

print(suma)
print(resta)
print(multiplicacion)
print(division)
```

Si revisas con detenimiento los resultados, notarás que la división de dos números enteros (`tres` y `dos`) nos da un número decimal. Esto es porque Python siempre va a intentar devolver el resultado de una operación con el tipo de dato más complejo. Por ejemplo, si sumamos un número entero y un número decimal, el resultado va a ser un número decimal.

### Cadenas de texto

Las cadenas de texto (*strings*) son una secuencia de caracteres. Por ejemplo, las siguientes son cadenas de texto:

```{code-cell}
nombre = "nombre"
apellido = "apellido"
```

Las cadenas de texto se pueden concatenar con el operador `+`:

```{code-cell}
nombre_completo = nombre + " " + apellido
print(nombre_completo)
```

También se pueden multiplicar por un número entero:

```{code-cell}
nombre_completo = nombre_completo * 3
print(nombre_completo)
```

```{admonition} Sobre las cadenas de texto
:class: tip
Debemos entender que las cadenas de texto son una secuencia de caracteres. Es decir, la computadora entiende una palabra como "perro" como la secuencia de los caracteres "p", "e", "r", "r", "o". Y es una secuencia totalmente diferente a "P", "e", "r", "r", "o". Es decir, para la computadora "perro" es diferente a "Perro". Así, cuando tratamos de un tipo de valor de "texto" no nos referimos al texto en el sentido humano (letras, palabras, frases...), sino al texto en el sentido de la computadora.
```

#### Formateo de cadenas de texto

En ocasiones, queremos mostrar un mensaje que contenga información de una variable. Por ejemplo, si queremos mostrar el nombre completo de una persona, podemos hacerlo de la siguiente manera:

```{code-cell}
nombre = "Manila"
apellido = "Luzon"
nombre_completo = nombre + " " + apellido
print("El nombre completo es " + nombre_completo)
```

Sin embargo, esta forma de hacerlo es muy tediosa. Por eso, Python nos permite formatear las cadenas de texto de una manera más sencilla. Para ello, debemos utilizar el método `format()` de las cadenas de texto. Por ejemplo, si queremos mostrar el nombre completo de una persona, podemos hacerlo de la siguiente manera:

```{code-cell}
print("El nombre completo es {}".format(nombre_completo))
```

El método `format()` nos permite insertar variables dentro de una cadena de texto. Para ello, debemos utilizar las llaves `{}`. En este caso, la variable `nombre_completo` se inserta dentro de la cadena de texto en la posición de la llave `{}`.

Incluso podemos hacerlo de manera más sintética simplemente agregando una `f` antes de la cadena de texto. Por ejemplo, si queremos mostrar el nombre completo de una persona, podemos hacerlo de la siguiente manera:

```{code-cell}
print(f"El nombre completo es {nombre_completo}")
```

El formateo de cadenas de texto es muy útil cuando queremos modificar textos o incluso asignar valores no textuales a una variable textual. Por ejemplo:

```{code-cell}
edad = 20
print(f"El nombre completo es {nombre_completo} y tiene {edad} años")
```

### Booleanos

Los valores booleanos (*booleans*) son valores que pueden ser `True` o `False`. Por ejemplo:

```{code-cell}
verdadero = True
falso = False
```

Los valores booleanos son muy útiles para realizar operaciones lógicas. Por ejemplo, podemos comparar dos valores y obtener un valor booleano:

```{code-cell}
print(uno == dos)
print(uno != dos)
```

Los símbolos `==` y `!=` son operadores lógicos, es decir, nos permite comparar si un valor es igual o diferente de otro valor. En este caso, el resultado de la comparación es un valor booleano.

Por esto, los valores de igualdad no se refieren solamente a números, sino que también se pueden utilizar para comparar cadenas de texto. Por ejemplo:

```{code-cell}
print("perro" == "Perro")
print("perro" != "Perro")
```

También nos permite comparar si un valor es mayor o menor que otro valor:

```{code-cell}
print(uno > dos)
print(uno < dos)
```

Los valores booleanos también nos permiten realizar operaciones lógicas. Por ejemplo, podemos utilizar los operadores `and` y `or` para determinar si dos valores booleanos son verdaderos o falsos. Por ejemplo:

```{code-cell}
print(uno == dos and uno < dos)
print(uno == dos or uno < dos)
```

En el primer caso, el primer valor es falso y el segundo verdadero, por lo que el resultado es falso. En el segundo caso, el primer valor es falso y el segundo verdadero, por lo que el resultado es verdadero [^logica_formal].

Y, finalmente, nos permite comparar tipos de datos. Por ejemplo:

```{code-cell}
print(type(uno) == int)
print(type(uno) == str)
```

## Síntesis

En este capítulo hemos aprendido sobre los tipos de datos más comunes en Python. En particular, hemos aprendido sobre los tipos de datos numéricos, los tipos de datos de texto y los tipos de datos booleanos. Además, hemos aprendido sobre el formateo de cadenas de texto y sobre las operaciones lógicas. En el siguiente apartado, abordaremos las listas, un tipo de dato muy importante en Python.

## Notas

[^var_global]: En algunos lenguajes de programación existe una distinción entre variables locales y globales, que se refiere a que las variables locales solo pueden ser utilizadas dentro de la función en la que fueron declaradas. En Python, no existe esta distinción, por lo que todas las variables son globales. De igual manera, existen algunos valores que pueden considerarse "constantes", es decir, que no se modifican durante toda la ejecución del código. Python no cuenta con un mecanismo de declarar un valor como constante, pero se puede simular utilizando nombres de variables en mayúsculas. Por ejemplo, `PI = 3.1416`.

[^logica_formal]: En lógica formal, los operadores `and` y `or` se conocen como conjunción y disyunción, respectivamente. La conjunción es verdadera si ambos valores son verdaderos, mientras que la disyunción es verdadera si al menos uno de los valores es verdadero. Para profundizar en este tema, te recomiendo el primer capítulo del libro de {cite}`juola_six_2017`.
