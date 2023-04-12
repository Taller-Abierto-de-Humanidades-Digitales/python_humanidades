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

# Introducción a la programación orientada a objetos

En términos técnicos, todo en Python es un objeto {cite}`vanderplas_whirlwind_2016`.[^1] Incluso los tipos de datos básicos como enteros, cadenas y listas son objetos en sí mismos y tienen sus propios métodos y propiedades.

Las clases también son objetos y sirven para crear objetos. Tal vez parezca un poco complicado en este momento, pero con la práctica se hará más clara esta idea.

En términos de la Programación Orientada a Objetos, podemos entender un objeto como una entidad que tiene un estado y un comportamiento. El estado de un objeto se refiere a sus propiedades y el comportamiento a sus métodos. Por ejemplo, un objeto de tipo `Coche` puede tener como propiedades el color, la marca, el modelo, etc. y como métodos el arrancar, el frenar, el girar, etc.

Otro aspecto importante de entender, antes de iniciar nuestro proceso de programación, es la idea de instanciación. Cuando creamos un objeto a partir de una clase, decimos que estamos instanciando un objeto de esa clase. Por ejemplo, podemos instanciar un objeto de la clase `Coche` y asignarlo a una variable:

```{code-cell} ipython3
class Coche:
    def __init__(self, color, marca, modelo):
        self.color = color
        self.marca = marca
        self.modelo = modelo

mi_coche = Coche("rojo", "Renault", "Megane")
```

El objeto `mi_coche` es una instancia de la clase `Coche` y tiene como propiedades el color, la marca y el modelo. Podemos acceder a ellas de la siguiente forma:

```{code-cell} ipython3
print(mi_coche.color)
print(mi_coche.marca)
print(mi_coche.modelo)
```

Podríamos verbalizarlo de la siguiente manera:

Una clase es una plantilla para la creación de objetos. Cuando creamos un objeto a partir de una clase, decimos que estamos instanciando un objeto de esa clase.

Lo que es relevante de entender en este momento, es que las clases nos ayudan a pensar como programadores. En lugar de pensar en un problema como un conjunto de variables y funciones, podemos pensar en él como un conjunto de objetos que interactúan entre sí. Esto nos permite abstraer el problema y centrarnos en los aspectos más importantes. Lo anterior implica que debamos diseñar antes de escribir código y en este sentido pasamos de un enfoque imperativo (una sucesión de instrucciones) a un enfoque orientado a objetos.

## Notas

[^1]: Puedes consultar la cita y algunos ejemplos en el siguiente enlace: https://jakevdp.github.io/WhirlwindTourOfPython/03-semantics-variables.html#Everything-Is-an-Object
