# Actividad 7: Funciones

En esta actividad, pondremos a funcionar nuestro diccionario con el catálogo que creamos en la actividad anterior. Para esto, crearemos algunas funciones que nos permitan consultar el catálogo y realizar algunas operaciones con él.

## Ejercicio 1. Crear una función que permita consultar el catálogo

Este primer ejercicio servirá como un buscador por título. El programa debe pedirle al usuario que ingrese una palabra clave para el título del elemento del catálogo que desea consultar. Mediante una función, debe imprimirse en pantalla el listado de elementos que coincidan con la palabra clave ingresada. La función debe lidiar con mayúsculas y minúsculas, es decir, si el usuario ingresa "el" o "El", el programa debe imprimir los elementos que contengan "el" o "El".

También, deberá imprimirse el número de elementos encontrados. En caso de no encontrar elementos, el programa debe imprimir un mensaje indicando que no se encontraron elementos.

La función debe estar documentada y, si es el caso, cachar posible errores que puedan ocurrir.

El resultado debe ser similar a lo siguiente:

```shell
Ingresa una palabra clave para el título:  el
Se encontraron 2 elementos:
- El señor de los anillos
- El principito
```

## Ejercicio 2. Crear una función que permita consultar el catálogo por fecha

Este ejercicio es similar al anterior, pero en este caso, debe agregarse un parámetro que permita filtrar por fecha.

El programa debe solicitarle al usuario una palabra clave para el título y un año. En el mensaje del `input()` debe indicarse la forma de ingresar el año (por ejemplo, "Año de publicación (YYYY): ").

La función debe intentar lidiar con posibles errores de dedo (por ejemplo, si el usuario ingresa 1890 en lugar de 1980), para lo cual se pueden tomar las fechas extremas del catálogo e indicarlas en las instrucciones del `input()`.

La función debe imprimir el listado de elementos que coincidan con la palabra clave y el año ingresados. La función debe estar documentada y, si es el caso, cachar posible errores que puedan ocurrir.

El resultado debe ser similar a lo siguiente:

```shell
Ingresa una palabra clave para el título:  el
Año de publicación (YYYY):  1980

Se encontraron 1 elementos:
- El señor de los anillos
```

## Ejercicio 3. Crear una función para administrar el catálogo

En este ejercicio, crearemos una función que permita agregar elementos al catálogo. La función debe:

1. pedirle al usuario que ingrese los datos del elemento que desea agregar.
2. Debe agregar el elemento al catálogo y
3. Mostrar un mensaje indicando que el elemento fue agregado.

La función debe estar documentada y, si es el caso, cachar posible errores que puedan ocurrir.

## Envío de la actividad

Al igual que las actividades anteriores, envía tu código a través de Github.

Los cinco ejercicios deberán ser realizados en un archivo llamado `actividad7.py`. Guárdalo en el directorio con tu nombre (de preferencia en un subdirectorio).

Para entregar la actividad, debes hacer un `commit` de los modificados y hacer un `push` de tu brazo al repositorio remoto.

```bash
git add .
git commit -m "Entrega de la actividad 7"
git push -u origin nombre-del-brazo
```

### Fecha de entrega

Entrega la actividad antes del martes 14 de marzo.
