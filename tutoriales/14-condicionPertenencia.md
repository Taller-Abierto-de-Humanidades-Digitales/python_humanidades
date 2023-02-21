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

# Operadores de pertenencia

En este caso, lo que se busca es determinar si un valor se encuentra dentro de una colección de valores. Si la condición se cumple, será verdadera. Para ello, se utiliza el operador `in`. Veamos algunos ejemplos:

```{code-cell} ipython3
perro = "Firulais"
print(perro in ["Firulais", "Lassie", "Scooby Doo"])
```

En este caso, la condición se cumple ya que el valor de la variable `perro` se encuentra dentro de la lista de perros. Ahora, veamos un caso diferente:

```{code-cell} ipython3
perro = "Firulais"
print(perro in ["Lassie", "Scooby Doo"])
```

En este caso, la condición no se cumple ya que el valor de la variable `perro` no se encuentra dentro de la lista de perros. Veamos un ejemplo más:

```{code-cell} ipython3
perro = "Firulais"
print(perro in "Firulais")
```

En este caso, la condición se cumple ya que el valor de la variable `perro` se encuentra dentro de la cadena de caracteres.

## Operadores de no pertenencia

En este caso, lo que se busca es determinar si un valor no se encuentra dentro de una colección de valores. Si la condición se cumple, será verdadera. Para ello, se utiliza el operador `not in`. Veamos algunos ejemplos:

```{code-cell} ipython3
perro = "Firulais"
print(perro not in ["Firulais", "Lassie", "Scooby Doo"])
```

En este caso, la condición no se cumple ya que el valor de la variable `perro` se encuentra dentro de la lista de perros. 

Como habrás deducido, el operador `not in` es el opuesto del operador `in`.

## Operadores de pertenencia y no pertenencia con cadenas de caracteres

En el caso de las cadenas de caracteres, el operador `in` determina si un carácter se encuentra dentro de la cadena de caracteres. Veamos un ejemplo:

```{code-cell} ipython3
print("a" in "Hola")
```

En este caso, la condición se cumple ya que el carácter `a` se encuentra dentro de la cadena de caracteres. Ahora, veamos un caso diferente:

```{code-cell} ipython3
print("b" in "Hola")
```

En este caso, la condición no se cumple ya que el carácter `b` no se encuentra dentro de la cadena de caracteres.

Y el caso contrario:

```{code-cell} ipython3
print("b" not in "Hola")
```

En este caso, la condición se cumple ya que el carácter `b` no se encuentra dentro de la cadena de caracteres.

## A continuación...

Ahora que ya tenemos claro cómo realizar operaciones que determinen si una condición es verdadera o falsa, estamos preparados para empezar a utilizar las estructuras de control de flujo. En el siguiente apartado, veremos cómo utilizar las estructuras de control de flujo `if`, `elif` y `else`.
