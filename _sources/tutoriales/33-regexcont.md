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
# Funciones de la librería `re`

En la sección anterior vimos el funcionamiento de la función `findall` de la librería `re` y muy someramente aplicamos la función `match`. La librería `re` tiene otras funciones que son de mucha utilidad para trabajar con cadenas de texto de manera eficiente. En esta sección veremos las funciones `search`, `match`, `group`, `split`, `sub` y `compile`.

## Función `search`

La función `search` es muy similar a la función `findall` que vimos en la sección anterior. La función `search` busca en una cadena de texto la primera ocurrencia de una expresión regular y devuelve un objeto de tipo `Match` que contiene la posición de la cadena de texto donde se encontró la primera ocurrencia de la expresión regular. Si no se encuentra ninguna ocurrencia, la función devuelve `None`.

Tomemos esta vez todo el texto del archivo `quijote.txt` y busquemos la primera ocurrencia de la palabra `caballero`:

```{code-cell} ipython3
import re
import os

with open("../archivos/txt/el_quijote.txt", "r", encoding="utf-8") as f:
    texto = f.read()

busqueda = re.search(r"caballero", texto)
print(busqueda)
```

Como verás, no se retorna un listado de coincidencias, sino un objeto de tipo `Match`. Para acceder a la posición donde se encontró la primera ocurrencia de la expresión regular, se utiliza el método `start` del objeto `Match`:

```{code-cell} ipython3
busqueda.start()
```

Ahora, el resultado, como notarás, es un número entero que indica la posición donde se encontró la primera ocurrencia de la expresión regular. Esto puede ser útil para extraer una porción de texto de una cadena de texto. Por ejemplo, si queremos extraer los 50 caracteres previos y posteriores a la primera ocurrencia de la palabra `caballero`, podemos hacer lo siguiente:

```{code-cell} ipython3
texto[busqueda.start()-50:busqueda.start()+50]
```

Existen otras funciones para el objeto `Match` que pueden ser de utilidad. Por ejemplo, el método `end` devuelve la posición donde termina la primera ocurrencia de la expresión regular:

```{code-cell} ipython3
busqueda.end()
```

```{admonition} Observación
:class: tip
En todos los casos, el objeto `Match` retorna la posición de la primera ocurrencia de la expresión regular. Si la expresión regular se repite en la cadena de texto, el objeto `Match` no retorna las posiciones de las demás ocurrencias, por lo que `end()` se refiere a la posición final (2538), pero no a la última coincidencia en el texto.
```

Otra función es `span`, que retorna una tupla con las posiciones inicial y final de la primera ocurrencia de la expresión regular:

```{code-cell} ipython3
busqueda.span()
```

Finalmente, el método `group` retorna la cadena de texto que coincide con la expresión regular:

```{code-cell} ipython3
busqueda.group()
```

El objeto `Match` también tiene un atributo `string` que retorna la cadena de texto donde se realizó la búsqueda:

```{code-cell} ipython3
busqueda.string[100] # Reducimos a 100 caracteres porque de otra forma el resultado es todo El Quijote
```

## Función `match`

La función `match` es muy similar a la función `search`, pero con una diferencia fundamental: `match` busca la expresión regular al comienzo de la cadena de texto, mientras que `search` busca la expresión regular en cualquier parte de la cadena de texto. Veamos un ejemplo:

```{code-cell} ipython3
busqueda = re.match(r"caballero", texto)
print(busqueda)
```

Como puedes ver, la función `match` no encuentra ninguna coincidencia, por lo que retorna `None`. Esto se debe a que la palabra `caballero` no se encuentra al comienzo de la cadena de texto. Si buscamos la palabra `DON` al comienzo de la cadena de texto, la función `match` sí encuentra una coincidencia:

```{code-cell} ipython3
busqueda = re.match(r"DON", texto)
print(busqueda)
```

Aquí podemos utilizar el parámetro `flags` para evitar que la búsqueda sea sensible a mayúsculas y minúsculas:

```{code-cell} ipython3
busqueda = re.match(r"don", texto, flags=re.IGNORECASE)
print(busqueda)
```

Igualmente, hemos utilizado aquí un texto exacto como expresión regular, pero podríamos utilizar una expresión regular un poco más elaborada, por ejemplo, que el texto empiece con mayúscula sostenida y tenga un espacio después de tres letras mayúsculas:

```{code-cell} ipython3
busqueda = re.match(r"[A-Z]{3}\s", texto)
print(busqueda)
```

En general, la función `match` no tiene mucha utilidad con textos largos, pero puede ser útil para validar que una cadena de texto cumpla con ciertas condiciones. Por ejemplo, un correo electrónico debe tener un formato específico, por lo que podemos utilizar la función `match` para validar que un correo electrónico cumpla con ese formato:

```{code-cell} ipython3
correo = "jairoantoniomelo@gmail.com"
busqueda = re.match(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+", correo)
if busqueda:
    print("El correo es válido")
else:
    print("El correo no es válido")
```

