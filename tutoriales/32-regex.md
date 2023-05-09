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
# Expresiones regulares

Durante buena parte de este curso hemos recurrido a operaciones lógicas para "descubrir" coincidencias en los textos. Hemos recurrido a las funciones propias del método `str` de Python para normalizar palabras, hemos usado condicionales para identificar si una palabra es igual o está contenida en un conjunto de caracteres, hemos usado iteraciones para recorrer los conjuntos de palabras de un texto, incluso hemos recurrido a los métodos de `try` y `except` para saber si una palabra es un número o no.

Sin embargo, hay un método que nos permite hacer todo esto de manera más eficiente: las expresiones regulares. Las expresiones regulares son un lenguaje de programación en sí mismo, que nos permite identificar patrones en los textos. En este tutorial veremos cómo usarlas en Python.

## ¿Qué son las expresiones regulares?

En términos simples, las expresiones regulares consisten en patrones de caracteres que nos permiten identificar coincidencias en los textos, a partir de una serie de reglas. Téoricamente, las expresiones regulares están fundamentadas en la teoría de los autómatas, un tema propio de la teoría computacional. No es necesario que comprendamos la teoría computacional para usar expresiones regulares, pero sí es relevante tener en cuenta que lo que buscan las expresiones regulares no es una coincidencia exacta, sino un patrón de coincidencia.

## Uso de expresiones regulares

Vamos a retomar un ejemplo que utilizamos en la lección [Funciones y modularidad](23-funcionesLlamados.md). En esa lección, creamos una función llamada `extraer_fechas()` que nos permitía extraer las fechas de un texto. La función era la siguiente:

```{code-cell} ipython3
def separador(palabra, caracter):
    """Separa una palabra en una lista de palabras según un caracter.

    Parámetros
    ----------
    palabra: str
        Palabra a separar
    caracter: str
        Caracter por el cual se separará la palabra

    Retorna
    -------
    palabras: list
        Lista de palabras separadas
    """
    palabras = []
    for palabra in palabra.split(caracter):
        if palabra.isdigit() and len(palabra) == 4:
            palabras.append(palabra)
    return palabras

def extraer_fechas(texto):
    """Extrae todas las fechas que aparezcan en un texto.
    
    Parámetros
    ----------
    texto: str
        Texto del cual se extraerán las fechas

    Retorna
    -------
    fechas: list
        Lista de fechas extraídas del texto
    """
    fechas = []
    for palabra in texto.split():
        palabra = palabra = palabra.strip(",;:()[]{}")
        if palabra.endswith("."):
            palabra = palabra.replace(".", "")

        if palabra.isdigit() and len(palabra) == 4:
            fechas.append(palabra)
        elif len(palabra) > 5 and "-" in palabra:
            fechas.extend(separador(palabra, "-"))
        elif len(palabra) > 5 and "." in palabra:
            fechas.extend(separador(palabra, "."))

    return fechas
```

Y la utilizamos en un texto de ejemplo:

```{code-cell} ipython3
Cervantes = "Miguel de Cervantes Saavedra (Alcalá de Henares,4 29 de septiembre de 1547-Madrid, 22 de abril3 de 1616) fue un novelista, poeta, dramaturgo y soldado español."
extraer_fechas(Cervantes)
```

Como vemos, la función nos devuelve una lista con las fechas que encontró en el texto. Sin embargo, la función tiene un problema: sólo funciona con fechas que estén escritas en el formato `dd/mm/aaaa`. Si la fecha está escrita en otro formato, la función no la detecta. Por ejemplo, si la fecha está escrita en el formato `dd-mm-aaaa`, la función no la detecta:

```{code-cell} ipython3
Cervantes = "Miguel de Cervantes Saavedra (Alcalá de Henares,4 29-09-1547-Madrid, 22-04-1616) fue un novelista, poeta, dramaturgo y soldado español."
extraer_fechas(Cervantes)
```

Para solucionar este problema, podríamos modificar la función para que detecte fechas en el formato `dd-mm-aaaa`. Sin embargo, esto no solucionaría el problema, ya que podrían haber fechas escritas en otros formatos, como `dd.mm.aaaa` o `dd mm aaaa`. En este caso, la solución más eficiente sería usar expresiones regulares.

## Sintaxis de las expresiones regulares

