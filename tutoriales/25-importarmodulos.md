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

# Funciones: Modularidad

Hasta el momento, nuestros programas han consistido en varios bloques de código que se ejecutan secuencialmente. Seguramente habrás notado que cada vez que quieres probar una función tienes que ejecutar todo el programa, incluso aquellos bloques de código que no quieres usar en ese momento.

A mayor complejidad del código, más difícil es leer y entender el programa. Además, si sumamos conjuntos de datos, diccionarios, listados y otros tipos de datos, la extensión del script aumenta hasta acumular miles de líneas de código. Al igual que en un sitio Web, la lectura se hace más difícil entre más "largo" es el texto.

La modularidad es una técnica de diseño de software ampliamente utilizada en la industria, que permite dividir un programa en partes más pequeñas, llamadas módulos. Cada módulo contiene una parte del programa, incluso puede ser un programa en sí mismo, que se puede importar y usar en otros programas o en un programa complejo.

Todos los lenguajes de programación modernos tienen mecanismos para modularizar el código, y Python no es la excepción.

En este segmento del curso, aprenderás a importar módulos desde la biblioteca estándar de Python, a crear tus propios módulos y a importar funciones específicas de un módulo.

## Importar módulos

La biblioteca estándar de Python es una colección de módulos que se instalan junto con el lenguaje. Estos módulos proporcionan una amplia variedad de funciones que pueden ser utilizadas en tus programas. Para ver una lista completa de los módulos de la biblioteca estándar, puedes consultar la [documentación oficial de Python](https://docs.python.org/es/3/library/index.html).

Para los fines de nuestro curso, vamos a utilizar el módulo `datetime` para trabajar con fechas y horas. Para importar un módulo, utilizamos la palabra reservada `import` seguida del nombre del módulo. Por ejemplo, para importar el módulo `datetime`, escribimos:

```{code-cell} ipython3
import datetime
```

Una vez importado el módulo, podemos utilizar sus funciones. Por ejemplo, para obtener la fecha y hora actuales, escribimos:

```{code-cell} ipython3
datetime.datetime.now()
```

Este valor devuelve la fecha y hora en la que fue construido este libro. Si ejecutas este código en tu computadora, obtendrás la fecha y hora actuales.

Con este módulo también podemos calcular la diferencia entre dos fechas. Por ejemplo, para calcular la diferencia entre la fecha de hoy y el fin del año, escribimos:

```{code-cell} ipython3
fin_de_ano = datetime.datetime(2023, 12, 31)
diferencia = fin_de_ano - datetime.datetime.now()
print(diferencia)
```

Cuando importamos la librería `datetime` con la instrucción `import datetime`, estamos importando todo el módulo. Esto significa que podemos acceder a todas las funciones del módulo utilizando el prefijo `datetime.`. Es decir, cuando escribimos `datetime.datetime.now()`, estamos accediendo a la función `now()` de la clase `datetime` que pertenece al módulo `datetime`.[^nota1]

### Importar funciones específicas

Otra manera de importar un módulo es importando funciones específicas. Por ejemplo, para importar la función `datetime()` del módulo `datetime`, escribimos:

```{code-cell} ipython3
from datetime import datetime
```

Una vez importada la función, podemos utilizarla directamente. Por ejemplo, para obtener la fecha y hora actuales, escribimos:

```{code-cell} ipython3
datetime.now()
```

En general es buena práctica importar funciones específicas de un módulo, ya que evita que se sobreescriban nombres de funciones que ya existen en el programa.[^nota2]

### Importar módulos con alias

Una práctica muy común es importar módulos con alias. Por ejemplo, para importar el módulo `datetime` con el alias `dt`, escribimos:

```{code-cell} ipython3
import datetime as dt
```

Una vez importado el módulo, podemos utilizar sus funciones utilizando el alias. Por ejemplo, para obtener la fecha y hora actuales, escribimos:

```{code-cell} ipython3
dt.datetime.now()
```

En la librería estándar no es muy común utilizar alias para importar los módulos, pero es una costumbre con librerías populares como `matplotlib`, `numpy` y `pandas`.

## Notas
  
[^nota1]: En los siguientes segmentos del curso abordaremos las clases y los objetos en Python.

[^nota2]: Una manera permitida pero no recomendada de realizar importaciones es a través de la instrucción `from datetime import *`. Esta instrucción importa todas las funciones del módulo `datetime`, pero no es recomendable utilizarla ya que puede sobreescribir nombres de funciones que ya existen en el programa. Por otra parte, es difícil reconocer qué se ha importado y qué no; lo que impacta en la legibilidad del código. Por esta razón, es mejor importar funciones específicas de un módulo.
