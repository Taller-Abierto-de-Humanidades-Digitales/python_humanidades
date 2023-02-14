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

# Operaciones con cadenas de caracteres

Una cadena de caracteres no es otra cosa sino el conjunto de caracteres que, en el lenguaje natural, forman una palabra, frase o texto. Como ya vimos, las cadenas se representan por comillas dobles o sencillas:

```{code-cell}
cuento = "Arrasado el jardín, profanados los cálices y las aras, entraron a caballo los hunos en la biblioteca monástica y rompieron los libros incomprensibles y los vituperaron y los quemaron, acaso temerosos de que las letras encubrieran blasfemias contra su dios, que era una cimitarra de hierro. Jorge Luis Borges, 'Los teólogos'."
```

Para nosotros, esta frase tiene un sentido, unos personajes, una historia. Para la computadora, en cambio, solamente es la suma de caracteres que la componen. Al manipular estas cadenas, podemos realizar operaciones que nos ayuden a extraer información de ellas.

## Concatenación

La concatenación es la operación que permite unir dos cadenas de caracteres. En Python, se realiza con el operador `+`:

```{code-cell}
print("Arrasado" + " " + "el" + " " + "jardín")
```

Observa que el espacio entre palabras está representado por una cadena de caracteres vacía, que es lo mismo que una cadena de caracteres que contiene un solo espacio. Si no lo hacemos así, la frase resultante no tendrá espacios entre palabras:

```{code-cell}
print("Arrasado" + "el" + "jardín")
```

Otra opción es que cada palabra cuente con los espacios que la separan de las demás:

```{code-cell}
print("Arrasado " + "el " + "jardín")
```

## Obtener el largo de una cadena

Debido a que las cadenas de caracteres son un conjunto de caracteres, podemos obtener el número de caracteres que la componen. Para ello, utilizamos la función `len()`:

```{code-cell}
print(len(cuento))
```

Esto puede ser útil al momento de comparar textos, por ejemplo, dos traducciones de Hamlet. Una (`trad1`) proveniente de una edición espúrea y la otra (`trad2`) obtenida de la edición de Inarco Celenio, impresa en Madrid en 1798 y digitalizada por la Biblioteca Virtual Cervantes:

```{code-cell}

trad1 = """
        FORTINBRÁS Cuatro capitanes portarán a Hamlet marcialmente al catafalco, pues, de habérsele brindado, habría sido un gran rey. Su muerte será honrada con sones militares y ritos de guerrero. Llevaos los cadáveres. Esta escena, más propia de batalla, aquí disuena. Vamos, que disparen los soldados
        """

trad2 = """
        FORTIMBRÁS.-  Cuatro de mis capitanes lleven al túmulo el cuerpo de Hamlet con las insignias correspondientes a un guerrero. ¡Ah! Si él hubiese ocupado el trono, sin duda hubiera sido un excelente Monarca... Resuene la música militar por donde pase la pompa fúnebre, y hagánsele todos los honores de la guerra... Quitad, quitad de ahí esos cadáveres. Espectáculo tan sangriento, más es propio de un campo de batalla que de este sitio... Y vosotros, haced que salude con descargas todo el ejército.
        """

diff = len(trad2) - len(trad1)
print(f"La diferencia de longitud entre las dos traducciones es de {diff} caracteres")
```

En este ejemplo, la comparación se hace con el último diálogo de la obra, pero lo mismo podría realizarse con un conjunto de diálogos, o con todo el texto. De esta manera podríamos identificar cuánta es la "pérdida de materia" que se está produciendo en las traducciones a través del tiempo.

```{admonition} Sobre las cadenas de texto
:class: tip
Bien podríamos intentar un acercamiento similar para las palabras o frases, pero en ese caso es mejor utilizar una aproximación más "sofisticada" que pueda tener en cuenta el valor lingüístico de una palabra y diferenciarla de un conector, un pronombre o un signo de puntuación.
```

## Acceder a una posición de una cadena

En ocasiones es necesario acceder a una de las posiciones de una cadena, por ejemplo el último caracter de una palabra para saber si es plural o no. Para ello, utilizamos la notación de corchetes (`[]`) y el índice de la posición que queremos acceder:

```{code-cell}
sing = "casa"
plur = "casas"

final = plur[-1]
print(f"La palabra {plur} es plural porque su último caracter es {final}")
```

