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

# Retornar valores en una función

En los ejemplos anteriores cada función que creamos imprime un mensaje en la pantalla. Esto puede ser útil en algunos casos, pero en general lo que deseamos es que una función devuelva un valor que podamos utilizar en nuestro programa. Modifiquemos nuestra función  `saludar()` para que en lugar de imprimir un mensaje en la pantalla, devuelva el mensaje como un valor de cadena:

```{code-cell} ipython3
def saludar(nombre):
    mensaje = f"Hola {nombre}, ¿cómo estás?"
    return mensaje
```

Ahora podemos llamar a la función `saludar()` y guardar el valor de retorno en una variable:

```{code-cell} ipython3
saludo = saludar("Juan")
print(saludo)
```

Aunque "técnicamente" nuestro programa cumple la misma función, una ventaja es que podemos reutilizar el valor del saludo en cualquier parte del programa:

```{code-cell} ipython3
saludo = saludo.upper()
print(saludo)
```

El anterior es un ejemplo sumamente simple, pero describe de manera sucinta lo que puede lograr una función. Ahora realicemos una acción un poco más compleja.

## Retornar múltiples valores (tuples)

En el ejemplo anterior, la función `saludar()` devolvió un único valor. Sin embargo, es posible que una función devuelva múltiples valores. Por ejemplo, podemos modificar la función `saludar()` para que devuelva el saludo y la longitud del saludo:

```{code-cell} ipython3
def saludar(nombre):
    mensaje = f"Hola {nombre}, ¿cómo estás?"
    return mensaje, len(mensaje)
```

Ahora podemos llamar a la función `saludar()` y guardar los valores de retorno en dos variables:

```{code-cell} ipython3
saludo, longitud = saludar("Juan")
print(saludo)
print(longitud)
```

```{admonition} Observación
:class: tip

En este caso, la función devuelve un tipo de dato denominado `tuple` (tupla). Una tupla es una estructura de datos que permite almacenar múltiples valores, de manera similar a un lista, pero con unas características ligeramente diferentes:

- La tupla es ordenada: los valores se almacenan en un orden específico.
- La tupla es inmutable: una vez creada, no es posible modificar sus valores.
- La tupla permite duplicados: es posible almacenar valores duplicados en una tupla.

Veremos un poco más sobre las tuplas en el siguiente tutorial.
```

