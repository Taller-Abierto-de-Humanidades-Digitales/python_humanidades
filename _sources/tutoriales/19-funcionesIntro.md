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
# Funciones: Introducción

Hasta ahora, hemos apredido a realizar programas que tiene un comportamiento lineal, que se ejecutan sencuencialmente y de ser necesario repetir una acción, debemos escribir nuevamente el código que la realiza. Esto tiene varios inconvenientes, entre ellos, que el código se hace muy largo y difícil de leer, además, si queremos modificar una de estas acciones, debemos hacerlo sobre cada una de las repeticiones, lo cual es una receta para el desastre. Las funciones son bloques de código que nos permiten agrupar acciones que se repiten y que además nos permiten reutilizarlas en otros programas. Básicamente, una función tiene la intención de realizar una función específica a partir de unos parámetros de entrada y con ello devolver un resultado.

## Definición de una función

La siguiente imagen muestra la estructura de una función en Python:

```{figure} ../_static/imgs/función_estructura.png
---
height: 200px
name: estructura_funcion
---
Estructura de una función en Python
```

Como verás, la sintaxis de una función es bastante simple:

* Se define con la palabra reservada `def`
* Le sigue el nombre de la función. La convención es que se escriba en minúsculas y separando las palabras con guiones bajos.
* Se abre un paréntesis y se escriben los parámetros de entrada de la función, separados por comas. Si la función no tiene parámetros de entrada, se deja el paréntesis vacío.
* Se cierra el paréntesis y se abre un dos puntos.
* Se escribe el código de la función, indentado.

Veamos un ejemplo de una función que no tiene parámetros de entrada:

```{code-cell} ipython
def saludar():
    print("Hola, ¿cómo estás?")

saludar()
```

En este caso, la función `saludar()` no tiene parámetros de entrada, por lo que no hay ningún elemento dentro del paréntesis. La acción, en este caso, es sencillamente imprimir un mensaje en pantalla que dice "Hola, ¿cómo estás?". La función se invoca en la última línea del código escribiendo el nombre de la función y abriendo y cerrando paréntesis.

```{note}
Nota que cuando invocamos la función `saludar()` no estamos haciendo print en la línea (`print(saludar())`), sino que es el bloque de código de la función el que hace el print. 
```

## Pasar valores a una función

Como vimos en la imagen anterior, las funciones pueden tener parámetros de entrada. Un *parámetro* es una "pieza de información" que se pasa a la función para que esta pueda realizar sus acciones. Un *argumento* sería el valor que se le pasa a la función para que ésta lo utilice como parámetro.

Modifiquemos la función anterior para que reciba un nombre y lo imprima en pantalla:

```{code-cell} ipython
def saludar(nombre):
    print(f"Hola {nombre.title()}, ¿cómo estás?")

saludar("Virginia")
```

Ahora la función recibe un valor ("Virginia") y lo utiliza para personalizar el mensaje. Es decir, el *argumento* es "Virginia" y se asigna al *parámetro* `nombre`. Podríamos decir que el *parámetro* es un nombre de variable, y el *argumento* el valor que se le asigna

```{note}
Esta distinción que realizamos no es estrictamente necesaria. De hecho, es común que estos términos se usen como sinónimos. Por esta razón, es posible que encuentres que en algunos libros se usan los términos de manera intercambiable.
```

## Pasar argumentos

Una función suele tener más de un parámetro, por lo que necesitamos definir cómo pasar los argumentos de tal manera que el bloque de código utilice los valores de manera correcta. Para esto, Python nos ofrece varias formas de pasar los argumentos a una función, los cuales veremos con detalle.

### Argumentos posicionales

Este es el método más sencillo de pasar argumentos a una función. Básicamente, el orden de los parámetros es el mismo que el orden de los argumentos. Por ejemplo, si en nuestra función queremos recibir el nombre y la fecha de nacimiento, para regresar un saludo y la edad de la persona, podemos hacer lo siguiente:

```{code-cell} ipython
def saludar(nombre, fecha_nacimiento):
    edad = 2023 - fecha_nacimiento
    print(f"Hola {nombre.title()}, ¿cómo estás? Tienes {edad} años.")

saludar("Virginia", 1990)
```

La función define que requerimos dos valores: un nombre y una fecha. El orden en este caso es fundamental, de otra manera obtendremos un error:

```{code-cell} ipython
saludar(1990, "Virginia")
```

Los argumentos son los mismos, pero al cambiarse el orden la función pasa el valor de la fecha de nacimiento al parámetro `nombre` y el valor del nombre a `fecha_nacimiento`. Obviamente esto tiene como consecuencia que no se pueda calcular la edad porque no se puede restar un string a un entero.

### ¿Cómo facilitar el uso de las funciones?

Debido a que la función es directamente visible por nosotros, conocemos los parámetros y su posición, pero esto no es el caso en todas las situaciones. De hecho, suele ser la excepción. Para lograr que cualquier persona o nosotros mismos podamos reutilizar la función, es importante documentarla y explicar qué hace y qué parámetros recibe, su orden y su tipo. Esto se puede hacer con comentarios en el código:

