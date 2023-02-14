# Listas

Las listas son conjuntos de datos en Python. Sus características básicas son:

- Son **mutables**. Esto significa que podemos modificar su contenido.
- Son **ordenadas**. Esto significa que los elementos de una lista tienen un orden y podemos acceder a ellos mediante su posición.
- Son **iterables**. Esto significa que podemos recorrer sus elementos con un bucle `for`.

Además, en Python las listas pueden estar compuestas de cualquier tipo de datos, incluso de otras listas, diccionarios, tuplas, entre otros. Esto hace que sean muy flexibles, a la vez que requieren que tengamos cuidado de no mezclar tipos de datos de manera inadecuada.

## Creación de listas

Para crear una lista en Python, debemos encerrar sus elementos entre corchetes `[]` y separarlos con comas `,`. Por ejemplo:

```python
lista = ["a", "b", "c", "d", "e"]
```

Si queremos crear una lista vacía, debemos hacerlo de la siguiente manera:

```python
lista_vacia = []
```

## Acceso a elementos de una lista

Para acceder a un elemento de una lista, debemos indicar su posición entre corchetes `[]`. Por ejemplo, si queremos acceder al primer elemento de la lista `lista` que creamos en el ejemplo anterior, debemos hacer lo siguiente:

```python
lista[0]
```

```shell
'a'
```

En Python, las posiciones de los elementos de una lista empiezan en `0`, por lo que el primer elemento de una lista es el que está en la posición `0`. Por lo tanto, si queremos acceder al segundo elemento de la lista, debemos hacer lo siguiente:

```python
lista[1]
```

```shell
'b'
```

Si queremos acceder al último elemento de la lista, podemos hacerlo de dos maneras:

```python
lista[-1]
```

```shell
'e'
```

```python
lista[len(lista) - 1]
```

```shell
'e'
```

En este caso, el último elemento de la lista es el que está en la posición `len(lista) - 1`, donde `len(lista)` es la longitud de la lista, es decir, el número de elementos que contiene.

## Modificación de elementos de una lista

Para modificar un elemento de una lista, debemos indicar su posición entre corchetes `[]` y asignarle un nuevo valor. Por ejemplo, si queremos modificar el primer elemento de la lista `lista` que creamos en el ejemplo anterior, debemos hacer lo siguiente:

```python
lista[0] = "A"
```

```shell
['A', 'b', 'c', 'd', 'e']
```

## Añadir elementos a una lista

Para añadir un elemento al final de una lista, debemos utilizar el método `append()`. Por ejemplo, si queremos añadir el elemento `"f"` al final de la lista `lista` que creamos en el ejemplo anterior, debemos hacer lo siguiente:

```python
lista.append("f")
```

```shell
['A', 'b', 'c', 'd', 'e', 'f']
```

Si queremos añadir un elemento en una posición determinada de una lista, debemos utilizar el método `insert()`. Por ejemplo, si queremos añadir el elemento `"z"` en la posición `2` de la lista `lista` que creamos en el ejemplo anterior, debemos hacer lo siguiente:

```python
lista.insert(2, "z")
```

```shell
['A', 'b', 'z', 'c', 'd', 'e', 'f']
```

## Eliminar elementos de una lista

Para eliminar un elemento de una lista, debemos utilizar el método `remove()`. Por ejemplo, si queremos eliminar el elemento `"z"` de la lista `lista` que creamos en el ejemplo anterior, debemos hacer lo siguiente:

```python
lista.remove("z")
```

```shell
['A', 'b', 'c', 'd', 'e', 'f']
```

Si queremos eliminar un elemento de una posición determinada de una lista, debemos utilizar el método `pop()`. Por ejemplo, si queremos eliminar el elemento que está en la posición `2` de la lista `lista` que creamos en el ejemplo anterior, debemos hacer lo siguiente:

```python
lista.pop(2)
```

```shell
['A', 'b', 'd', 'e', 'f']
```

Si queremos eliminar todos los elementos de una lista, debemos utilizar el método `clear()`. Por ejemplo, si queremos eliminar todos los elementos de la lista `lista` que creamos en el ejemplo anterior, debemos hacer lo siguiente:

```python
lista.clear()
```

```shell
[]
```

## Operaciones con listas

### Concatenación

Para concatenar dos listas, debemos utilizar el operador `+`. Por ejemplo, si queremos concatenar las listas `lista1` y `lista2` que creamos en el ejemplo anterior, debemos hacer lo siguiente:

```python
lista1 = ["a", "b", "c"]
lista2 = ["d", "e", "f"]
lista1 + lista2
```

```shell
['a', 'b', 'c', 'd', 'e', 'f']
```

### Repetición

Para repetir una lista, debemos utilizar el operador `*`. Por ejemplo, si queremos repetir la lista `lista` que creamos en el ejemplo anterior, debemos hacer lo siguiente:

```python
lista = ["a", "b", "c"]
lista * 2
```

```shell
['a', 'b', 'c', 'a', 'b', 'c']
```

### Comprobación de pertenencia

Para comprobar si un elemento pertenece a una lista, debemos utilizar el operador `in`. Por ejemplo, si queremos comprobar si el elemento `"a"` pertenece a la lista `lista` que creamos en el ejemplo anterior, debemos hacer lo siguiente:

```python
lista = ["a", "b", "c"]
"a" in lista
```

```shell
True
```

### Longitud de una lista

Para obtener la longitud de una lista, debemos utilizar la función `len()`. Por ejemplo, si queremos obtener la longitud de la lista `lista` que creamos en el ejemplo anterior, debemos hacer lo siguiente:

```python
lista = ["a", "b", "c"]
len(lista)
```

```shell
3
```

## Recorrer una lista

Para recorrer una lista, podemos utilizar un bucle `for`. Por ejemplo, si queremos recorrer la lista `lista` que creamos en el ejemplo anterior, debemos hacer lo siguiente:

```python
lista = ["a", "b", "c"]
for elemento in lista:
    print(elemento)
```

```shell 
a
b
c
```

## Ordenar una lista

Para ordenar una lista, debemos utilizar el método `sort()`. Por ejemplo, si queremos ordenar la lista `lista` que creamos en el ejemplo anterior, debemos hacer lo siguiente:

```python
lista = ["c", "a", "b"]
lista.sort()
```

```shell
['a', 'b', 'c']
```

También podemos hacer lo de manera invertida con el método `reverse()`. Por ejemplo, si queremos ordenar la lista `lista` que creamos en el ejemplo anterior, debemos hacer lo siguiente:

```python
lista = ["a", "b", "c"]
lista.reverse()
```

```shell
['c', 'b', 'a']
```

## Copiar una lista

Para copiar una lista, debemos utilizar el método `copy()`. Por ejemplo, si queremos copiar la lista `lista` que creamos en el ejemplo anterior, debemos hacer lo siguiente:

```python
lista = ["a", "b", "c"]
lista_copia = lista.copy()
```

```shell
['a', 'b', 'c']
```

## Listas multidimensionales

Una lista multidimensional es una lista que contiene otras listas. Por ejemplo, si queremos crear una lista multidimensional, debemos hacer lo siguiente:

```python
lista = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
```

```shell
[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
```

Para acceder a un elemento de una lista multidimensional, debemos indicar la posición de la lista y la posición del elemento dentro de la lista. Por ejemplo, si queremos acceder al elemento `5` de la lista `lista` que creamos en el ejemplo anterior, debemos hacer lo siguiente:

```python
lista = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
lista[1][1]
```

```shell
'e'
```

## Listas por comprensión

Las listas por comprensión son una forma de crear listas de forma sencilla. Por ejemplo, si queremos crear una lista con los números del `1` al `10`, debemos hacer lo siguiente:

```python
lista = [i for i in range(1, 11)]
```

```shell
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Podemos hacer algo similar con letras del alfabeto, pero en este caso debemos utilizar la función `chr()` para obtener el código ASCII de cada letra. Por ejemplo, si queremos crear una lista con las letras del `a` al `z`, debemos hacer lo siguiente:

```python
lista = [chr(i) for i in range(97, 123)]
```

```shell
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
```