De la misma manera podemos lograr que la función regrese múltiples valores de cualquier tipo de dato:

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

    Retorna
    -------
    edad: int
        Edad de la persona
    nombre: str
        Nombre de la persona
    lugar_de_nacimiento: str
        Lugar de nacimiento de la persona
    """
    try:
        edad = 2023 - int(fecha_nacimiento)
        return edad, nombre, lugar_de_nacimiento # observa que el orden de los valores es diferente al de los parámetros
    except:
        raise ValueError(f"La fecha de nacimiento ingresada ({fecha_nacimiento}) no es un número.")
        raise

edad, nombre, lugar_de_nacimiento = saludar("Juan", 1990, "Colombia")
print(f"{nombre} nació en {lugar_de_nacimiento} y tiene {edad} años.")
```

Teniendo en cuenta que esta función regresa un valor de edad a partir de una fecha de nacimiento, podríamos utilizarla en un programa que calcule la edad promedio de un grupo de estudiantes a partir de sus fechas de nacimiento:

```{code-cell} ipython3
grupo = [
    ("Juan", 1990, "Colombia"),
    ("María", 1992, "Colombia"),
    ("Pedro", 1994, "Colombia"),
    ("Ana", 1996, "Colombia"),
    ("Luis", 1998, "Colombia"),
    ("Sofía", 2000, "Colombia"),
    ("Carlos", 2002, "Colombia"),
    ("Camila", 2004, "Colombia"),
    ("Jorge", 2006, "Colombia"),
    ("Laura", 2008, "Colombia"),
]

edades = []
for estudiante in grupo:
    edad, nombre, lugar_de_nacimiento = saludar(*estudiante) # este es un ejemplo de desempaquetamiento de tuplas
    edades.append(edad)

edad_promedio = sum(edades) / len(edades)
print(f"La edad promedio del grupo es {edad_promedio:.2f} años.")
```

Esto significa que también podríamos aplicar esta función a una lista de comprensión:

```{code-cell} ipython3
edades = [saludar(*estudiante)[0] for estudiante in grupo]
edad_promedio = sum(edades) / len(edades)
print(f"La edad promedio del grupo es {edad_promedio:.2f} años.")
```

## Retornar listas

En los ejemplos anteriores retornamos una tupla, una estructura de datos inmutable y ordenada. No obstate, es posible retornar una lista. Vamos a cambiar de función. En este caso, vamos a crear una que nos permita retornar todas los años que se encuentren en un texto:

```{code-cell} ipython3
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
            for palabra in palabra.split("-"):
                if palabra.isdigit() and len(palabra) == 4:
                    fechas.append(palabra)
        elif len(palabra) > 5 and "." in palabra:
            for palabra in palabra.split("."):
                if palabra.isdigit() and len(palabra) == 4:
                    fechas.append(palabra)

    return fechas
```

Esta función nos permitirá encontrar los valores numéricos en un texto y todos aquellos que tengan cuatro dígitos serán considerados una fecha. Además, consideramos dos casos particulares, los rangos de fecha separados por un guión y los valores de fecha que puedan estar unidos a un llamado a nota al pie (p. ej, “1894.45”).

```{note}
La lógica de esta función viene determinada por el tipo de información que le estamos pasando al programa. En este caso, sabemos que las fechas se escriben completas (AAAA) y que no contamos con valores decimales que nos puedan confundir (p. ej, en “1894.45” el primer valor - 1894 - es una fecha y el segundo valor - 45 - es un llamado a una nota al pie). Es por tanto una función hecha a propósito para este caso particular.

Asimismo, esta función utiliza una estrategia lógica para encontrar coincidencias. Sin embargo, será más eficiente cuando utilicemos expresiones regulares, como veremos al final del curso.
```

Vamos a realizar nuestro ejercicio con algunos textos tomados de unas biografías en Wikipedia:

```{code-cell} ipython3
# Tomamos el primer párrafo de la biografía en español de Wikipedia

Cervantes = "Miguel de Cervantes Saavedra (Alcalá de Henares,4​ 29 de septiembre de 1547-Madrid, 22 de abril3​ de 1616) fue un novelista, poeta, dramaturgo y soldado español."
Quevedo = "Francisco Gómez de Quevedo Villegas y Santibáñez Cevallos (Madrid, 14 de septiembre de 1580-Villanueva de los Infantes, Ciudad Real, 8 de septiembre de 1645) fue un noble, político y escritor español del Siglo de Oro."
Calderon = "Pedro Calderón de la Barca (Madrid, 17 de enero de 1600-25 de mayo de 1681) fue un escritor español, sacerdote católico, miembro de la Venerable Congregación de Presbíteros Seculares Naturales de Madrid San Pedro Apóstol y caballero de la Orden de Santiago, conocido fundamentalmente por ser uno de los más insignes literatos barrocos del Siglo de Oro, en especial por su teatro."

bios = [Cervantes, Quevedo, Calderon]

fechas = []
for b in bios:
    fechas.append(extraer_fechas(b))
```

En cada caso recuperamos una lista de fechas. En caso de que no existieran elementos se devolvería una lista vacía. Incluso, por la forma de nuestros datos, podríamos determinar la edad de la persona en el momento de su muerte:

```{code-cell} ipython3
for f in fechas:
    if len(f) == 2:
        print(f"La edad de la persona en el momento de su muerte fue de {int(f[1]) - int(f[0])} años.")
    else:
        print("No se encontró la fecha de muerte.")
```

Nuevamente, estamos tratando aquí de un ejemplo muy puntual que funcionará solamente en unos cuantos casos, pero nos es útil para ilustrar el uso de las funciones y su retorno.

## Retornar diccionarios

En el ejemplo anterior, retornamos una lista de fechas. Sin embargo, es posible retornar un diccionario. Vamos a crear una función que nos permita extraer las palabras de un texto y contar cuántas veces aparecen:

```{code-cell} ipython3
def contar_palabras(texto):
    """Cuenta las palabras que aparecen en un texto.
    
    Parámetros
    ----------
    texto: str
        Texto del cual se extraerán las palabras

    Retorna
    -------
    palabras: dict
        Diccionario con las palabras y su frecuencia
    """
    palabras = {}
    for palabra in texto.split():
        palabra = palabra.strip(",;:()[]{}")
        if palabra.endswith("."):
            palabra = palabra.replace(".", "")

        if palabra in palabras:
            palabras[palabra] += 1
        else:
            palabras[palabra] = 1

    return palabras
```

```{note}
Esta función también utiliza una estrategia lógica para encontrar coincidencias, no obstante, una manera más sofisticada de hacerlo sería utilizando una librería como `nltk` para tokenizar el texto y luego contar las palabras. Veremos un poco de esta librería en sesiones posteriores.
```

Vamos a realizar nuestro ejercicio con algunos textos tomados de unas biografías en Wikipedia:

```{code-cell} ipython3

for b in bios:
    palabras = contar_palabras(b)
    print(f"\nBiografía de {' '.join(b.split()[0:4])}\n".upper())
    # imprime solamente las palabras que aparecen más de una vez
    for palabra, frecuencia in palabras.items(): # iteramos sobre el diccionario
        if frecuencia > 1:
            print(palabra, frecuencia)
```

Vemos entonces que dependiendo del tipo de dato que retornemos, podremos utilizar la función de distintas maneras. Por ejemplo, si retornamos una lista, podemos iterar sobre ella y utilizarla para realizar otras operaciones. Si retornamos un diccionario, podemos iterar sobre él y utilizarlo para realizar otras operaciones.

En el siguiente apartado veremos cómo llamar a una función desde otra función.