```{code-cell} ipython
def saludar(nombre, fecha_nacimiento):
    """Saluda a una persona y le dice su edad.
    
    Parámetros
    ----------
    nombre: str
        Nombre de la persona a saludar
    fecha_nacimiento: int
        Año de nacimiento de la persona
    """
    edad = 2023 - fecha_nacimiento
    print(f"Hola {nombre.title()}, ¿cómo estás? Tienes {edad} años.")

saludar("Virginia", 1990)
```

La mayoría de editores de código en la actualidad tienen funcionalidades que permiten ver la documentación de una función. Por ejemplo, en VS Code, podemos situar el cursor sobre el nombre de la función y ver la documentación en una ventana emergente:

```{figure} ../_static/imgs/parametros.png
---
height: 200px
name: parametros
---
Documentación de una función en VS Code
```

También podemos utilizar la función `help()` para ver la documentación de una función:

```{code-cell} ipython
help(saludar)
```

```{admonition} Documentación
:class: tip
La labor de documentar las funciones es una de las tareas más importantes que debemos realizar cuando elaboramos un programa. Incluso si lo hacemos para nosotros sin la intención de distribuirlo, podemos olvidarnos de los detalles y no recordar qué hace una función en un tiempo. Por esta razón, es importante documentar las funciones para que podamos entenderlas en el futuro. Por otra parte, una documentación detallada (aunque no excesiva) es evidencia de un procedimiento metódico y profesional.
```

### Argumentos con palabras clave

También podemos pasar argumentos asociando directamente el valor a un parámetro. Esto se conoce como *argumentos con palabras clave*. Por ejemplo, podemos hacer lo siguiente:

```{code-cell} ipython
saludar(nombre="Virginia", fecha_nacimiento=1990)
```

En este caso, el orden de los argumentos no importa, ya que se asocia directamente el valor a un parámetro. Esto es útil cuando tenemos muchas funciones y no queremos recordar el orden de los parámetros.

```{code-cell} ipython
saludar(fecha_nacimiento=1990, nombre="Virginia")
```

Incluso, no es necesario que todos los argumentos sean con palabras clave, podemos mezclarlos:

```{code-cell} ipython
saludar("Virginia", fecha_nacimiento=1990)
```

Ten en cuenta que en este último caso el argumento "Virginia" se asigna posicionalmente, mientras el argumento `fecha_nacimiento` se asigna con palabras clave.

### Argumentos predeterminados

Otra forma útil de definir parámetros consiste en asignar un valor predeterminado. En este caso, a menos que se pase un argumento diferente, Python tomará el valor predeterminado para ejecutar el bloque de código de la función. Por ejemplo, podemos modificar la función anterior para incluir un valor que puede ser muy común, por ejemplo, lugar de nacimiento:

```{code-cell} ipython
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
    edad = 2023 - fecha_nacimiento
    print(f"Hola {nombre.title()}, ¿cómo estás? Tienes {edad} años y naciste en {lugar_de_nacimiento.title()}.")

saludar("Virginia", 1990)
```

Notarás que no necesitamos pasar un argumento para el parámetro `lugar_de_nacimiento`, ya que Python toma el valor predeterminado. Sin embargo, si queremos cambiar el valor predeterminado, podemos hacerlo:

```{code-cell} ipython
saludar("Virginia", 1990, lugar_de_nacimiento="México")
```

```{admonition} Importante
:class: important
Los argumentos con palabras clave deben ir después de los argumentos posicionales, de otra manera tendrás un error de sintaxis.
```

### Errores comunes

A continuación, veremos algunos errores comunes que se pueden presentar al pasar argumentos a una función.

#### Número incorrecto de argumentos

Si pasamos un número incorrecto de argumentos, Python nos arrojará un error indicando que falta un argumento o que hay un argumento de más:

```{code-cell} ipython
saludar("Virginia")
```

```{code-cell} ipython
saludar("Virginia", 1990, "México", "Michoacán")
```

#### Argumentos con palabras clave incorrectos

Si pasamos un argumento con palabras clave incorrecto, Python nos arrojará un error indicando que el parámetro no existe:

```{code-cell} ipython
saludar("Virginia", 1990, lugar_de_nacimiento="México", lugar_de_residencia="Michoacán")
```

Este error también puede presentarse si escribimos mal el nombre del parámetro:

```{code-cell} ipython
saludar("Virginia", 1990, nacimiento="México")
```

## En resumen

Las funciones son bloques de código que podemos reutilizar en cualquier parte del programa o incluso en otros programas. Hemos visto la sintaxis de las funciones y aprendimos a evitar algunos errores comunes al pasar argumentos a una función. En la siguiente lección, veremos cómo podemos lograr recibir información directamente del usuario del programa con el método `input`.
