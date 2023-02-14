# Actividad 4: Iteraciones

## Ejercicio 1: Crear un microcatálogo bibliográfico

Para esta actividad, retomaremos la lista que creamos para el [ejercicio 2 de la actividad 3](actividades/3-listas.md#ejercicio-2-crear-un-microcatalogo-bibliografico). Al final del ejercicio han quedado por lo menos tres elementos que tienen la siguiente estructura:

```python
libro = ["Cuentos completos; Jorge Luis Borges; 1995; Ficción"]
```

En este ejercicio, vamos a crear cuatro listados: uno para los títulos, otro para los autores, otro para los años y uno final para los géneros. Para ello deberás utilizar un *for loop* y el método `split()` para separar los elementos de la lista. El resultado final debe ser algo como lo siguiente:

```python
titulos = ["Cuentos completos", "El Aleph", "Ficciones", "El libro de arena", "El jardín de senderos que se bifurcan"]
autores = ["Jorge Luis Borges", "Jorge Luis Borges", "Jorge Luis Borges", "Jorge Luis Borges", "Jorge Luis Borges"]
anios = ["1995", "1949", "1944", "1945", "1941"]
generos = ["Ficción", "Ficción", "Ficción", "Ficción", "Ficción"]
```

## Ejercicio 2: Enriquecer el microcatálogo bibliográfico

En este ejercicio, vas a añadir al menos tres nuevos libros al microcatálogo bibliográfico que creaste en el ejercicio anterior. Para ello, debes crear una nueva lista denominada `nuevos_libros` en la cual incluyas los nuevos elementos. A continuación, debes utilizar el método `extend()` para añadir los nuevos elementos a la lista `libros`. 

## Ejercicio 3: Eliminar la categoría "género" del microcatálogo bibliográfico

En este ejercicio, vas a eliminar la categoría "género" del microcatálogo bibliográfico que creaste en el ejercicio anterior. Para ello, debes utilizar el método `pop()` para eliminar el último elemento de cada uno de los elementos de la lista `libros`. Al finalizar, el listado de libros debe tener los mismos elementos del ejercicio anterior, pero sin la categoría "género".

## Ejercicio 4: Calcula la fecha promedio de los libros de tu catálogo

En este ejercicio, vas a calcular la fecha promedio de los libros de tu catálogo. Para ello, debes crear una lista denominada `anios` en la cual incluyas los años de publicación de cada uno de los libros de tu catálogo. A continuación, debes utilizar un *for loop* para sumar todos los elementos de la lista `anios`. Finalmente, debes dividir el resultado de la suma entre la longitud de la lista `anios` para obtener la fecha promedio de los libros de tu catálogo.

Muestra tu resultado mediante un mensaje formateado de la siguiente manera:

```python
print(f"La fecha promedio de los libros de mi catálogo es: {fecha_promedio}")
```

## Ejercicio 5: Calcula el promedio de caracteres de los títulos de tu catálogo

En este ejercicio, vas a calcular el promedio de caracteres de los títulos de tu catálogo. Para ello, debes crear una lista denominada `titulos` en la cual incluyas los títulos de cada uno de los libros de tu catálogo. A continuación, crea una lista de comprensión en la variable `longitud` que contenga la longitud de cada uno de los títulos de la lista (aprovecha la función `len()`). Encuentra el promedio sumando los valores de la lista `longitud` y dividiendo el resultado entre la longitud de la lista `titulos`. Muestra tu resultado mediante un mensaje formateado de la siguiente manera:

```python
print(f"El promedio de caracteres de los títulos de mi catálogo es: {promedio}")
```
