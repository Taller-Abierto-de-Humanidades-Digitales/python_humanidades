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

# Iteraciones (*for loops*)

Después de haber explorado las variables, tipos básicos de datos, operaciones con textos y listas, podemos iniciar nuestro camino hacia la automatización de tareas. Uno de estos procesos es la iteración, repetición o *loops*.

Efectivamente, una de las tareas más directas en las que nos puede ayudar una computador es la de poder ejecutar tareas repetitivas de manera lógica. Una iteración, en términos simples, es un proceso en el cual se repite una tarea una y otra vez, hasta que se cumpla una condición. En el caso de un *for loop*, esta condición es que se hayan recorrido todos los elementos de una lista o un rango de números.

Vamos a ver esto con un poco más de detalle.

## Iterando sobre una lista

Vamos a crear una lista con los nombres de los países de Sudamérica:

```{code-cell}
paises = ['Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Perú', 'Surinam', 'Uruguay', 'Venezuela']
```

Ahora, vamos a iterar sobre esta lista, imprimiendo cada uno de los elementos:

```{code-cell}
for pais in paises:
    print(pais)
```

Vamos a ver qué está pasando en este código. La primera línea es la que define el *loop*:

```{code-cell}
:tags: [remove-output]
for pais in paises:
```

La palabra  `for` indica que vamos a iterar sobre una lista. Podemos entender el valor `pais` como una variable que va a tomar el valor de cada uno de los elementos de la lista `paises`. En cada iteración, el valor de `pais` va a cambiar, y va a tomar el valor del siguiente elemento de la lista. En la primera iteración, `pais` va a tomar el valor de `'Argentina'`, en la segunda, el valor de `'Bolivia'`, y así sucesivamente.

La segunda línea es la que se va a ejecutar en cada iteración:

```{code-cell}
:tags: [remove-output]
    print(pais)
```

En este caso, estamos imprimiendo el valor de la variable `pais`. En la primera iteración, se va a imprimir `'Argentina'`, en la segunda, `'Bolivia'`, y así sucesivamente. Técnicamente, podemos hacer lo que queramos con esta variable, dependiendo de su tipo de dato y obviamente de lo que queramos lograr. En este caso, solo queremos imprimir el valor de la variable.

¡Y listo! Ya hemos iterado sobre una lista. Veamos ahora un poco más sobre la sintaxis de los *loops*.

## Sintaxis de los *loops*

La sintaxis de los *loops* es muy simple. En general, se define de la siguiente manera:

```{code-cell}
:tags: [remove-output]
for variable in lista:
    # hacer algo
```

Presta atención a los elementos de esta sintaxis.

Por una parte, la primera línea se escribe siempre de la forma `for variable in lista`, es decir, siempre utilizamos los términos `for` e `in`. Estos términos son palabras claves del lenguaje Python, y no pueden ser reemplazados por otros ni pueden usarse como nombres de variables.

La línea además termina con dos puntos (`:`). Esto es muy importante, ya que indica que la línea es una definición de un *loop*, y que la siguiente línea es la primera línea de código que se va a ejecutar en cada iteración.

A partir de la segunda línea, se escribe el bloque de código que queremos que se ejecute en cada iteración. Este bloque de código debe estar indentado, es decir, debe tener un tabulador o cuatro espacios al comienzo de cada línea.

Si no tenemos en cuenta lo anterior podemos encontrar los siguientes errores:

### Olvidarse de indentar

```{code-cell}
for pais in paises:
print(pais)
```

Este error de indentación muestra que no hemos dado los espacios necesarios para que Python entienda que este es un bloque de código. Esto lo sabe porque espera que después de los dos puntos exista un bloque de código o al menos una instrucción.

### Olvidarse de indentar líneas adicionales

```{code-cell}
for pais in paises:
    print(pais)
print(f'{pais} es una país sudamericano.')
```

En este caso no hay un error de sintaxis, pero el resultado no es el que esperábamos. La idea original del código es que se mostrara en pantalla lo siguiente:

```shell
Argentina
Argentina es un país sudamericano
Bolivia
Bolivia es un país sudamericano
Brasil
Brasil es un país sudamericano
...
Uruguay
Uruguay es un país sudamericano
Venezuela
Venezuela es un país sudamericano
```

En lugar de eso, solamente nos muestra el último país de la lista. Esto se debe a un error lógico.

### Indentación innecesaria

También puede suceder lo contrario, que se haya indentado una línea que no debía estar indentada:

```{code-cell}
:tags: [output_scroll]
for pais in paises:
    print(pais)
    print(f'Ha finalizado la lista de países sudamericanos.')
```

Como podemos observar, el resultado no es el esperado. Queríamos que al finalizar de mostrarse cada elemento de la lista se mostrara el mensaje `Ha finalizado la lista de países sudamericanos.`. Una mala indentación hace que el mensaje se muestre con cada iteración.

### Olvidarse de los dos puntos

```{code-cell}
for pais in paises
    print(pais)
```

En este caso, nos enfrentamos a un error en la sintaxis. Python entiende que se está usando la instrucción `for`, pero requiere que se le indique que se está definiendo un *loop* con los dos puntos.

## Listas numéricas o por rango

Son muchas las ocasiones en las que necesitamos iterar sobre una serie de números, es decir, sobre una lista numérica. Si esta lista sigue una secuencia numérica, podemos utilizar la función `range()` para crearla. Esta función recibe dos parámetros, el número inicial y el final de la secuencia. Por ejemplo:

```{code-cell}
for numero in range(1, 5):
    print(numero)
```

Notemos que el número final no se incluye en la lista. En este caso, la lista va a contener los números del 1 al 4. Es decir, tenemos que tener en cuenta que la lista dentro del rango incluye el número inicial y excluye el número final.

