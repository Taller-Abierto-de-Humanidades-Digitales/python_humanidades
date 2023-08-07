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
# Actividad final

Hemos llegado al final de este curso de bases para programar en Python para las humanidades. Después de la actividad intermedia, hemos dedicado un par de semanas a aprender algunos procesos importantes para programar de manera correcta: la lectura, escritura y modificación de archivos; el uso de expresiones regulares; y el uso de clases. Con estas herramientas básicas, programar ya será una realidad y podrás resolver problemas computacionales en tus proyectos de investigación.

En esta actividad final, realizaremos un proyecto con un poco más de complejidad. Tendrás que tomar algunas decisiones por tu cuenta, así que ese será un aspecto muy importante en la creación de tu programa.

Como habrás notado por algunos de los ejercicios propuestos durante las lecciones, la idea de esta actividad será hacer más eficiente, mejor escrito y más legible el código que ya has escrito.

En la actividad intermedia, utilizamos un esquema de datos predeterminado para la elaboración de nuestra interface de usuario. En esta actividad, diseñarás y crearás todo el sistema de gestión de información bibliográfica. Esto incluye tanto la gestión de la información bibliográfica (añadir, editar, eliminar, consultar) como la interface de usuario en la cual realizará las búsquedas.

Los pasos sugeridos para realizar la actividad son los siguientes:

## 1. Creación del sistema de gestión de información bibliográfica

En esta primera parte, tendrás que diseñar el sistema de gestión de información bibliográfica. Esto incluye tanto el diseño de la "base de datos" como el diseño de la interface de usuario.

### 1.1. Diseño de la base de datos

En este caso, podrás tomar como ejemplo la estructura de datos de la actividad intermedia o realizar tu propia estructura de datos, es decir:

- ¿Qué campos deben tener los registros bibliográficos?
- ¿Qué tipo de datos deben tener esos campos?
- ¿Qué campos serán obligatorios y cuáles opcionales?
- ¿Qué campos serán únicos y cuáles no?

Puedes utilizar una estructura tabular (tablas en csv) para almacenar la información o una estructura de diccionarios (json). En ambos casos, tendrás que diseñar la estructura de datos y crear un archivo de ejemplo con algunos registros.

Mi sugerencia es: no diseñes tu base de datos con un modelo tan ambicioso como el utilizado por Zotero para gestionar la información. Piensa en un tipo de colección bibliográfica en particular, por ejemplo, una pequeña biblioteca física, o una colección de objetos digitales. Con base en este criterio, diseña los campos y valores que serán más útiles para la gestión de esa colección.

### 1.2. Diseño de la interface de usuario

En este caso, el usuario será la persona encargada de gestionar la información bibliográfica. Por lo tanto, la interface de usuario debe ser lo más sencilla posible. Debe permitir realizar las siguientes acciones:

- Añadir un nuevo registro bibliográfico.
- Editar un registro bibliográfico existente.
- Eliminar un registro bibliográfico existente.
- Consultar un registro bibliográfico existente.

Para realizar estas acciones, puedes utilizar un menú de opciones o un sistema de comandos. En ambos casos, la interface de usuario debe ser lo más sencilla posible.

Algunas sugerencias de diseño son las siguientes:

- Evitar que el usuario creé accidentalmente un registro duplicado. Para ello, puedes utilizar un campo único (por ejemplo, el título del libro) para verificar si el registro ya existe y preguntar al usuario si desea duplicar el registro o modificar el registro existente.
- Evitar que el usuario elimine o modifique accidentalmente un registro. Para ello, puedes pedirle al usuario que confirme la eliminación o modificación del registro.
- Evitar que el usuario introduzca datos erróneos. Para ello, puedes utilizar expresiones regulares para verificar que los datos introducidos por el usuario sean válidos.
- Evita forzar al usuario a usar un formato específico (por ejemplo, mayúsculas o minúsculas en un campo, o un formato de fecha). Para ello, puedes utilizar expresiones regulares para convertir los datos introducidos por el usuario en el formato deseado.
- En el caso de las fechas, puedes recurrir a la librería `datetime` para verificar que la fecha introducida por el usuario sea válida.

## 2. Creación del sistema de consulta de información bibliográfica

En esta segunda parte, tendrás que crear el sistema de consulta de información bibliográfica. Este sistema debe permitir realizar búsquedas en la base de datos y mostrar los resultados de la búsqueda, además de filtrar y ordenar los resultados de la búsqueda.

### 2.1. Creación del sistema de búsqueda

En este caso, el usuario será la persona encargada de consultar la información bibliográfica. Por lo tanto, la interface de usuario debe ser lo más sencilla posible. Debe permitir realizar las siguientes acciones:

- Buscar un registro bibliográfico por un campo específico (ej: título, autor, año, tema).
- Buscar un registro bibliográfico por varios campos (ej: título y autor, título y año, autor y tema).
- Buscar un registro bibliográfico por todos los campos.

Para realizar estas acciones, puedes utilizar un menú de opciones o un sistema de comandos.

### 2.2. Creación del sistema de visualización de resultados

La interface deberá entregar un listado de resultados de la búsqueda. Este listado debe incluir los campos más importantes del registro bibliográfico (ej: título, autor, año, tema). En caso de que la colección tenga registros digitalizados, también se puede incluir un enlace a la versión digital del registro (puede ser la ubicación local o una URL).

Puedes complejizar tu interface agregando opciones como las siguientes:

- Filtrar los resultados de la búsqueda por un campo específico (ej: autor, año, tema).
- Ordenar los resultados de la búsqueda por un campo específico (ej: título, autor, año, tema).

## Envío de la actividad

A diferencia de las actividades anteriores, este programa estará mejor ubicado en un repositorio propio de Github. Por lo tanto, deberás crear un repositorio en Github y subir tu programa a ese repositorio. El repositorio debe tener un archivo README.md con las instrucciones para ejecutar el programa.

Para que tu programa pueda recibir retroalimentación, envía el enlace de tu repositorio a nuestro foro de discusión a través de la etiqueta [programas](https://github.com/Taller-Abierto-de-Humanidades-Digitales/curso_python_2023B/discussions/new?category=programas&title=mi%20programa).