*Este es un acercamiento muy directo a este problema, pero no es el mejor. Posteriormente veremos cómo podemos utilizar expresiones regulares para resolverlo de una manera más eficiente.*

También podemos extraer segmentos de una cadena. Para ello utilizamos un rango de índices, separados por dos puntos (`:`):

```{code-cell}
print("Arrasado el jardín"[0:8])
```

En este caso, el primer índice indica el inicio del segmento y el segundo el final. Si no se especifica el primer índice, se asume que es el primero:

```{code-cell}
print("Arrasado el jardín"[:8])
```

Si no se especifica el segundo índice, se asume que es el último:

```{code-cell}
print("Arrasado el jardín"[8:])
```

## Reemplazar una cadena por otra

En ocasiones es necesario reemplazar una cadena por otra. Por ejemplo, si queremos eliminar los signos de puntuación de un texto, podemos hacerlo de la siguiente manera:

```{code-cell}
print("Arrasado el jardín.".replace(".", ""))
```

En este caso, el método `replace()` recibe dos parámetros: el primero es la cadena que queremos reemplazar y el segundo es la cadena que reemplazará a la primera. En este caso, el primer parámetro es un punto (`.`) y el segundo es una cadena vacía (`""`). Lo mismo puede hacerse con otros caracteres, como comas, signos de interrogación, etc. Por ejemplo, si queremos eliminar los puntos y las comas de las traducciones de Hamlet y luego comparar sus longitudes:

```{code-cell}
trad1 = trad1.replace(".", "").replace(",", "")
trad2 = trad2.replace(".", "").replace(",", "")

diff = len(trad2) - len(trad1)
print(f"La diferencia de longitud entre las dos traducciones es de {diff} caracteres")
```

## Encontrar subcadenas en una cadena

El método find() nos permite encontrar la posición de una subcadena dentro de una cadena. Por ejemplo, si queremos saber en qué posición se encuentra la palabra "jardín" en la frase "Arrasado el jardín":

```{code-cell}
print("Arrasado el jardín".find("jardín"))
```

Si la subcadena no se encuentra, el método devuelve el valor `-1`:

```{code-cell}
print("Arrasado el jardín".find("dios"))
```

```{admonition} Sobre el método find()
:class: tip
El método find() no es una función de búsqueda, es decir, encuentra la posición de una subcadena dentro de una cadena, pero no puede determinar cuántas veces se repite en un texto.
```

## Método `count()` para encontrar subcadenas

El método count() nos permite contar cuántas coincidencias hay de una subcadena dentro de un texto. Por ejemplo, si queremos saber cuántas veces se repite la preposición 'los' en el texto `cuento`:

```{code-cell}
print(cuento.count("los"))
```

Valga anotar que esta es una coincidencia exacta, es decir, no se consideran las palabras que contengan la subcadena (como por ejemplo 'losa' o 'losas'), ni aquellas que no coincidan en mayúsculas y minúsculas (como por ejemplo 'Los' o 'LOS').

## Métodos de cadenas: `startswith()` y `endswith()`

Los métodos de cadenas son funciones que se aplican a una cadena. Por ejemplo, si queremos saber si una cadena comienza con una subcadena, podemos utilizar el método `startswith()`:

```{code-cell}
print("Arrasado el jardín".startswith("Arrasado"))
```

Si la cadena no comienza con la subcadena, el método devuelve `False`:

```{code-cell}
print("Arrasado el jardín".startswith("arrasado"))
```

Si queremos saber si una cadena termina con una subcadena, podemos utilizar el método `endswith()`:

```{code-cell}
print("Arrasado el jardín".endswith("jardín"))
```

Si la cadena no termina con la subcadena, el método devuelve `False`:

```{code-cell}
print("Arrasado el jardín".endswith("jardín."))
```

Si queremos saber si una cadena contiene una subcadena, podemos utilizar el método `in`:

```{code-cell}
print("jardín" in "Arrasado el jardín")
```

Si la cadena no contiene la subcadena, el método devuelve `False`:

```{code-cell}
print("cimitarra" in "Arrasado el jardín")
```

Estos métodos pueden aplicarse a textos de cualquier extensión. Por ejemplo, podemos usarlos en nuestro `cuento`:

```{code-cell}
print(cuento.startswith("En un lugar de la Mancha"))
print(cuento.endswith("Jorge Luis Borges, 'Los teólogos'."))
print("cimitarra" in cuento)
```