También podemos crear sencuencias numéricas para mostrar los números pares, por ejemplo:

```{code-cell}
for numero in range(2, 11, 2):
    print(numero)
```

En este caso, el tercer parámetro de la función `range()` indica el *step*, es decir, el número de unidades que se va a avanzar en cada iteración. Si el *step* es 2 significa que se va a avanzar de 2 en 2. Claramente podríamos hacer algo similar para mostrar los números impares:

```{code-cell}
for numero in range(1, 11, 2):
    print(numero)
```

Siguiendo este mismo método podemos crear secuencias numéricas inversas si añadimos un argumento de pasos negativo. Por ejemplo, si queremos mostrar los números del 5 al 1, podemos hacer lo siguiente:

```{code-cell}
for numero in range(5, 0, -1):
    print(numero)
```

## Llenar listas con *loops*

Uno de los procesos que podemos hacer con los *loops* consiste en llenar listas vacías. Por ejemplo, si queremos crear una lista con las iniciales de cada uno de los países sudamericanos, podemos hacer lo siguiente:

```{code-cell}
iniciales = []
for pais in paises:
    iniciales.append(pais[0])
print(iniciales)
```

Como puedes ver, aquí combinamos varias operaciones que hemos aprendido a lo largo del curso:

* Creamos una lista vacía.
* Iteramos sobre la lista `paises`.
* "Recortamos" una cadena de texto para obtener la primera letra.
* Añadimos la letra a la lista vacía.

## *Loops* anidados

Un *loop* anidado se refiere a una iteración dentro de otra iteración. Revisa el siguiente ejemplo:

```{code-cell}

frase = "Era la estación de las lluvias en Bangkok".split()

for palabra in frase:
    for letra in palabra:
        print(letra, end=' ')
    print()
```

En este ejemplo, tomamos una lista obtenida a partir de aplicar el método `split()` a la frase. El primer *loop* itera sobre cada una de las palabras de la lista, en tanto el segundo *loop* itera sobre cada una de las letras de cada palabra. Por cada iteración del segundo *loop* se imprime la letra y se agrega un espacio en blanco. Al finalizar la iteración del segundo *loop* se imprime un salto de línea.

## *Loops* sobre cadenas de caracteres

En el ejemplo anterior realizamos el `split` de la frase antes de iterar sobre ella. ¿Qué pasaría si no hicieramos esto? Veamos:

```{code-cell}
:tags: [output_scroll]
frase = "Era la estación de las lluvias en Bangkok"

for palabra in frase:
    print(palabra)
```

Esto sucede porque la cadena de caracteres es iterable. Es importante tener en cuenta esto porque nos podemos enfrentar a situaciones donde este no sería el resultado esperado. 

## Iterar sobre partes de una lista

Podemos tener la posibilidad de iterar solamente sobre una parte de la lista, lo cual en general es una práctica recomendable si tenemos una gran cantidad de datos y queremos probar nuestro código con una pequeña muestra. Para ello podemos utilizar el operador de *slicing*:

```{code-cell}
for pais in paises[0:3]:
    print(pais)
```

En este caso, estamos iterando sobre los tres primeros elementos de la lista `paises`. Si queremos iterar sobre los tres últimos elementos, podemos hacer lo siguiente:

```{code-cell}
for pais in paises[-3:]:
    print(pais)
```

## Iterar en una lista anidada

En ocasiones, las listas pueden contener otras listas. En este caso, podemos iterar sobre cada una de las listas anidadas. Por ejemplo, si tenemos una lista de listas con los nombres de los países sudamericanos y sus capitales, podemos iterar sobre cada una de las listas anidadas:

```{code-cell}
paises_capitales = [
    ['Argentina', 'Buenos Aires'],
    ['Bolivia', 'La Paz'],
    ['Brasil', 'Brasilia'],
    ['Chile', 'Santiago de Chile'],
    ['Colombia', 'Bogotá'],
    ['Ecuador', 'Quito'],
    ['Guyana', 'Georgetown'],
    ['Paraguay', 'Asunción'],
    ['Perú', 'Lima'],
    ['Surinam', 'Paramaribo'],
    ['Uruguay', 'Montevideo'],
    ['Venezuela', 'Caracas']
]

for pais_capital in paises_capitales:
    print(pais_capital)
```

En este caso, la variable `pais_capital` es una lista anidada que contiene el nombre del país y su capital. Teniendo en cuenta esto, podríamos iterar sobre cada una de las listas anidadas para obtener su capital:

```{code-cell}
for pais_capital in paises_capitales:
    print(pais_capital[1])
```

Esto se logra porque `print()` está recibiendo un argumento de tipo lista, por lo que nos es posible acceder a su segundo elemento a través de un índice.

## Listas de comprensión

Una forma eficiente para crear listas es a través de las denominadas listas de comprensión. Estas nos permite crear una lista a través de iteraciones en una sola línea de código. Veamos cómo funciona.

Recordemos cómo llenamos una lista vacía a través de un loop:

```{code-cell}
iniciales = []
for pais in paises:
    iniciales.append(pais[0])
print(iniciales)
```

Ahora bien, una lista de comprensión nos permite hacerlo en una sola línea de código:

```{code-cell}
iniciales = [pais[0] for pais in paises]
print(iniciales)
```

La sintaxis de este tipo de listas es la siguiente:

```{code-cell}
:tags: [remove-output]
[nombre_variable for nombre_variable in nombre_lista]
```

Observa que estamos utilizando los mismos elementos de un *loop* tradicional, pero simplemente cambiamos el orden para que todo se pueda escribir en una sola línea.