Las expresiones regulares tienen una sintaxis propia, que nos permite identificar patrones en los textos. En este tutorial veremos los patrones más comunes, pero si quieren profundizar en el tema, pueden consultar la [documentación oficial de Python](https://docs.python.org/3/library/re.html).

### Coincidencias exactas

La coincidencia más simple que podemos buscar es una coincidencia exacta. Por ejemplo, si queremos buscar la palabra "novelista" en el texto de ejemplo, podemos usar la siguiente expresión regular:

```{code-cell} ipython3
import re

re.findall(r"novelista", Cervantes)
```

Como vemos, la expresión regular nos devuelve una lista con todas las coincidencias exactas que encontró en el texto. Si queremos buscar la palabra "novelista" o "poeta", podemos usar el operador `|`:

```{code-cell} ipython3
re.findall(r"novelista|poeta", Cervantes)
```

Incluso podemos evitar las mayúsculas y minúsculas aprovechando el parámetro `flags` de la librearía `re`:

```{code-cell} ipython3
re.findall(r"miguel|madrid", Cervantes, flags=re.IGNORECASE)
```

Hasta ahora nada sorprendente, ya que podríamos haber usado el método `str` de Python para buscar coincidencias exactas. Sin embargo, las expresiones regulares nos permiten buscar patrones más complejos gracias a los metacaracteres, las clases y los cuantificadores.

### Metacaracteres, clases de caracteres y cuantificadores

Las expresiones regulares nos permiten buscar patrones más complejos, usando metacaracteres, clases de caracteres y cuantificadores.

#### Metacaracteres

Una lista de metacaracteres más comunes es la siguiente:

| Metacaracter | Descripción |
|--------------|-------------|
| `.` | Cualquier carácter, excepto nueva línea |
| `^` | Inicio de la cadena |
| `$` | Fin de la cadena |
| `*` | Cero o más ocurrencias |
| `+` | Una o más ocurrencias |
| `?` | Cero o una ocurrencia |
| `{}` | Exactamente el número de ocurrencias especificado |
| `[]` | Un conjunto de caracteres |
| `()` | Captura y agrupa |
| `\` | Carácter de escape |
| `\|` | Operador OR |

Usemos un ejemplo para mostrar un poco el funcionamiento de algunos de estos metacaracteres. Por ejemplo, si queremos buscar todas las palabras que empiezan con "nov", podemos usar el metacaracter `^`:

```{code-cell} ipython3
Cervantes = "Miguel de Cervantes Saavedra (Alcalá de Henares,4 29 de septiembre de 1547-Madrid, 22 de abril3 de 1616) fue un novelista, poeta, dramaturgo y soldado español."
nov = [p for p in Cervantes.split(" ") if re.match(r"^nov", p, re.IGNORECASE)]
print(nov)
```

Como vemos, la expresión regular nos devuelve una lista con todas las palabras que empiezan con "nov". Si queremos buscar todas las palabras que terminan con "el", podemos usar el metacaracter `$`:

```{code-cell} ipython3
el = [p for p in Cervantes.split(" ") if re.match(r"el$", p, re.IGNORECASE)]
print(el)
```

Ahora, supongamos que queremos buscar solamente las palabras que estén entre paréntesis. Para esto, podemos usar el metacaracter `(`:

```{code-cell} ipython3
re.findall(r"\(.*\)", Cervantes, re.UNICODE)
```

Nota que la sintaxis en este caso es un poco más compleja, pero ya no requerimos recurrir a una iteración para encontrar los patrones.. Vamos a explicarla en detalle:

- `\(`: el paréntesis izquierdo tiene un significado especial en las expresiones regulares, por lo que debemos usar el metacaracter `\` para indicar que queremos buscar un paréntesis izquierdo.
- `.*`: el punto en esta fórmula significa que buscamos cualquier carácter, excepto nueva línea. El asterisco significa que queremos buscar cero o más ocurrencias de cualquier carácter.
- `\)`: la expresión regular busca todos los caracteres a la derecha del paréntesis izquierdo, hasta que encuentra un paréntesis derecho.

Iremos utilizando otros metacaracteres en tanto avancemos en nuestras búsquedas. Por ahora, veamos las clases de caracteres.

#### Clases de caracteres

Las clases de caracteres son un conjunto predefinido de caracteres que encontramos en un texto. En la siguiente tabla mostramos las clases de caracteres predefinidas más comunes:

| Clase de caracteres | Descripción |
|---------------------|-------------|
| `\d` | Cualquier dígito |
| `\D` | Cualquier carácter que no sea un dígito |
| `\s` | Cualquier espacio en blanco |
| `\S` | Cualquier carácter que no sea un espacio en blanco |
| `\w` | Cualquier carácter alfanumérico |
| `\W` | Cualquier carácter que no sea alfanumérico |

Hagamos otro reto, utilizando una clase de caracteres, creemos una búsqueda que regrese la primera palabra a la izquierda y la primera a la derecha después de la conjunción "de":

```{code-cell} ipython3
re.findall(r"(\w+) de (\w+)", Cervantes)
```

Deconstruyamos esta fórmula para entender cómo funciona:

- `(\w+)`: la expresión regular busca una o más ocurrencias de cualquier carácter alfanumérico. Está utilizando el metacaracter `()` para agrupar el resultado. La clase de caracteres `\w` es equivalente a `[a-zA-Z0-9_]`, que quiere decir que busca cualquier carácter alfanumérico, incluyendo letras mayúsculas y minúsculas, números y el guión bajo. El signo `+` significa que queremos buscar una o más ocurrencias de cualquier carácter alfanumérico.
- `de`: la expresión regular busca la palabra "de" en el texto.
- `(\w+)`: la expresión regular busca una o más ocurrencias de cualquier carácter alfanumérico. Está utilizando el metacaracter `()` para agrupar el resultado. En este caso, a la derecha de la palabra "de".

Subamos la apuesta. Ahora busquemos las tres palabras a la izquierda y tres a la derecha de la palabra "de". Para que el ejercicio tenga sentido, aumentemos el tamaño del texto a analizar:

```{code-cell} ipython3
Cervantes += """Es ampliamente considerado una de las máximas figuras de la literatura española. Fue el autor de El ingenioso hidalgo don Quijote de la Mancha, novela conocida habitualmente como El Quijote, que lo llevó a ser mundialmente conocido y a la cual muchos críticos han descrito como la primera novela moderna, así como una de las mejores obras de la literatura universal, cuya cantidad de ediciones y traducciones solo es superada por la Biblia.5 A Cervantes se le ha dado el apelativo de «Príncipe de los Ingenios».6

Desde el siglo xviii está admitido que el lugar de nacimiento de Miguel de Cervantes fue Alcalá de Henares,4 dado que allí fue bautizado, según su acta bautismal, y que de allí aclaró ser natural en la llamada Información de Argel (1580).7 El día exacto de su nacimiento es menos seguro, aunque lo normal es que naciera el 29 de septiembre, fecha en que se celebra la fiesta del arcángel San Miguel, dada la tradición de recibir el nombre del santoral del día del nacimiento. Miguel de Cervantes fue bautizado el 9 de octubre de 1547 en la parroquia de Santa María la Mayor.89 El acta del bautizo reza:

Domingo, nueve días del mes de octubre, año del Señor de mill e quinientos e quarenta e siete años, fue baptizado Miguel, hijo de Rodrigo Cervantes e su mujer doña Leonor. Baptizóle el reverendo señor Bartolomé Serrano, cura de Nuestra Señora. Testigos, Baltasar Vázquez, Sacristán, e yo, que le bapticé e firme de mi nombre. Bachiller Serrano.10
El padre del escritor era Rodrigo de Cervantes (1509-1585), casado con Leonor de Cortinas, de la cual apenas se sabe nada, excepto que era natural de Arganda del Rey.11 Los hermanos de Cervantes fueron Andrés (1543), Andrea (1544), Luisa (1546), que llegó a ser priora de un convento carmelita; Rodrigo (1550), también soldado, que le acompañó en el cautiverio argelino; Magdalena (1554) y Juan, solo conocido porque su padre lo menciona en el testamento."""
```

Ahora, apliquemos la siguiente expresión regular:

```{code-cell} ipython3
re.findall(r"(\w+) (\w+) (\w+) de (\w+) (\w+) (\w+)", Cervantes)
```

En este caso, repetimos tres veces el grupo de caracteres `\w+`. Una solución lógica para simplificar la expresión podría ser el uso de un cuantificador, por ejemplo:

```{code-cell} ipython3
re.findall(r"(\w+ ){3}de (\w+ ){3}", Cervantes, re.MULTILINE)
```

Pero como verás, en este caso no se obtiene el listado de las palabras, lo cual no es lo que queremos. Por lo tanto, la expresión regular que utilizamos al principio es la más adecuada.

Ahora, con los metacaracteres y las clases de caracteres, podemos construir una expresión que nos permita extraer los años de este conjunto de textos:

```{code-cell} ipython3
re.findall(r"\d{4}", Cervantes)
```

¡Y eso es todo! Mientras con la función `extraer_fechas()` tuvimos que explorar una serie de opciones lógicas para extraer los años, con las expresiones regulares pudimos extraer los años en una sola línea de código.

#### Clases de caracteres personalizadas

Los corchetes nos permiten crear clases personalizadas, de tal manera que sea más precisa nuestra búsqueda. Por ejemplo, si queremos buscar todas las palabras que empiecen con una letra mayúscula, podemos utilizar la siguiente expresión regular:

```{code-cell} ipython3
re.findall(r"[A-Z]\w+", Cervantes)
```

También podemos modificar la expresión para que evite encontrar conectores como "El", "Es", "Se", etc.:

```{code-cell} ipython3
re.findall(r"\b(?!El\b|Es\b|Se\b)([A-Z][a-z]+)\b", Cervantes)
```

Con esta expresión empezamos a ver cómo las expresiones regulares pueden volverse ilegibles bastante rápido. Vamos a explicar esta expresión regular:

Esta expresión está compuesta de dos conjuntos: uno buscar patrones que no queremos y el segundo busca patrones que sí queremos.

- `\b(?!El\b|Es\b|Se\b)`: el primer conjunto busca patrones que no queremos. En este caso, buscamos patrones que empiecen con "El", "Es" o "Se". El metacaracter `\b` busca límites de palabras, es decir, que la palabra empiece o termine con el patrón que estamos buscando. El metacaracter `|` funciona como un operador lógico OR, es decir, que si encuentra "El", "Es" o "Se", la expresión regular se detiene. El metacaracter `?!` es un operador lógico NOT, es decir, que si encuentra "El", "Es" o "Se", la expresión regular se detiene.
- `([A-Z][a-z]+)`: el segundo conjunto busca patrones que sí queremos. En este caso, buscamos patrones que empiecen con una letra mayúscula y que tengan una o más letras minúsculas. El metacaracter `+` significa que queremos buscar una o más ocurrencias de cualquier carácter alfanumérico.

Es fáci identificar que en este caso, si queremos ampliar nuestra lista de expresiones negativas, la fórmula va a adquirir un tamaño casi absurdo, por ejemplo:

```{code-cell} ipython3
patron = r'\b(?!Es\b|Se\b|De\b|El\b|La\b|Los\b|Las\b|Un\b|Una\b|Unos\b|Unas\b|Al\b|Del\b|Y\b|O\b|En\b|A\b|Ante\b|Bajo\b|Cabe\b|Con\b|Contra\b|De\b|Desde\b|Durante\b|En\b|Entre\b|Hacia\b|Hasta\b|Mediante\b|Para\b|Por\b|Según\b|Sin\b|Sobre\b|Tras\b|Versus\b|Vía\b)([A-Z][a-z]+)\b'

resultado = re.findall(patron, Cervantes)

print(resultado)
```

En este caso, podemos aprovechar los métodos de Python para incluir todos los conectores en una lista y luego usar el método `join()` para unirlos con el operador lógico OR:

```{code-cell} ipython3

conectores = ["Es", "Se", "De", "El", "La", "Los", "Las", "Un", "Una", "Unos", "Unas", "Al", "Del", "Y", "O", "En", "A", "Ante", "Bajo", "Cabe", "Con", "Contra", "De", "Desde", "Durante", "En", "Entre", "Hacia", "Hasta", "Mediante", "Para", "Por", "Según", "Sin", "Sobre", "Tras", "Versus", "Vía"]

patron = r'\b(?!' + '|'.join(conectores) + r'\b)([A-Z][a-z]+)\b'

resultado = re.findall(patron, Cervantes)

print(resultado)
```

De esta manera el código es mucho más legible y fácil de modificar.

## Ejercicios

### Ejercicio 1

Construye una expresión regular que pueda identificar un patrón en el que el nombre y el apellido de una persona estén separados por una coma (por ejemplo, "Cervantes, Miguel"). La expresión debe ser capaz de identificar el nombre y el apellido de la persona.

### Ejercicio 2

Construye una expresión regular que permita extraer la fecha completa que tenga el formato dd de mes de aaaa (por ejemplo, "12 de octubre de 1492"). La expresión debe ser capaz de identificar el día, el mes y el año.

### Ejercicio 3

Construye una función que permita obtener el contexto de una palabra clave (n palabras a la izquierda y n a la derecha) en un texto. La función debe recibir como parámetros el texto, la palabra clave y el número de palabras a la izquierda y a la derecha que se quieren extraer. La función debe retornar el contexto de la palabra clave.