## Métodos de cadenas: `upper()` y `lower()`

Los métodos `upper()` y `lower()` nos permiten convertir una cadena a mayúsculas o minúsculas, respectivamente. Por ejemplo, si queremos convertir la frase "Arrasado el jardín" a mayúsculas:

```{code-cell}
print("Arrasado el jardín".upper())
```

Si queremos convertir la frase "Arrasado el jardín" a minúsculas:

```{code-cell}
print("Arrasado el jardín".lower())
```

## Métodos de cadenas: `capitalize()`, `title()` y `swapcase()`

Los métodos `capitalize()`, `title()` y `swapcase()` nos permiten convertir una cadena a mayúsculas y minúsculas. Por ejemplo, si queremos convertir el nombre "AGUSTÍN GONZÁLEZ HIRIARTE" a mayúsculas en la primera letra:

```{code-cell}
print("AGUSTÍN GONZÁLEZ HIRIARTE".capitalize())
```

Si en cambio, queremos convertir el nombre "AGUSTÍN GONZÁLEZ HIRIARTE" a mayúsculas en la primera letra de cada palabra:

```{code-cell}
print("AGUSTÍN GONZÁLEZ HIRIARTE".title())
```

Si en cambio, queremos convertir el nombre "Agustín González Hiriarte" a minúsculas en la primera letra de cada palabra y a mayúsculas en el resto:

```{code-cell}
print("Agustín González Hiriarte".swapcase())
```

## Métodos de cadenas: `strip()`, `replace()` y `split()`

Los métodos `strip()`, `replace()` y `split()` nos permiten eliminar espacios en blanco, reemplazar una subcadena por otra y dividir una cadena en varias subcadenas, respectivamente. Por ejemplo, si queremos eliminar los espacios en blanco de la frase " Arrasado el jardín ":

```{code-cell}
print(" Arrasado el jardín ".strip())
```

Si en cambio, queremos reemplazar la palabra "jardín" por la palabra "casa" en la frase "Arrasado el jardín":

```{code-cell}
print("Arrasado el jardín".replace("jardín", "casa"))
```

Si en cambio, queremos dividir la frase "Arrasado el jardín" en varias subcadenas:

```{code-cell}
print("Arrasado el jardín".split())
```

El método split() puede utilizar cualquier otro separador, por ejemplo, podemos usar la coma para separar frases en el `cuento`:

```{code-cell}
print(cuento.split(","))
```

## Métodos de cadenas: `isalpha()`, `isalnum()` y `isdecimal()`

Los métodos `isalpha()`, `isalnum()` y `isdecimal()` nos permiten saber si una cadena está formada por letras, letras y números o números, respectivamente. Por ejemplo, si queremos saber si la frase "Arrasado el jardín" está formada únicamente por letras:

```{code-cell}
print("Arrasado el jardín".isalpha())
```

¿Por qué el resultado es `False`? Porque la frase "Arrasando el jardín" contiene espacios en blanco, que no son letras.

Si en cambio, queremos saber si la frase "Arrasado el jardín" está formada por letras y números:

```{code-cell}
print("Arrasado el jardín".isalnum())
```

Si en cambio, queremos saber si la frase "Arrasado el jardín" está formada por números:

```{code-cell}
print("Arrasado el jardín".isdecimal())
```

Como habrás notado, estas funciones no son muy útiles al momento de trabajar con oraciones, pero sí lo son cuando trabajamos con palabras de manera individual. Por ejemplo:

```{code-cell}
palabra = "Arrasado"
signo = "."
fecha = "1894"

print(palabra.isalpha())
print(signo.isalpha())
print(fecha.isdecimal())
```

Estos métodos tendrán más sentido cuando realicemos operaciones sobre listados de palabras y hagamos uso de procesos como iteraciones y condicionales.

## Conclusión

Los métodos aquí mencionados son apenas unos cuantos de los que se encuentran disponibles en Python. Un listado completo de estos métodos se puede encontrar en la [documentación oficial](https://docs.python.org/3/library/stdtypes.html#string-methods) y también en [W3Schools](https://www.w3schools.com/python/python_ref_string.asp).

Algunos métodos adicionales (como `join()`, `encode()`, `islower()`, `isupper()`, entre otros) los exploraremos en tanto avancemos con el curso.
