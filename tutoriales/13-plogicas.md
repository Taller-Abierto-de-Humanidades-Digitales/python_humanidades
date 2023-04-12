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

# Pruebas condicionales

Las pruebas condicionales consisten en evaluar una condición lógica matemática (igualdad, desigualdad, mayor que, menor que, entre otras). Para ello, nos valemos de una serie de operadores para representar proposiciones y para manipular y evaluar expresiones. Estos operadores pueden ser lógicos (`and`, `or`, `not`) o relacionales (`==`, `!=`, `>`, `<`, `>=`, `<=`). Los operadores relacionales se utilizan para comparar dos valores y devolver un valor booleano (`True` o `False`). Los operadores lógicos se utilizan para combinar expresiones booleanas y devolver un valor booleano (`True` o `False`). Veamos esto con mayor detalle.

## Operaciones de igualdad

Las operaciones de igualdad se utilizan para comparar dos valores y determinar si son iguales o no. Para ello, se utiliza el operador `==`. Como ya vimos, si la igualdad se cumple, la expresión devuelve `True`, de lo contrario devuelve `False`. Veamos algunos ejemplos:

```{code-cell} ipython3
perro = "Firulais"
print(perro == "Firulais")
```

En este caso es evidente que la igualdad se cumple, ya que el valor de la variable es idéntica al valor que se compara. Ahora, veamos un caso diferente:

```{code-cell} ipython3
perro = "Firulais"
print(perro == "Lassie")
```

La condición ahora no se cumple, ya que el valor de la variable (`Firulais`) es diferente al valor que se compara (`Lassie`). Veamos un ejemplo más:

```{code-cell} ipython3
perro = "Firulais"
print(perro == "firulais")
```

La condición ahora no se cumple aunque los valores `Firulais` y `firulais` tienen el mismo significado (son iguales en términos semánticos). Esto se debe a que Python distingue entre mayúsculas y minúsculas. Para evitar esto, podemos utilizar el método `lower()` que convierte todos los caracteres de una cadena a minúsculas:

```{code-cell} ipython3
perro = "Firulais"
print(perro.lower() == "firulais")
```

Obviamente, esto no es un caso que siempre se pueda utilizar, ya que en ciertas ocasiones es relevante identificar mayúsculas y minúsculas. Por ejemplo, si queremos saber si una palabra es un palíndromo, es decir, si se lee igual de izquierda a derecha que de derecha a izquierda, entonces sí es importante distinguir entre mayúsculas y minúsculas. Por ello, la elección de utilizar o no el método `lower()` (o cualquier otra transformación que favorezca la igualdad) dependerá del contexto.

## Operaciones de desigualdad

En este caso, lo que se busca es determinar si dos valores son diferentes. Si la condición se cumple, será verdadera. Para ello, se utiliza el operador `!=`. Veamos algunos ejemplos:

```{code-cell} ipython3
perro = "Firulais"
print(perro != "Firulais")
```

En este caso, la condición no se cumple, ya que el valor de la variable es idéntico al valor que se compara. Ahora, veamos un caso diferente:

```{code-cell} ipython3
perro = "Firulais"
print(perro != "Lassie")
```

La condición ahora sí se cumple, ya que el valor de la variable (`Firulais`) es diferente al valor que se compara (`Lassie`). Veamos un ejemplo más:

```{code-cell} ipython3
perro = "Firulais"
print(perro != "firulais")
```

La condición ahora sí se cumple porque los valores son diferentes al comparar mayúsculas y minúsculas.

## Operaciones de mayor que y menor que

Estas operaciones son utilizadas para comparar valores numéricos (podríamos comparar si dos cadenas son mayores o menores, pero no tiene mucho sentido). Si la condición se cumple, será verdadera. Para ello, se utilizan los operadores `>`, `<`, respectivamente. Veamos algunos ejemplos:

```{code-cell} ipython3
print(5 > 3)
```

En este caso, la condición se cumple, ya que el valor de la variable es mayor que el valor que se compara. Ahora, veamos un caso diferente:

```{code-cell} ipython3
print(5 < 3)
```

Este fue el tipo de comparación que utilizamos en el ejemplo introductorio de este capítulo. La condición que buscamos era determinar si el valor aleatorio obtenido por la función `randint()` era menor que 50 (dentro de un rango de 1 a 100). Veamos ese ejemplo nuevamente:

```{code-cell} ipython3
from random import randint
numero = randint(1, 100)
print(numero)
print(numero < 50)
```

Este ejemplo es útil porque en general lo que buscamos con un operador de este tipo es asegurar una condición para tomar una decisión específica.

## Operaciones de mayor o igual que y menor o igual que

Una extensión de las operaciones anteriores está dada por las de mayor o igual que y menor o igual que. Para ello, utilizamos los operadores `>=` y `<=`, respectivamente. Veamos un ejemplo simple:

