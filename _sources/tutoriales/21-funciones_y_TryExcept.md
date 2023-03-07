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

# Control de errores con `Try` `Except`

Como vimos en la sección previa, una función tiene muchas posibilidades de fallar. Una forma de intentar controlar los errores e identificar los posibles problemas es utilizar el comando `try` y `except`. Este comando permite que el programa se detenga cuando encuentre un error o que continúe con el programa en caso de que eso sea lo que queramos.

Supongamos, por ejemplo, que nuestro usuario ingresa todos los valores, pero en la fecha de nacimiento comete un error y no escribe un número sino una cadena de caracteres. En ese caso, el programa se detendrá y no podremos continuar. Podemos evitar esto utilizando el comando `try` y `except`:

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
    try:
        edad = 2023 - fecha_nacimiento
        print(f"Hola {nombre.title()}, ¿cómo estás? Tienes {edad} años y naciste en {lugar_de_nacimiento.title()}.")
    except:
        print("No se pudo calcular la edad. Verifica que la fecha de nacimiento ingresada ({fecha_nacimiento}) sea un número.")

```

Si el usuario ingresara de manera incorrecta su información, este sería el resultado

```{code-cell} ipython3
:tags: [remove-input]
nombre = "Juan"
fecha_nacimiento = "marzo de 1980"

saludar(nombre, fecha_nacimiento)
```

No obstante, usar `try` y `except` de esta manera no es la mejor forma de controlar los errores. En el ejemplo anterior, el programa no se detiene, pero tampoco nos dice qué fue lo que falló. Para esto, podemos utilizar el comando `raise`:

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
    try:
        edad = 2023 - fecha_nacimiento
        print(f"Hola {nombre.title()}, ¿cómo estás? Tienes {edad} años y naciste en {lugar_de_nacimiento.title()}.")
    except:
        print("No se pudo calcular la edad. Verifica que la fecha de nacimiento ingresada ({fecha_nacimiento}) sea un número.")
        raise
```

El error se muestra de esta manera:

```{code-cell} ipython3
:tags: [remove-input]
nombre = "Juan"
fecha_nacimiento = "marzo de 1980"

saludar(nombre, fecha_nacimiento)
```

En este caso, el programa se detiene y necesita ejecutarse nuevamente para corregir el error.

Otra opción consiste en identificar específicamente un tipo de error que podemos controlar. Para el ejemplo que hemos usado, el error `TypeError` es el más adecuado:

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
    try:
        edad = 2023 - fecha_nacimiento
        print(f"Hola {nombre.title()}, ¿cómo estás? Tienes {edad} años y naciste en {lugar_de_nacimiento.title()}.")
    except TypeError:
        print("No se pudo calcular la edad. Verifica que la fecha de nacimiento ingresada ({fecha_nacimiento}) sea un número.")
        raise
```

El resultado es idéntico a la primera forma que usamos:

```{code-cell} ipython3
:tags: [remove-input]
nombre = "Juan"
fecha_nacimiento = "marzo de 1980"

saludar(nombre, fecha_nacimiento)
```

No obstante, con eso nos evitamos que el programa se detenga por otros errores que podrían ser saltados o, al contrario, que continúe con el programa cuando no es lo que queremos.
