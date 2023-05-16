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

# Clases

Si podemos hacer la analogía de una función como una acción, podemos entender igualmente una clase como una entidad. En nuestros programas previos, elaboramos bibliografías a partir de datos que teníamos en diccionarios. Las funciones realizaban acciones, operaciones de búsqueda, segmentación, etc. La pregunta en este caso sería ¿qué entidad o entidades constituyen una bibliografía?

Un catálogo bibliográfico no es otra cosa sino la representación de objetos bibliográficos: libros, revistas, manuscritos, videos, entre otros. En este sentido, podemos asimilar esto en un lenguaje de programación, donde creamos un objeto digital correspondiente a un libro, revista, etc. y que tenga las propiedades y métodos que necesitemos para trabajar con él.

Iniciemos nuestro ejercicio creando la clase Libro. En este caso, la clase Libro tendrá como propiedades el título, el autor, el año de publicación y el lugar de publicación. Además, tendrá como métodos el mostrar la información del libro y el mostrar el autor.

```{code-cell} ipython3
class Libro:
    def __init__(self, titulo, autor, anio, lugar):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.lugar = lugar

    def mostrar_info(self):
        print(f"El libro {self.titulo} fue escrito por {self.autor} en {self.lugar} en el año {self.anio}.")

    def mostrar_autor(self):
        print(f"El autor del libro {self.titulo} es {self.autor}.")
```

Habrás notado rápidamente la sintaxis de una clase: para crear este objeto, necesitamos hacer uso de la palabra reservada `class` seguido por el nombre arbitrario de la clase. Por convención, la clase se escribe en estilo "Camel Case", es decir, la primera letra de cada palabra es mayúscula. En el cuerpo de la clase, se definen las propiedades y métodos de la clase. En este caso, las propiedades son las variables que definen el objeto y los métodos son las acciones que puede realizar el objeto.

## El método `__init__`

Habrás notado que las propiedades del objeto se asignan en el método `__init__`. Este es un método especial de Python que se crea automáticamente cada vez que se instancia una clase.

```{admonition} Sintaxis
:class: tip
Ten cuidado con la sintaxis del método `__init__`. Debes utilizar **dos guiones bajos** antes y después de la palabra `init`. Si no lo haces, Python no reconocerá el método como tal y no funcionará correctamente.
```

Notarás también que el método `__init__()` recibe cinco parámetros: `self`, `titulo`, `autor`, `anio` y `lugar`. El primer parámetro, `self`, es una referencia al objeto actual, y se utiliza para acceder a las variables que pertenecen a la clase. Los otros cuatro parámetros son los que se utilizan para crear el objeto. En este caso, los parámetros `titulo`, `autor`, `anio` y `lugar` son los que se asignan a las propiedades del objeto.

## El parámetro `self`

En Python, la palabra clave self se utiliza como el primer parámetro en la definición de los métodos de una clase. Este parámetro hace referencia a la instancia actual de la clase y se utiliza para acceder a los atributos y métodos de esa instancia. En este caso, el parámetro `self` se utiliza para acceder a las propiedades del objeto.

Cada vez que se crea una instancia de la clase, Python crea un objeto y lo asigna a la variable `self`. Por lo tanto, podemos acceder a las propiedades del objeto utilizando la variable `self`.

```{code-cell} ipython3
libro1 = Libro("El Quijote", "Miguel de Cervantes", 1605, "Madrid")
print(libro1.mostrar_info())
```

Para que un parámetro se convierta en una propiedad del objeto es necesario utilizar la palabra clave `self`. Si hiciésemos lo contrario y no utilizásemos la palabra clave `self`, el parámetro no se convertiría en una propiedad del objeto.

```{code-cell} ipython3
class Libro:
    def __init__(titulo, autor, anio, lugar):
        titulo = titulo
        autor = autor
        anio = anio
        lugar = lugar

    def mostrar_info():
        print(f"El libro {titulo} fue escrito por {autor} en {lugar} en el año {anio}.")

    def mostrar_autor():
        print(f"El autor del libro {titulo} es {autor}.")

libro1 = Libro("El Quijote", "Miguel de Cervantes", 1605, "Madrid")
print(libro1.mostrar_info())
```

