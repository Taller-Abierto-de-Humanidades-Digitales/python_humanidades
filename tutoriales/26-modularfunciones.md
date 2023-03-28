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

# Crear módulos

En esta parte, realizaremos una modularización simple para que podamos entender cómo funciona. Para ello, vamos a retomar el diccionario con el conjunto de bibliografía que utilizamos en el capítulo [Iterar a través de un diccionario](18-iterardiccio.md). Para ello, creamos un archivo llamado `biblio.py` y escribimos el siguiente código:

```{code-cell} ipython3
bibliografia = {
    "001": {
        "tipo": "libro",
        "autor": [{"nombre": "Martin", "apellido": "Heidegger"}],
        "titulo": "Ser y tiempo",
        "editorial": "Trotta",
        "lugar": "Madrid",
        "fecha": 2003
    },
    "002": {
        "tipo": "libro",
        "autor": [{"nombre": "Fernand", "apellido": "Braudel"}],
        "titulo": "El Mediterráneo y el mundo mediterráneo en la época de Felipe II",
        "editorial": "Fondo de Cultura Económica",
        "lugar": "México",
        "fecha": 2022,
        "edicion": "tercera"
    },
    "003": {
        "tipo": "libro",
        "autor": [{"nombre": "Hans-Georg", "apellido": "Gadamer"}],
        "titulo": "Verdad y método I: fundamentos de una hermenéutica filosófica",
        "editorial": "Sígueme",
        "lugar": "Salamanca",
        "fecha": 1996
    },
    "004": {
        "tipo": "libro",
        "autor": [{"nombre": "Giorgio", "apellido": "Agamben"}],
        "titulo": "Estado de excepción",
        "editorial": "Adriana Hidalgo Editora",
        "lugar": "Buenos Aires",
        "fecha": 2010
    },
    "005": {
        "tipo": "libro",
        "autor": [{"nombre": "Ludwig", "apellido": "Wittgenstein"}],
        "titulo": "Zettel",
        "editorial": "University of California Press",
        "lugar": "Berkeley",
        "fecha": 1970,
        "idioma": "en"
    }
}
```

Este archivo funcionará como un módulo cuya única intención es almacenar un diccionario con la bibliografía.[^nota3]

En el **mismo directorio**, creamos un archivo llamado `biblioteca.py` y escribimos el siguiente código:

```{code-cell} ipython3
from biblio import bibliografia
```

Si todo ha salido bien, al ejecutar el código anterior no debería aparecer ningún error. En caso contrario, es posible que salga el error `ModuleNotFoundError: No module named 'biblio'`. Esto significa que Python no encuentra el módulo `biblio`. Para solucionarlo, debemos asegurarnos de que el archivo `biblio.py` se encuentra en el mismo directorio que el archivo `biblioteca.py`.

```{admonition} Nota
:class: tip
La importación de la celda anterior funciona, de hecho, al realizar la importación del archivo `biblio.py` que se encuentra en el directorio `tutoriales`. En ese sentido, este cuaderno funciona porque es posible llamar a esta `bibliografia` desde el "módulo" biblio.
```

Ahora, podemos crear una función que nos permita realizar búsquedas en el diccionario `bibliografia`. Para ello, escribimos el siguiente código:

```{code-cell} ipython3
def buscar_biblio(campo, valor):
    for clave, item in bibliografia.items():
        if item[campo] == valor:
            return clave, item
```

La función `buscar_biblio()` recibe dos argumentos: `campo` y `valor`. El argumento `campo` es una cadena de caracteres que indica el campo del diccionario `bibliografia` que queremos buscar ('tipo', 'autor', 'titulo', etc). El argumento `valor` la palabra o frase que queremos buscar en el campo indicado por `campo`. La función devuelve una tupla con la clave y el valor del diccionario `bibliografia` que cumple con la condición de búsqueda.

Escribamos ahora una función que permita darle formato a la salida de la función `buscar_biblio()`:

```{code-cell} ipython3
def formato_biblio(clave, item):
    print(f"Clave: {clave}")
    print(f"Tipo: {item['tipo']}")
    print(f"Autor: {item['autor'][0]['nombre']} {item['autor'][0]['apellido']}")
    print(f"Título: {item['titulo']}")
    print(f"Editorial: {item['editorial']}")
    print(f"Lugar: {item['lugar']}")
    print(f"Fecha: {item['fecha']}")
```

Finalmente, escribamos una función que una ambas funciones anteriores:

