# Actividad 6: Manejo de diccionarios

En este ejercicio vamos a convertir nuestros listados bibliográficos en un catálogo de libros más estructurado utilizando diccionarios. Para ello, retomaremos el listado de libros que elaboraste en la [actividad 4](4-iteraciones.html)

## Ejercicio 1: Crear un diccionario a partir del listado bibliográfico

Para este ejercicio, convertiremos nuestro listado en un diccionario, donde cada elemento del diccionario será un libro.

Para ello, debemos primero, crear un diccionario vacío donde estarán incluidos los campos así:

```python
bibliografia = {"000" : {
    "tipo" : "",
    "autor" : [{"nombre" : "", "apellido" : ""}],
    "titulo" : "",
    "editorial" : "",
    "fecha" : 0,
    "lugar" : ""
    },
}
```

Posteriormente, itera sobre la lista de libros que retomas desde la actividad 4 y ajusta el diccionario para que contenga los datos de cada libro. Deberás actualizar el diccionario con la información que no haya estado disponible en tu listado original.

Al finalizar, imprime la lista con los libros que se encuentran en el diccionario de tal manera que se muestren de la siguiente manera:

```shell
        LISTADO DE LIBROS

        Identificador: 001
        Título: El arte de la guerra
        Autor: Sun Tzu
        Editorial: Ediciones B
        Lugar: Barcelona
        Fecha: 2000
```

## Ejercicio 2: Añadir nuevos elementos al diccionario

Ahora que ya tenemos un conjunto bibliográfico en formato diccionario, podemos añadir nuevos tipos de materiales. Para este ejercicio, agrega por lo menos tres artículos de revista académica, dos artículos de periódico y un video de YouTube a tu diccionario.

Puedes utilizar cualquier método para añadir estos elementos, ya sea a través de una lista o de un diccionario. Intenta que el procedimiento sea lo más automático posible.

Para las revistas académicas deberás incluir los siguientes campos:

- Revista
- Volumen
- Número
- url

Para los artículos de periódico deberás incluir los siguientes campos:

- Periódico
- Sección
- Fecha de publicación
- url

Para los videos de YouTube deberás incluir los siguientes campos:

- Título
- Canal
- Fecha de publicación
- url

Al igual que en el ejercicio 1, imprime la lista con todos los elementos.

## Ejercicio 3: Listar los elementos por tipo

En este ejercicio, deberás crear un programa que te permita mostrar los elementos contenidos en el diccionario de acuerdo a su tipo. Por ejemplo, si el usuario "ingresa" `artículo`, el programa deberá mostrar todos los artículos académicos que se encuentren en el diccionario. El resultado debería verse en pantalla de la siguiente manera:

```shell
        LISTADO DE ARTÍCULOS

        Identificador: 005
        Título: El título del artículo
        Autor: Ramírez Beltrán, Juan
        Revista: Revista de Ciencias Sociales
        Volumen: 1
        Número: 1
        Fecha: 2000
        url: https://www.revistacienciassociales.com/1/1/1
```

## Ejercicio 4: Contar ciudades

Para este ejercicio, deberás crear un programa que te muestre cuántas coincidencias existe en la ciudad de publicación de los libros que se encuentran en el diccionario. Debes iterar sobre el diccionario de tal manera que sea posible contar cuántas veces aparece una ciudad específica. Los resultado deberás guardarlos en un diccionario de esta manera:

```python
resultados {
    "Barcelona" : 3,
    "Madrid" : 2,
    "Buenos Aires" : 1
}
```

Al finalizar, imprime el diccionario de resultados de tal manera que se muestre en pantalla de la siguiente manera:

```shell
        RESULTADOS

        Barcelona: 3
        Madrid: 2
        Buenos Aires: 1
```

## Envío de la actividad

Al igual que las actividades anteriores, envía tu código a través de Github.

Los cinco ejercicios deberán ser realizados en un archivo llamado `actividad6.py`. Guárdalo en el directorio con tu nombre (de preferencia en un subdirectorio).

Para entregar la actividad, debes hacer un `commit` de los modificados y hacer un `push` de tu brazo al repositorio remoto.

```bash
git add .
git commit -m "Entrega de la actividad 6"
git push -u origin nombre-del-brazo
```

### Fecha de entrega

Entrega la actividad antes del martes 7 de marzo.