Esta es una fórmula muy sencilla, y deja de lado varias opciones como un correo con terminación `.com.co` o `.co`, pero es un buen punto de partida para validar que un correo electrónico tenga un formato válido [^nota1].

Del mismo modo, puedes utilizar la función `match` para saber si un nombre propio es válido o no, independientemente si está compuesto por dos nombres y dos apellidos, un nombre y dos apellidos, o un nombre y un apellido:

```{code-cell} ipython3
nombre = "Jairo Antonio Melo"
busqueda = re.match(r"([A-Z][a-z]+\s[A-Z][a-z]+)|([A-Z][a-z]+)\s([A-Z][a-z]+)", nombre)
if busqueda:
    print("El nombre es válido")
else:
    print("El nombre no es válido")
```

Esta expresión captura dos patrones:

- Un nombre completo con un espacio en medio, donde tanto el nombre como el apellido comienzan con mayúscula sostenida y tienen al menos una letra minúscula.
- Un nombre y un apellido, donde tanto el nombre como el apellido comienzan con mayúscula sostenida y tienen al menos una letra minúscula.

Este patrón regresa un error solamente en caso de que se agregue una sola palabra o que haya una letra mayúsucula en medio de la palabra (ej. `JAiro Antonio Melo`)

### Método `group`

El método `group` es muy útil para extraer información de una cadena de texto. Por ejemplo, en este caso, si el nombre tiene un formato válido (un nombre y dos apellidos), entonces podemos extraer el nombre y el apellido por separado:

```{code-cell} ipython3
nombre = "Jairo Melo Flórez"
busqueda = re.match(r"([A-Z][a-ü]+)\s+([A-Z][a-z]+(?:\s+[A-Z][a-ü]+)*)", nombre)
if busqueda:
    print("El nombre es válido")
    print("Nombre:", busqueda.group(1))
    print("Apellidos:", busqueda.group(2))
else:
    print("El nombre no es válido")
```

En esta expresión regular, el nombre y apellidos se capturan en dos grupos diferentes:

- El primer grupo ```([A-Z][a-ü]+)``` captura el primer nombre, que comienza con una letra mayúscula seguida de letras minúsculas, incluyendo las letras acentuadas o con diéresis.
- El segundo grupo ```([A-Z][a-z]+(?:\s+[A-Z][a-ü]+)*)``` captura los apellidos. Aquí utilizamos un patrón más complejo:
  - ```(?:\s+[A-Z][a-ü]+)*``` captura cero o más grupos de espacios seguidos de una letra mayúscula seguida de letras minúsculas, lo que permite capturar apellidos compuestos o con múltiples palabras.

Ten en cuenta que para que el método `group` funcione, es necesario que la función `match` encuentre un grupo (definido por el metacaracter `(` y `)`). Si no se encuentra ningún grupo, el método `group` retorna un error:

```{code-cell} ipython3
nombre = "Jairo Melo Flórez"
busqueda = re.match(r"[A-Z][a-ü]+\s+[A-Z][a-z]+(?:\s+[A-Z][a-ü]+)*", nombre)
if busqueda:
    print("El nombre es válido")
    print("Nombre:", busqueda.group(1))
    print("Apellidos:", busqueda.group(2))
else:
    print("El nombre no es válido")
```

Aquí regresa un `IndexError` porque no se encontró ningún grupo [^nota2].

## Función `sub`

La función `sub` tiene un funcionamiento similar al método `replace` del objeto `str`, solamente que no se limita a reemplazar las cadenas literales, también lo puede hacer por medio de patrones. Por ejemplo, si alguien ingresa su nombre o apellido de manera incorrecta (p. ej: "JAiro Melo FLórez") es posible corregirlo siguiendo un patrón:

```{code-cell} ipython3
nombre = "JAiro Melo FLórez"
if not re.match(r"([A-Z][a-ü]+)\s+([A-Z][a-z]+(?:\s+[A-Z][a-ü]+)*)", nombre):
    nombre_correcto = re.sub(r"([A-Z])([A-Z][a-ü]+)\b", lambda match: match.group(1) + match.group(2).lower(), nombre)
    print(nombre_correcto)
```

Vamos a explicar un poco lo que hicimos en esta expresión regular:

- ```([A-Z])([A-Z][a-ü]+)``` captura dos grupos:
  - El primer grupo captura una letra mayúscula.
  - El segundo grupo captura una letra mayúscula seguida de letras minúsculas, incluyendo las letras acentuadas o con diéresis.
- ```\b``` es un límite de palabra, que indica que la expresión regular debe terminar en una palabra.
- ```lambda match: match.group(1) + match.group(2).lower()``` es una función anónima que recibe como parámetro el objeto `match` y retorna el primer grupo en mayúscula y el segundo grupo en minúscula.

Otro ejemplo un tanto más sencillo es el siguiente. Supongamos que queremos modificar las fechas que vengan con el formato "AAAA-MM-DD" a "DD/MM/AAAA":

```{code-cell} ipython3
fecha = "La fecha actual es 2023-05-15"
fecha_corregida = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", fecha)
print(fecha_corregida)
```