```{code-cell} ipython3
def busqueda_simple(campo, valor):
    clave, item = buscar_biblio(campo, valor)
    formato_biblio(clave, item)
```

Ahora, podemos ejecutar la función `busqueda_simple()` para buscar un libro por su título:

```{code-cell} ipython3
busqueda_simple("titulo", "Ser y tiempo")
```

Este código tiene un problema: si realizamos la importación desde otro archivo, se ejecutará la linea `busqueda_simple("titulo", "Ser y tiempo")` y se mostrará el resultado de la búsqueda. Esto no es deseable, ya que queremos que la función `busqueda_simple()` sea llamada desde otro archivo. Para solucionar este problema, podemos utilizar la instrucción `if __name__ == "__main__":`. Al final, nuestro código quedaría de la siguiente manera:

```{code-cell} ipython3
from biblio import bibliografia

def buscar_biblio(campo, valor):
    for clave, item in bibliografia.items():
        if item[campo] == valor:
            return clave, item

def formato_biblio(clave, item):
    print(f"Clave: {clave}")
    print(f"Tipo: {item['tipo']}")
    print(f"Autor: {item['autor'][0]['nombre']} {item['autor'][0]['apellido']}")
    print(f"Título: {item['titulo']}")
    print(f"Editorial: {item['editorial']}")
    print(f"Lugar: {item['lugar']}")
    print(f"Fecha: {item['fecha']}")

def busqueda_simple(campo, valor):
    clave, item = buscar_biblio(campo, valor)
    formato_biblio(clave, item)

if __name__ == "__main__":
    busqueda_simple("titulo", "Ser y tiempo")
```

La instrucción `if __name__ == "__main__":` permite ejecutar el código que se encuentra dentro de ella únicamente si el archivo es ejecutado como un programa principal. En caso contrario, el código no se ejecuta. Esto es útil cuando queremos importar un módulo y no queremos que se ejecute el código que se encuentra fuera de las funciones.

Finalmente, podemos crear un programa que aproveche el módulo `biblioteca` que acabamos de crear y que funcione como una interfaz de búsqueda de la bibliografía. Para ello, creamos un archivo llamado `busqueda.py` y escribimos el siguiente código:

```{code-cell} ipython3
from biblioteca import busqueda_simple

def menu():
    print("1. Buscar por título")
    print("2. Buscar por autor")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")
    return opcion

def main():
    opcion = menu()
    while opcion != "3":
        if opcion == "1":
            titulo = input("Ingrese el título: ")
            busqueda_simple("titulo", titulo)
        elif opcion == "2":
            autor = input("Ingrese el autor: ")
            busqueda_simple("autor", autor)
        else:
            print("Opción inválida")
        opcion = menu()

if __name__ == "__main__":
    main()
```

El programa `busqueda.py` importa la función `busqueda_simple()` del módulo `biblioteca`. Luego, define una función `menu()` que muestra un menú de opciones y devuelve la opción elegida por el usuario. La función `main()` muestra el menú y ejecuta la función `busqueda_simple()` según la opción elegida por el usuario. Finalmente, la función `main()` se ejecuta únicamente si el archivo es ejecutado como un programa principal.

Ahora puedes probar el programa `busqueda.py` desde la terminal:

```bash
python busqueda.py
```

Así podrás realizar búsquedas en la bibliografía de manera similar a este ejemplo:

```bash
python busqueda.py

Ingrese una opción: 1
Ingrese el título: Ser y tiempo
Clave: 001
Tipo: libro
Autor: Martin Heidegger
Título: Ser y tiempo
Editorial: Trotta
Lugar: Madrid
Fecha: 2003
Ingrese una opción:
```

De esta manera tenemos un buscador simple, modular y que podemos mantener de manera adecuada.

## Ejercicios

Estos ejercicios son opcionales. Si deseas practicar más, puedes intentar resolverlos.

1. Modifica el programa `busqueda.py` para que permita realizar búsquedas por año de publicación.
2. Modifica el programa `busqueda.py` para que no se presente el error `TypeError` cuando se ingresa un valor no existente (por ejemplo "Ser y Tiempo")
3. Modifica el programa `busqueda.py` para que permita realizar búsquedas por coincidencia parcial (por ejemplo, "Ser" o "tiempo").

## Notas

[^nota3]: En una aplicación real utilizaríamos un formato de archivo específico para almacenar información, como por ejemplo un archivo CSV o JSON. En las secciones del curso dedicadas a la lectura y escritura de archivos, abordaremos estos temas.
