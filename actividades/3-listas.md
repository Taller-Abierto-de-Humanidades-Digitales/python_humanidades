# Actividad 3: Listas (operaciones básicas)

## Ejercicio 1: Crear un listado de autores

1.1. En este ejercicio, deberás crear un listado con al menos cinco autores y autoras, pueden ser de un tema literario, científico, de divulgación, entre otros. Realiza un `print` de cada elemento de la lista a través de un índice.

1.2. Ahora, construye un mensaje personalizado para cada autora y autor. La estructura del mensaje debe ser la siguiente:

> Hola, soy [nombre del autor o autora] y me conocen por el libor [título del libro].

1.3. Ahora, crea una lista con los títulos de los libros de cada autor o autora. Realiza un `print` de cada elemento de la lista a través de un índice que construya el mensaje anterior.

## Ejercicio 2: Crear un microcatálogo bibliográfico

2.1. En este ejercicio, deberás crear un microcatálogo bibliográfico con al menos cinco libros. Cada libro debe tener un título, un autor o autora, un año de publicación y un género. Realiza un `print` de la lista completa para ver los datos. **Nota**: Es muy importante que tengas en cuenta la sintaxis de la lista. Cada libro debe ser un elemento y los valores de título, autor o autora, año y género deben estar en una cadena de caracteres. Por ejemplo:

```python
libro = ["Cuentos completos; Jorge Luis Borges; 1995; Ficción"]
```

2.2. Ahora, reemplaza uno de los libros por otro. Realiza un `print` de la lista completa para mostrar los cambios.

2.3. Añade tres nuevos libros a tu lista de la siguiente manera:

* Un libro al inicio mediante el método `insert()`.
* Un libro al final mediante el método `append()`.
* Un libro en la posición 3 mediante el método `insert()`.

2.4. Utiliza la función `len()` para conocer el número de elementos de la lista y construye el mensaje:

> La lista tiene ahora [número de elementos] libros.

2.5. Ahora, elimina un libro de la lista mediante el método `pop()`. Realiza un `print` de la lista completa para mostrar los cambios.

2.6. Ahora, elimina un libro de la lista mediante el método `remove()`. Realiza un `print` de la lista completa para mostrar los cambios.

2.7. Ahora, elimina un libro de la lista mediante el método `del`. Realiza un `print` de la lista completa para mostrar los cambios.

2.8. Utiliza la función `len()` para conocer el número de elementos de la lista y construye el mensaje:

> La lista tiene ahora [número de elementos] libros.

2.9. Finalmente, imprime cada uno de los libros de la lista y que pueda construir el siguiente mensaje:

> El libro [título del libro] fue escrito por [autor o autora] en el año [año de publicación] y es de género [género].

## Ejercicio 3: Organizar una lista

3.1. Aprovechando el microcatálogo bibliográfico realizaremos las siguientes operaciones:

* Crea una variable llamada `titulo_asc` que contenga una copia de la lista de libros ordenada alfabéticamente por título. Usa el método `sort()` para ordenar la lista.

* Crea una variable llamada `titulo_desc` que contenga una copia de la lista de libros ordenada alfabéticamente inversa por título. Usa el método `reverse()` para ordenar la lista.

3.2. Imprime los primeros dos resultados de cada lista.

## Envío

Los tres ejercicios deberán ser realizados en un archivo llamado `actividad3.py`. Guárdalo en el directorio con tu nombre (de preferencia en un subdirectorio).

Para entregar la actividad, debes hacer un `commit` de los modificados y hacer un `push` de tu brazo al repositorio remoto.

```bash
git add .
git commit -m "Entrega de la actividad 3"
git push -u origin nombre-del-brazo
```

### Fecha de entrega

Entrega la actividad antes del martes 14 de febrero.
