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

# Iterar a través de un diccionario

Un diccionario es una estructura de datos y, como tal, puede contener una cantidad sumamente grande de elementos. En cuanto mayor sea el tamaño del diccionario, las operaciones para acceder a los valores deben ser un poco más complejas. En este capítulo veremos cómo iterar a través de un diccionario.

Para estos ejercicios, crearemos un diccionario a partir de la siguiente bibliografía:

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

Como verás, la estructura diccionario contiene una serie de claves propias de un conjunto bibliográfico: `tipo`, `autor`, `título`, `editorial`, `lugar`, `fecha`, `edición` y `idioma`. No todos los elementos tienen todas las claves, por lo que debemos considerar que el campo está vacío si no existe.

## Iterar a través pares clave-valor

Para iterar a través de un diccionario, podemos utilizar el método `items()`. Este método devuelve una lista de tuplas, donde cada tupla contiene una clave y su valor correspondiente.

```{code-cell} ipython3

for clave, valor in bibliografia.items():
    print(f"Clave: {clave} :: Valor: {valor}")
```

En este caso la clave es el identificador de cada elemento bibliográfico (por ejemplo, `001`), y el valor es el diccionario que contiene los campos de cada libro.

Iterar sobre este diccionario sería útil para, por ejemplo, obtener un listado de todos los libros que se encuentran en la bibliografía. Para ello, podemos utilizar la clave `tipo` para filtrar los elementos que sean libros.

```{code-cell} ipython3

print("        Listado de libros".upper())

for clave, valor in bibliografia.items():
    if valor["tipo"] == "libro":
        print(f"""
        Identificador: {clave}
        Título: {valor["titulo"]}
        Autor: {valor["autor"][0]["apellido"]}, {valor["autor"][0]["nombre"]}
        Editorial: {valor["editorial"]}
        Lugar: {valor["lugar"]}
        Fecha: {valor["fecha"]}
        """)
```

## Iterar a través de las claves

Si queremos iterar a través de las claves de un diccionario, podemos utilizar el método `keys()`.

```{code-cell} ipython3

for clave in bibliografia.keys():
    print(f"Clave: {clave}")
```

De hecho, este es el comportamiento predeterminado al iterar sobre un diccionario, de tal manera que si no utilizamos la función `keys()`, el resultado será el mismo.

```{code-cell} ipython3

for clave in bibliografia:
    print(f"Clave: {clave}")
```

Usar o no la función `keys()` es un asunto de legibilidad.

La utilidad de iterar sobre las claves está en el hecho de que podemos utilizarlas para acceder a los valores correspondientes, por ejemplo:

```{code-cell} ipython3

for clave in bibliografia.keys():
    print(f"ID: {clave}\nTítulo: {bibliografia[clave]['titulo']}")
```

También, debido a que el método `keys()` devuelve una lista de claves, podemos aplicar cualquiera de los métodos de listas que hemos visto, por ejemplo, determinar si una clave está en el diccionario:

```{code-cell} ipython3

if "006" not in bibliografia.keys():
    print("La clave 006 no existe en el diccionario")
```

## Agregar elementos de una lista a un diccionario

Ahora, veamos cómo podemos agregar elementos de una lista a un diccionario. Por ejemplo, si tenemos una lista similar a la de los ejercicios anteriores:

```{code-cell} ipython3

lista_bibliografia = [
    "Edgar Alan Poe; Cuentos completos; 2019; Alianza Editorial",
    "David Hume; Del conocimiento; 1984; Aguilar",
    "Ludwig Wittgenstein; Tractatus Logico-Philosophicus; 2017; Tecnos",
    "Francois Hartog; Cronos; 2022; Siglo XXI",
    "David Spiegelhalter; The art of statistics; 2021; Basic Books"
]

```

Podemos crear agregar estos elementos al diccionario `bibliografia` de la siguiente manera:

```{code-cell} ipython3

for elemento in lista_bibliografia:
    # obtener la última clave del diccionario, convertirla a entero y sumarle 1
    clave = int(list(bibliografia.keys())[-1]) + 1
    # convertir la clave a string y darle el formato de 3 dígitos
    clave = str(clave).zfill(3)
    # agregar el elemento a la bibliografía
    bibliografia[clave] = {
        "tipo": "libro",
        "autor": [{"nombre": elemento.split(";")[0].split(" ")[0], "apellido": elemento.split(";")[0].split(" ")[1]}],
        "titulo": elemento.split(";")[1],
        "editorial": elemento.split(";")[3],
        "fecha": int(elemento.split(";")[2]),
        "lugar": "" # dejamos vacío el campo lugar para evitar errores en la iteración
    }

```

Podemos iterar sobre los valores para comprobar que se han agregado correctamente:

```{code-cell} ipython3
print("        Listado de libros".upper())
for clave, valor in bibliografia.items():
    if valor["tipo"] == "libro":
        print(f"""
        Identificador: {clave}
        Título: {valor["titulo"]}
        Autor: {valor["autor"][0]["apellido"]}, {valor["autor"][0]["nombre"]}
        Editorial: {valor["editorial"]}
        Lugar: {valor["lugar"]}
        Fecha: {valor["fecha"]}
        """)
```

## Agregar valores a través de diccionarios

Ahora, supongamos que queremos corregir el valor vacío del campo `lugar` para los libros que hemos agregado. Para ello, podemos crear un diccionario con los valores correspondientes:

```{code-cell} ipython3

lugares = {
    "006": "Madrid",
    "007": "Madrid",
    "008": "Madrid",
    "009": "México",
    "010": "Nueva York"
}
```

Y luego, iterar sobre el diccionario `lugares` para agregar los valores correspondientes al diccionario `bibliografia`:

```{code-cell} ipython3

for clave, valor in lugares.items():
    bibliografia[clave]["lugar"] = valor

```

Nota que lo que hicimos en esta operación fue tomar el valor coincidente en ambos diccionarios (la clave) y tomar el único valor que tiene el diccionario ``lugares` para esa clave. Debido a que la coincidencia es la clave, podemos utilizarla para acceder al valor correspondiente en el diccionario `bibliografia` y agregar el valor correspondiente a la clave anidada `lugar`.

Finalmente, podemos volver a iterar sobre el diccionario `bibliografia` para comprobar que los valores se han agregado correctamente:

```{code-cell} ipython3

print("        Listado de libros".upper())
for clave, valor in bibliografia.items():
    if valor["tipo"] == "libro":
        print(f"""
        Identificador: {clave}
        Título: {valor["titulo"]}
        Autor: {valor["autor"][0]["apellido"]}, {valor["autor"][0]["nombre"]}
        Editorial: {valor["editorial"]}
        Lugar: {valor["lugar"]}
        Fecha: {valor["fecha"]}
        """)
```

## Síntesis

Como habrás visto, los diccionarios son estructuras de datos que hacen muy eficiente la búsqueda y almacenamiento de información. En estos ejercicios todavía trabajamos con datos efímeros (se agregan, procesan y finalizan con el mismo programa), pero esta misma estructura se puede utilizar para almacenar información en archivos de texto (JSON) o bases de datos, y luego recuperarla para procesarla. Es por esta razón que es fundamental conocer y dominar los diccionarios.
