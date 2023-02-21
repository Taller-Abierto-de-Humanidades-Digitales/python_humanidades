# Actividad 5: Condicionales y sentencias `if`

Para realizar estos ejercicios, reutilizaremos el listado de libros que elaboraste en la [actividad 4](4-iteraciones.md)

## Ejercicio 1: Lista de libros a partir de palabras clave

Crea un programa que guarde en una lista los libros que contengan una palabra clave. Para ello, deberás utilizar la sentencia `if` y "guardar" la palabra clave en una variable. Por ejemplo, si la palabra clave es "México", el programa deberá guardar en una lista los libros que contengan esta palabra. Al final, deberás imprimir la lista de libros que contengan la palabra clave.

El programa deberá funcionar con coincidencias independientes de mayúsculas y minúsculas. Por ejemplo, si la palabra clave es "méxico" y el título del libro es "Historia de la conquista de México", el programa deberá guardar el libro en la lista.

Asimismo, el programa deberá funcionar con cualquier palabra clave que se introduzca. En caso de que la palabra clave no se encuentre en ningún libro, el programa deberá imprimir un mensaje que indique que no se encontraron coincidencias.

## Ejercicio 2: Lista de libros a anteriores o posteriores a una fecha

Crea un programa que permita encontrar en tu listado de libros aquellos que fueron publicados antes o después de una fecha determinada. Al igual que en el ejercicio anterior, deberás guardar el resultado en una lista e imprimir la lista de libros que cumplan con la condición.

Guarda la fecha de búsqueda en una variable y comprueba que su resultado sea correcto tanto para fechas anteriores como posteriores. Esto implica que debes crear una condición que valide si la consulta es para libros anteriores o posteriores a la fecha de búsqueda.

En caso de que no se encuentren libros que cumplan con la condición, el programa deberá imprimir un mensaje que indique que no se encontraron coincidencias.

## Ejercicio 3: Listado de títulos de libros por género

En este tercer programa deberás crear un listado de títulos de libros de tu listado a partir del género de la publicación. Para ello puedes buscar el género por coincidencia en cada elemento de la lista (por ejemplo, `if "ensayo" in libro`) o forzar una coincidencia en el campo correspondiente al género (por ejemplo, `if libro.split("; ")[-1] == "ensayo"`). En cualquiera de los casos, deberás guardar el resultado en una lista e imprimir la lista de libros que cumplan con la condición.

Al igual que en el ejercicio 1, el programa deberá funcionar con coincidencias independientes de mayúsculas y minúsculas.

En caso de que no se encuentren libros que cumplan con la condición, el programa deberá imprimir un mensaje que indique que no se encontraron coincidencias.

## Ejercicio 4: Inventario de libros por categoría

En este ejercicio realizarás un inventario de libros por su categoría. Para ello, deberás crear al menos dos listados vacíos para cada categoría (p. ej: "historia", "filosofía"). Luego, deberás recorrer tu listado de libros y guardar cada libro en el listado correspondiente a su categoría. Por ejemplo, si el libro es de historia, deberás guardarlo en el listado de "historia". En caso de que el libro no tenga una categoría, deberás guardarlo en un listado llamado "otras categorías".

Para finalizar el programa, deberás imprimir el listado de libros de tal manera que se muestre un mensaje similar al siguiente:

```shell
Libros de historia:
- <autor>, <título> (<año>), <género>

Libros de filosofía:
- <autor>, <título> (<año>), <género>
- <autor>, <título> (<año>), <género>

Otros libros:
- <autor>, <título> (<año>), <género>
- <autor>, <título> (<año>), <género>
```

## Ejercicio 5: Lista de títulos por autor y fecha

En este ejercicio deberás crear un listado de libros a partir de la coincidencia con un autor y una fecha determinada. Para ello, deberás crear una lista vacía y recorrer tu listado de libros. En caso de que el autor y la fecha del libro coincidan con los valores de búsqueda, deberás guardar el título, fecha y género en una lista. Al final, deberás imprimir la lista de libros que cumplan con la condición de la siguiente manera:

```shell
Libros de <autor> publicados en <año>:
- <título> (<año>), <género>
- <título> (<año>), <género>
```

En caso de que no se encuentren libros que cumplan con la condición, el programa deberá imprimir un mensaje que indique que no se encontraron coincidencias.

## Envío de la actividad

Al igual que las actividades anteriores, envía tu código a través de Github.

Los cinco ejercicios deberán ser realizados en un archivo llamado `actividad5.py`. Guárdalo en el directorio con tu nombre (de preferencia en un subdirectorio).

Para entregar la actividad, debes hacer un `commit` de los modificados y hacer un `push` de tu brazo al repositorio remoto.

```bash
git add .
git commit -m "Entrega de la actividad 5"
git push -u origin nombre-del-brazo
```

### Fecha de entrega

Entrega la actividad antes del martes 28 de febrero.