Verás que nos muestra un `TypeError` en el que se esperaba recibir 4 parámetros posicionales y se pasaron 5. ¿A qué se debe esto? El problema en el código es que el método `__init__` de la clase Libro no está recibiendo el primer argumento self. El primer argumento de cualquier método de una clase en Python siempre debe ser self, que hace referencia a la instancia de la clase en sí misma. Por lo tanto, cuando llamamos a un método de una clase, Python automáticamente pasa la instancia de la clase como el primer argumento. Por lo tanto, si no incluimos el parámetro self en el método `__init__`, Python no sabrá qué hacer con él.

## Hacer una instancia de una clase

Para crear una instancia de una clase, debemos llamar a la clase como si fuera una función. En este caso, la clase Libro se llama como si fuera una función y se le pasan los parámetros necesarios para crear el objeto.

```{code-cell} ipython3
:tags: [remove-cell]
class Libro:
    def __init__(self, titulo, autor, anio, lugar):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.lugar = lugar

    def mostrar_info(self):
        print(f"El libro {self.titulo} fue escrito por {self.autor} en {self.lugar} en el año {self.anio}.")

    def mostrar_autor(self):
        print(f"El autor del libro {self.titulo} es {self.autor}.")
```

```{code-cell} ipython3
libro1 = Libro("El Quijote", "Miguel de Cervantes", 1605, "Madrid")
```

## Acceder a las propiedades o atributos de una instancia

Una vez que hemos creado una instancia de la clase, podemos acceder a los atributos de la instancia utilizando la notación de punto.

```{code-cell} ipython3
print(libro1.titulo)
print(libro1.autor)
print(libro1.anio)
print(libro1.lugar)
```

## Llamar métodos

Para llamar a un método de una clase, utilizamos igualmente la notación de punto. En este caso, llamamos al método `mostrar_info` de la clase Libro.

```{code-cell} ipython3
libro1.mostrar_info()
```

También podemos, de la misma manera, llamar al método `mostrar_autor`.

```{code-cell} ipython3
libro1.mostrar_autor()
```

Básicamente, estamos pasando una función que toma los argumentos de la instancia como argumentos de la función.

## Crear múltiples instancias

Podemos crear múltiples instancias de una clase. En este caso, creamos dos instancias de la clase Libro.

```{code-cell} ipython3
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, "Francia")
libro3 = Libro("El Hobbit", "J. R. R. Tolkien", 1937, "Inglaterra")
```

De esta manera podemos acceder a los atributos de cada uno de los objetos creados.

```{code-cell} ipython3
print("Mostrar la información del libro 1")
libro1.mostrar_info()
libro1.mostrar_autor()
print("")

print("Mostrar la información del libro 2")
libro2.mostrar_info()
libro2.mostrar_autor()
print("")

print("Mostrar la información del libro 3")
libro3.mostrar_info()
libro3.mostrar_autor()
print("")
```

Un aspecto importante a tener en cuenta es que incluso si tenemos la misma información es posible crear dos instancias diferentes de la misma clase.

```{code-cell} ipython3
libro4 = Libro("El Quijote", "Miguel de Cervantes", 1605, "Madrid")
libro5 = Libro("El Quijote", "Miguel de Cervantes", 1605, "Madrid")
```

Para Python, `libro4` y `libro5` son dos objetos diferentes, aunque tengan la misma información.

```{code-cell} ipython3
print(libro4.mostrar_info())
print(libro5.mostrar_info())
```

Dependiendo de la situación, esto puede ser una ventaja o una desventaja. Lo que es fundamental es que tengamos en cuenta que esta es una característica del lenguaje de programación Python y que debemos tenerla en cuenta a la hora de crear nuestros programas.

## Actividad autónoma

1. Crea una clase llamada `Colección` que tenga como atributos el `nombre` y la `fecha de creación`. Crea un método llamado `mostrar_info` que muestre por pantalla la información de la colección. Crea una instancia de la clase `Colección` y muestra la información de la colección.
2. Crea una clase llamada `Usuario` que tenga como atributos el `nombre`, el `apellido`, la `fecha de nacimiento` y el `correo electrónico`. Crea un método llamado `saludo` que muestre por pantalla un saludo personalizado al usuario. Crea una instancia de la clase `Usuario` y muestra un saludo personalizado al usuario.