```{code-cell} ipython3
print(5 >= 3)
```

En este caso, el operador cumple la misma función que el operador `>`. Pero veamos este caso:

```{code-cell} ipython3
print(5 > 5)
print(5 >= 5)
```

Observa como la primera condición no se cumple (porque 5 no es mayor que 5), pero la segunda sí (por la igualdad). Esto es un asunto fundamental en una serie numérica, por ejemplo:

```{code-cell} ipython3
for i in range(0, 10):
    if i >= 5:
        print(i)
```

En este caso, la serie de números incluye al cinco, pero si utilizáramos el operador `>` en lugar de `>=`, el cinco no sería incluido en la serie. Nuevamente, este uso depende de la intención de nuestro programa, por lo que es importante no utilizar los operadores de manera indiscriminada.

## Probando condiciones múltiples

En ocasiones, necesitamos probar más de una condición. Por ejemplo, en el ejemplo introductorio de este capítulo, queríamos determinar si el valor aleatorio obtenido por la función `randint()` era menor que 50 y mayor que 25. Para ello, podemos utilizar los operadores `and` y `or`. Veamos un ejemplo:

```{code-cell} ipython3
from random import randint
numero = randint(1, 100)
print(numero)
print(numero <= 50 and numero >= 25)
```

Para que la condición se cumpla, el número aleatorio debe ser menor o igual que 50 y mayor o igual que 25, o lo que es lo mismo, debe estar dentro del rango de 25 a 50. Veamos otro ejemplo:

```{code-cell} ipython3
from random import randint
numero = randint(1, 100)
print(numero)
print(numero <= 50 or numero >= 25)
```

En este caso la condición siempre se va a cumplir, por lo que hablamos de una tautología. No importa el valor que nos de la función `randint()`, todo número que es menor o igual a 50 siempre será mayor o igual a 25 (incluso si el número es igual a 25 o 50). Por esta razón, es relevante considerar que en estos casos utilizamos operadores lógicos cercanos a la lógica proposicional, por lo que es importante tener en cuenta la validez de las proposiciones que se forman.

Ahora bien, `and` y `or` no aplican solamente para condiciones matemáticas, sino que también pueden ser utilizados para comparar cadenas de caracteres. Veamos un ejemplo:

```{code-cell} ipython3
perro = "Firulais"
gato = "Garfield"

print(perro == "Firulais" and gato == "Garfield")
```

En todo caso, siempre estamos evaluando condiciones, por lo que debemos ser capaces de interpretar los resultados como valores booleanos, o lo que es lo mismo:

```{code-cell} ipython3
print(True and True)
print(True and False)
print(False and True)
print(False and False)
```

Lo siguiente no es indispensable para aprender a programar en Python, pero entender un poco la lógica proposicional nos puede ayudar a entender mejor los operadores `and` y `or`.

## Un poco de lógica proposicional

Podemos entender así cualquier valor booleano como una proposición. Por ejemplo:

* Firulais es el nombre de un perro: `perro == "Firulais"`
* Garfield es el nombre de un gato: `gato == "Garfield"`
* Firulais es el nombre de un perro y Garfield es el nombre de un gato: `perro == "Firulais" and gato == "Garfield"`

Lo que formalmente se puede escribir con variables proposicionales de la siguiente forma:

$$
\begin{align}
P &= \text{Firulais es el nombre de un perro} \\
Q &= \text{Garfield es el nombre de un gato} \\
R &= \text{Firulais es el nombre de un perro y Garfield es el nombre de un gato} \\
O &= \text{Firulais es el nombre de un perro o Garfield es el nombre de un gato} \\
\end{align}
$$

Y así, una tabla de verdad con estas proposiciones sería:

$$
\begin{array}{c|c|c|c|c}
P & Q & R & O \\
\hline
\text{V} & \text{V} & \text{V} & \text{V} \\
\text{V} & \text{F} & \text{F} & \text{V} \\
\text{F} & \text{V} & \text{F} & \text{V} \\
\text{F} & \text{F} & \text{F} & \text{F} \\
\end{array}
$$

De manera lógica, podemos escribir cualquiera de estas proposiciones como código Python:

```{code-cell} ipython3
perro = "Firulais"
gato = "Garfield"

condicion1 = perro != "Firulais" # corresponde a P falsa en la tabla de verdad
condicion2 = gato == "Garfield" # corresponde a Q verdadera en la tabla de verdad

print(condicion1 and condicion2) # corresponde a R falsa en la tabla de verdad
print(condicion1 or condicion2) # corresponde a O verdadera en la tabla de verdad
```

## A modo de cierre

En este apartado nos hemos centrado en los operadores de comparación que nos permiten evaluar condiciones de verdad o falsedad de manera lógica. Antes de entrar a explorar la estructura de control `if`, veremos rápidamente los operadores de pertenencia, los cuales nos permiten evaluar si un elemento se encuentra dentro de una colección.
