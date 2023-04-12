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

# Función `input()`

La función `input()` tiene el propósito de recibir un valor desde la consola por un usuario. Esta función es muy útil para recibir datos de entrada sin tener que escribirlos en una variable. Retomemots nuestra función `saludar()` y supongamos que el programa lo está usando "Juan", quien nació en 1980 [^1].

```{code-cell} ipython3
def saludar(nombre, fecha_nacimiento=1990, lugar_de_nacimiento="Colombia"):
    """Saluda a una persona y le dice su edad.
    
    Parámetros
    ----------
    nombre: str
        Nombre de la persona a saludar
    fecha_nacimiento: int
        Año de nacimiento de la persona
    lugar_de_nacimiento: str
        Lugar de nacimiento de la persona
    """
    edad = 2023 - fecha_nacimiento
    print(f"Hola {nombre.title()}, ¿cómo estás? Tienes {edad} años y naciste en {lugar_de_nacimiento.title()}.")

```

Podemos entonces pedirle su nombre al usuario y saludarlo:

``` python
nombre = input("Ingresa tu nombre: ")
saludar(nombre)
```

```{code-cell} ipython3
:tags: [remove-input]
nombre = "Juan"
saludar(nombre)
```

La función `input()` asigna cualquier valor que hayas pasado en la consola como una cadena de caracteres y la asigna a la variable asociada, en este caso `nombre`.

## Aceptar valores numéricos

En nuestro ejemplo anterior tuvimos que modificar el parámetro `fecha_nacimiento` para que el programa funcionara. Si no lo hubiéramos hecho de esa manera, obtendríamos el siguiente error:

``` python
nombre = input("Ingresa tu nombre: ")
fecha_nacimiento = input("Ingresa tu año de nacimiento: ")

saludar(nombre, fecha_nacimiento)
```

```{code-cell} ipython3
:tags: [remove-input]
nombre = "Juan"
fecha_nacimiento = "1980"

saludar(nombre, fecha_nacimiento)
```

Este error se debe a que la función `input()` no recibe otro tipo de valor diferente a un texto. Por ello, para lidiar con esto, debemos convertir el valor que recibimos de la consola a un número entero. Esto lo podemos hacer con la función `int()` directamente en el `input()`:

``` python
nombre = input("Ingresa tu nombre: ")
fecha_nacimiento = int(input("Ingresa tu año de nacimiento: "))
saludar(nombre, fecha_nacimiento)
```

```{code-cell} ipython3
:tags: [remove-input]
nombre = "Juan"
fecha_nacimiento = 1980

saludar(nombre, fecha_nacimiento)
```

O, podemos hacerlo directamente en la función:

```{code-cell} ipython3
:tags: [remove-output]
def saludar(nombre, fecha_nacimiento, lugar_de_nacimiento="Colombia"):
    """Saluda a una persona y le dice su edad.
    
    Parámetros
    ----------
    nombre: str
        Nombre de la persona a saludar
    fecha_nacimiento: int
        Año de nacimiento de la persona
    lugar_de_nacimiento: str
        Lugar de nacimiento de la persona
    """
    edad = 2023 - int(fecha_nacimiento) # Convertimos el valor a entero
    print(f"Hola {nombre.title()}, ¿cómo estás? Tienes {edad} años y naciste en {lugar_de_nacimiento.title()}.")


nombre = input("Ingresa tu nombre: ")
fecha_nacimiento = input("Ingresa tu año de nacimiento: ")
saludar(nombre, fecha_nacimiento)
```

```{code-cell} ipython3
:tags: [remove-input]
nombre = "Juan"
fecha_nacimiento = "1980"

saludar(nombre, fecha_nacimiento)
```

Así ya no tendremos problemas con el tipo de dato que recibimos de la consola.

## Notas

[^1]: Debido a que no contamos con una consola de entrada en este cuaderno, hemos asignado los valores directamente para simular el comportamiento de la función `input()`.
