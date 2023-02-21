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

# Introducción a los condicionales

En la lección anterior exploramos cómo realizar una tarea repetitiva con un bucle *for*, ese es un paso muy importante hacia la automatización de nuestras tareas. Ahora, podemos hacer que estas tareas sean mucho más complejas si tomamos decisiones en función de ciertas condiciones lógicas. Para ello, Python dispone de las sentencias `if` y `else`.

Antes de iniciar nuestro programa en Python, quiero que veamos un ejemplo de uso de condicionales en [Scratch](https://scratch.mit.edu/). En este ejemplo vamos a hacer lo siguiente:

* Cada vez que se pulse la barra espaciadora se asignará un valor aleatorio entre 1 y 10 a la variable *my variable*
* Si el valor de *my variable* es menor que 50, el personaje se moverá 100 pasos, rebotando si llega al borde, y hará el sonido de *meow*
* Si el valor de *my variable* es mayor que 50, el personaje cambiará de gesto, irá a una posición aleatoria en el cuadro y no hará el sonido de *meow*.
* En ambos casos, el personaje mostrará un mensaje con el valor de *my variable*.

Para ello, vamos a utilizar los bloques `if` y `else` de Scratch. El bloque `if` se ejecuta si la condición que se le pasa es verdadera, y el bloque `else` se ejecuta si la condición es falsa. En el siguiente ejemplo, el bloque `if` se ejecuta si el valor de *my variable* es menor que 50, y el bloque `else` se ejecuta si el valor de *my variable* es mayor que 50.

![Scratch](../_static/imgs/scratch.png)

Juega con el ejemplo e intenta identificar qué hace cada bloque y por qué el personaje se comporta de la manera que lo hace.

<iframe src="https://scratch.mit.edu/projects/807081542/embed" allowtransparency="true" width="485" height="402" frameborder="0" scrolling="no" allowfullscreen></iframe>

Si intentáramos replicar este ejemplo en Python, tendríamos que hacer algo similar a lo siguiente [^1]:

```{code-cell} ipython3
import random

my_variable = random.randint(1, 100)

posicion_personaje = (0, 0)

if my_variable < 50:
    posicion_personaje = (posicion_personaje[0] + 100, posicion_personaje[1])
    print(f"{my_variable}\nEl personaje se ha movido a la posición {posicion_personaje}\nMeow!")
else:
    posicion_personaje = (random.randint(0, 480), random.randint(0, 360))
    print(f"{my_variable}\nEl personaje se ha movido a la posición {posicion_personaje}\n")
```

No te preocupes si no entiendes completamente este programa. Lo que debes saber por lo pronto es que cada vez que ejecutes este código el personaje se habrá movido a una posición que bien puede ser `(100, 0)` o cualquier coordenada aleatoria entre `(0, 0)` y `(480, 360)`, es decir, el personaje toma una decisión en función de la condición que se le pasa, la cual desconocemos por completo al inicio del programa. Copia este código en un archivo de Python y ejecútalo varias veces para ver cómo se comporta el personaje.

Entendamos entonces las condicionales como una forma de tomar decisiones de acuerdo con una condición lógica que puede ser verdadera o falsa. Esto se puede representar con un diagrama de flujo, como el siguiente:

![Diagrama de flujo](../_static/imgs/condicional.png)

Vemos como, dependiendo de si se cumple o no la condición (si el valor de `my_variable` es menor a 50) el valor de `posición` será diferente. Esta simple estructura es la base de la programación condicional en Python.

A continuación veremos cómo se realizan las pruebas condicionales en Python para obtener resultados de verdad o falsedad.

[^1]: Este ejemplo es extremadamete sintético. Si quisiéramos replicar el ejemplo de Scratch en Python, tendríamos que utilizar la librería [Pygame](https://www.pygame.org/news) para dibujar el personaje y el fondo, y la librería [Pygame Zero](https://pygame-zero.readthedocs.io/en/stable/) para gestionar los eventos de teclado y ratón. No obstante, es un ejemplo funcional para empezar a entender el funcionamiento de las sentencias `if` y `else`.