La expresión regular `r"(\d{4})-(\d{2})-(\d{2})"` busca una cadena de cuatro dígitos, seguida de un guion, luego dos dígitos, otro guion y finalmente dos dígitos más. Utilizamos paréntesis para capturar los tres grupos de dígitos por separado.

En el argumento de sustitución de `re.sub()`, utilizamos `\3`, `\2` y `\1` para referirnos a los grupos capturados respectivamente. Esto nos permite reordenar los grupos de dígitos en el formato deseado.

## Función `finditer`

La función `finditer` es similar a la función `findall`, con la diferencia de que retorna un iterador en lugar de una lista. Esto es útil cuando se trabaja con cadenas de texto muy grandes, ya que no es necesario almacenar todos los resultados en memoria. Por ejemplo, si queremos encontrar todas las coincidencias con la palabra "Dulcinea" en el Quijote, podemos hacer lo siguiente:

```{code-cell} ipython3
contador = 0
for match in re.finditer(r"Dulcinea", texto):
    contador += 1

print(f"La palabra 'Dulcinea' aparece {contador} veces en el Quijote")
```

De la misma manera, podríamos encontrar todas las palabras que tengan el lexema "ilustr" en el Quijote:

```{code-cell} ipython3
for match in re.finditer(r"\bilustr\w+\b", texto):
    print(match.group())
```

O, podremos encontrar aquellas palabras que contengan el sufijo '-ción':

```{code-cell} ipython3
grupos = []
for match in re.finditer(r"\b\w+ción\b", texto):
    grupos.append(match.group())

print(grupos[:10])
```

## Función `split`

La función `split` es similar al método `split` del objeto `str`, con la diferencia de que se puede utilizar una expresión regular para definir el separador. Por ejemplo, si queremos separar una cadena de texto por los caracteres no alfanuméricos (signos de puntuación, admiración, espacios, etc.), podemos hacer lo siguiente:

```{code-cell} ipython3
palabras = re.split(r"\W+", texto)
print(palabras[:10])
```

En este ejemplo es evidente la utilidad de las expresiones regulares para definir patrones de búsqueda. Si utilizáramos el método `split` del objeto `str`, tendríamos que definir un separador para cada uno de los caracteres no alfanuméricos, mientras que en este caso podemos hacerlo con una sola expresión regular.

## Función `compile`

La función `compile` permite compilar una expresión regular para luego utilizarla en otras funciones. Por ejemplo, si queremos encontrar todas las palabras que comienzan con mayúscula, podemos hacer lo siguiente:

```{code-cell} ipython3
patron = re.compile(r"\b[A-Z]\w+\b")

grupos = []

for match in patron.finditer(texto):
    grupos.append(match.group())

print(grupos[:10])
```

La utilidad de esta función es que podemos reutilizar la expresión regular en otras funciones, sin tener que volver a escribirla. Reutilicemos el patrón que usamos para determinar un nombre completo:

```{code-cell} ipython3
patron = re.compile(r"([A-Z][a-ü]+)\s+([A-Z][a-z]+(?:\s+[A-Z][a-ü]+)*)")

patrones = []

for match in patron.finditer(texto):
    patrones.append(match.group())

print(patrones[:10])
```

Y ahora también lo puedo usar en otro texto:

```{code-cell} ipython3
texto2 = "El Quijote de la Mancha es una novela escrita por Miguel de Cervantes Saavedra"
for match in patron.finditer(texto2):
    print(match.group())
```

Esto hace que, por un lado, la escritura de las expresiones sea más fácil de mantener, y por otro lado, que el código sea más eficiente, ya que no tenemos que compilar la expresión regular cada vez que la utilizamos.

## Conclusión

Con estas lecciones abordamos los principios básicos de las expresiones regulares, además de explorar las funciones de la librería `re`. Obviamente, las expresiones regulares son todo un campo de estudio, por lo que no pretendemos, ni mucho menos, cubrirlas por completo en estas lecciones. Lo ideal es que intentes utilizarlas en tus propios proyectos, y que consultes la documentación de Python para profundizar en el tema.

## Ejercicio

Integra los métodos y patrones de las expresiones regulares en la interfaz de búsqueda del proyecto intermedio. Por ejemplo, puedes utilizar una expresión regular para buscar palabras que comiencen con mayúscula, o para buscar palabras que contengan un sufijo en particular.

## Notas

[^nota1]: En caso de que tengas curiosidad de una expresión regular estándar (aunque simplificada) para validar correos electrónicos usada por los navegadores, es la siguiente: ```^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$```. Tomado de David J. Malan, [Harvard CS50's Introduction to Programming with Python](https://youtu.be/nLRL_NcnK-4?t=34943)

[^nota2]: En este caso, la función `match` regresa un objeto `None`, que no tiene ningún grupo. Por lo tanto, la función `group` no puede extraer ningún grupo. Por otra parte, el segundo grupo ```(?:\s+[A-Z][a-ü]+)``` no se captura porque se usa `(?:...)` como grupo no capturador.
