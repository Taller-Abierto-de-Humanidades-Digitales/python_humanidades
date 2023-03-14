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

# Funciones y modularidad

La modularidad es una técnica de diseño de software que consiste en dividir un programa en partes más pequeñas, llamadas módulos. Cada módulo tiene una responsabilidad específica y se encarga de realizar una tarea concreta. Los módulos se comunican entre sí mediante llamadas a funciones. De esta forma, el programa se divide en partes más pequeñas y más fáciles de entender y modificar.

En la programación funcional se aplica el principio de modularidad para indicar que cada función realiza una tarea concreta e independiente de las demás.

Por ejemplo, en nuestra función `saludar()` podemos dividirla en dos partes: una que se encarga de solicitar el año de nacimiento para calcular la edad y otra que se encarga de saludar al usuario:

```{code-cell} ipython3
def edad(anio):
    return 2023 - int(anio)

def saludar(nombre, fecha_nacimiento=1990, lugar_de_nacimiento="Colombia"):
    return f"Hola {nombre}, tienes {edad(fecha_nacimiento)} años y naciste en {lugar_de_nacimiento}"
```

En este sentido, podemos llamar a la función `saludar()` sin necesidad de llamar a la función `edad()`:

```{code-cell} ipython3
saludar("Juan", 1980, "Colombia")
```

Pero también podemos llamar a la función `edad()` sin necesidad de llamar a la función `saludar()`:

```{code-cell} ipython3
edad(1980)
```

```{admonition} Programación funcional
:class: tip
En la programación funcional, cada función realiza una tarea concreta e independiente de las demás. Por lo tanto, las funciones no deben depender de otras funciones para funcionar. En este ejemplo, la función `edad()` no depende de la función `saludar()` para funcionar. La función `saludar()` usar la función `edad()` para calcular la edad del usuario, lo que es un ejemplo de **composición de funciones**, un aspecto clave de la programación funcional.
```

Podemos hacer algo similar con nuestra función `extraer_fechas()` para hacerla un poco más sintética:

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

El efecto en nuestro programa es el mismo:

```{code-cell} ipython3
Cervantes = "Miguel de Cervantes Saavedra (Alcalá de Henares,4​ 29 de septiembre de 1547-Madrid, 22 de abril3​ de 1616) fue un novelista, poeta, dramaturgo y soldado español."
Quevedo = "Francisco Gómez de Quevedo Villegas y Santibáñez Cevallos (Madrid, 14 de septiembre de 1580-Villanueva de los Infantes, Ciudad Real, 8 de septiembre de 1645) fue un noble, político y escritor español del Siglo de Oro."
Calderon = "Pedro Calderón de la Barca (Madrid, 17 de enero de 1600-25 de mayo de 1681) fue un escritor español, sacerdote católico, miembro de la Venerable Congregación de Presbíteros Seculares Naturales de Madrid San Pedro Apóstol y caballero de la Orden de Santiago, conocido fundamentalmente por ser uno de los más insignes literatos barrocos del Siglo de Oro, en especial por su teatro."

bios = [Cervantes, Quevedo, Calderon]

fechas = []
for b in bios:
    fechas.append(extraer_fechas(b))

print(fechas)
```

Aun mejor, podemos utilizar la función `separador()` en cualquier otro momento:

```{code-cell} ipython3
texto = "1580-Villanueva"
print(separador(texto, "-"))
```

Habrás notado que esto es un asunto de diseño más que de funcionalidad. La modularidad hace que el código sea más fácil de leer y mantener, por ello es sumamente recomendable utilizar este tipo de técnicas de diseño.
