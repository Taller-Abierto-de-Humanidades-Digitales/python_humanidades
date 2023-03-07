---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Diccionarios

Los diccionarios son estructuras de datos que permiten asociar información a través de claves y valores. De cierta manera, un diccionario puede ir desde algo muy simple hasta prácticamente representar una base de datos. En este capítulo veremos cómo crear diccionarios, cómo acceder a sus elementos y cómo modificarlos.

## Creando diccionarios

Los diccionarios se definen con llaves `{}` y los elementos se separan con comas `,`. Por ejemplo, un diccionario con los protagonistas de la serie de televisión "Seinfeld" se puede definir como:

```{code-cell} ipython3
protagonistas = {
    "Jerry": "Jerry Seinfeld",
    "George": "Jason Alexander",
    "Elaine": "Julia Louis-Dreyfus",
    "Kramer": "Michael Richards"
}

print(protagonistas)
```

De esa manera, tenemos un listado de los protagonistas y a cada uno de ellos le hemos asignado un valor. En este caso, el valor es el nombre del actor o actriz que lo interpretó.

### Determinar si un diccionario está vacío

Para determinar si un diccionario está vacío, podemos usar la función `len()`. Por ejemplo:

```{code-cell} ipython3
protagonistasFriends = {}
len(protagonistasFriends)
```

Asimismo, podemos evaluar si un diccionario está vacío en una condición, por ejemplo:

```{code-cell} ipython3
if protagonistasFriends:
    print("El diccionario protagonistasFriends no está vacío")
elif protagonistas:
    print("El diccionario protagonistas no está vacío")
else:
    print("Los diccionarios están vacíos")
```

Observa que en este caso evaluó si `protagonistasFriends` tenía elementos (`False`) y en caso contrario evaluó si `protagonistas` tenía elementos (`True`). En caso de que ambos diccionarios estuvieran vacíos, Python ejecutaría el `else`.

## Operaciones con diccionarios

Eric Matthes explica que un diccionario es "una colección de *pares de valores clave*" donde "cada *clave* está conextada a un valor, y se puede usar una clave para acceder a un valor asociado con dicha clave" {cite}`matthes_python_2016`. El valor de una clave puede ser cualquier tipo de dato, incluso otro diccionario.

Por ejemplo, podemos hacer un diccionario más complejo para que cada protagonista tenga un diccionario con sus datos personales:

```{code-cell} ipython3
protagonistas = {
    "Jerry": {
        "nombre": "Jerry Seinfeld",
        "año_nacimiento": 1954,
        "nacionalidad": "Estadounidense",
        "género": "Masculino"
    },
    "George": {
        "nombre": "Jason Alexander",
        "año_nacimiento": 1959,
        "nacionalidad": "Estadounidense",
        "género": "Masculino"
    },
    "Elaine": {
        "nombre": "Julia Louis-Dreyfus",
        "año_nacimiento": 1961,
        "nacionalidad": "Estadounidense",
        "género": "Femenino"
    },
    "Kramer": {
        "nombre": "Michael Richards",
        "año_nacimiento": 1949,
        "nacionalidad": "Estadounidense",
        "género": "Masculino"
    }
}

print(protagonistas)
```

De esa manera podemos acceder no solamente a un valor asociado a una clave (por ejemplo, el nombre de la actriz que intepretó a Elaine), sino también a un diccionario asociado a una clave (por ejemplo, la edad de cada uno de los protagonistas).

### Accediendo a los elementos de un diccionario

Para acceder a los elementos de un diccionario, podemos usar la sintaxis `diccionario[clave]`. Por ejemplo, para acceder al nombre de la actriz que interpretó a Elaine:

```{code-cell} ipython3
protagonistas["Elaine"]["nombre"]
```

Presta atención a la sintaxis que usamos para acceder al valor deseado. Primero, accedemos al diccionario `protagonistas` y luego a la clave `"Elaine"`. Esa clave nos devuelve un diccionario con los datos de Elaine. Finalmente, accedemos a la clave `"nombre"` para obtener el valor deseado.

Hagámoslo por pasos:

```{code-cell} ipython3
# aquí accedemos al diccionario "protagonistas" y a la clave "Elaine"
valor1 = protagonistas["Elaine"]
print(valor1)
```

```{code-cell} ipython3
# aquí accedemos al diccionario "valor1" y a la clave "nombre"
valor2 = valor1["nombre"]
print(valor2)
```

Si la clave no existe, Python nos arrojará un error indicando que la clave es incorrecta:

```{code-cell} ipython3
protagonistas["George"]["apellido"]
```

### Agregando elementos a un diccionario

Para agregar elementos a un diccionario, podemos usar la sintaxis `diccionario[clave] = valor`. Por ejemplo, para agregar el apellido de George:

```{code-cell} ipython3
protagonistas["George"]["apellido"] = "Costanza"
protagonistas["George"]
```

Notarás que el orden de los elementos no cambió. Esto es porque los diccionarios no tienen un orden definido. También notarás que no hay problema con que los demás miembros de la serie no tengan apellido. Pero si intentáramos acceder al apellido de Elaine, Python nos arrojaría un error:

```{code-cell} ipython3
protagonistas["Elaine"]["apellido"]
```

Una estrategia clave para trabajar con diccionarios es la consistencia. Modificar un diccionario para que todos los elementos tengan la misma estructura es una buena práctica, incluso si los valores de algunos elementos son nulos.

### Agregar una lista como valor de un diccionario

Podemos agregar una lista como valor de un diccionario. Por ejemplo, para agregar los empleos que tuvo George Costanza:

```{code-cell} ipython3
protagonistas["George"]["empleos"] = ["Rick Bahr Properties", "Sanalac", "Pendant Publishing", "New York Yankees", "Play Now", "Kruger Industrial Smoothing"]
protagonistas["George"]
```

De este modo, es posible acceder a los elementos de la lista e iterar sobre ellos:

```{code-cell} ipython3
for trabajo in protagonistas["George"]["empleos"]:
    print(trabajo)
```

### Agregar un diccionario como valor de un diccionario

Podemos agregar un diccionario como valor de un diccionario. Por ejemplo, para agregar los datos de la prometida de George Costanza:

```{code-cell} ipython3
protagonistas["George"]["esposa"] = {
    "nombre": "Susan",
    "año_nacimiento": 1960,
    "nacionalidad": "Estadounidense",
    "género": "Femenino"
}
protagonistas["George"]
```

De este modo, es posible acceder a este nuevo diccionario y a sus elementos:

```{code-cell} ipython3
protagonistas["George"]["esposa"]["nombre"]
```

Como te darás cuenta, el diccionario puede tener cualquier cantidad de valores anidados y de múltiples tipos, incluso otros diccionarios. Por esto, es importante tener una estructura clara en el diccionario para que no haya mezclas de datos que puedan hacerlo ilegible.

### Eliminar elementos de un diccionario

Para eliminar elementos de un diccionario, podemos usar la instrucción `del`. Por ejemplo, para eliminar el apellido de George:

```{code-cell} ipython3
del protagonistas["George"]["apellido"]
protagonistas["George"]
```

Volvimos al diccionario original :D

### Modificar los valores de un diccionario

Para modificar los valores de un diccionario, podemos usar la sintaxis `diccionario[clave] = valor`. Por ejemplo, para modificar el nombre de la actriz que interpretó a Elaine:

```{code-cell} ipython3
protagonistas["Elaine"]["nombre"] = "Julia Scarlett Elizabeth Louis-Dreyfus"
protagonistas["Elaine"]
```

Incluso podemos hacer una operación y devolver una nueva clave con la edad de Elaine basados en el año de nacimiento:

```{code-cell} ipython3
protagonistas["Elaine"]["edad"] = 2023 - protagonistas["Elaine"]["año_nacimiento"]
protagonistas["Elaine"]
```

## Síntesis

Ya abordamos los aspectos básicos de los diccionarios. En el siguiente apartado, veremos cómo iterar sobre los elementos de un diccionario, tanto para obtener los valores y claves, como para agregar y eliminar elementos.
