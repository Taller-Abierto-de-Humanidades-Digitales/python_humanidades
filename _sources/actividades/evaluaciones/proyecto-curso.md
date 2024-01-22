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

# Proyecto del curso: Creación de un Analizador de Texto Literario

Una de las áreas con mayor tradición en las ciencias de la computación, y una en la que los y las humanistas hemos estado involucrados desde el incio, es el análisis de texto. Grandes modelos de lenguaje que han servido para el desarrollo de herramientas como ChatGPT partieron de la base del análisis básico de textos.

Partamos de una premisa: las computadoras no saben leer. Lo que para nosotros es una palabra como "casa", para la computadora no es otra cosa que la secuencia de cuatro caracteres "c", "a", "s", "a". La palabra es lenguaje en tanto tiene un significante y un significado, hay una representación simbólica asociamos con el objeto "casa", y a su vez tiene un efecto tanto en quien enuncia como en quien recibe. "Por fin he comprado casa" es algo que tiene un efecto, muy diferente a "Te vamos a expulsar de la casa".

En este proyecto, vas a desarrollar un programa que te permita analizar textos literarios de manera automatizada. El programa se dividirá en tres componentes:

1. Módulo de descripción: conteo de palabras, palabras únicas, frases, frecuencias.
2. Módulo de patrones: frecuencia de personas, lugares, fechas.
3. Módulo de sentimientos: evaluación automatizada del tono del texto.

Analizaremos el "Corpus de novelas hispanoamericanas del siglo XIX (conha19)" {cite} `henny-krahmer_corpus_2021`. Este conjunto compila 234 novelas en texto plano, lo cual facilita procesos de pre-procesamiento que no alcanzaremos a abordar en este curso.

Los textos pueden consultarse aquí:

- [Novelas en formato texto](https://github.com/cligs/conha19/tree/main/txt)

Los metadatos pueden consultarse aquí:

- [Metadatos novelas XIX](https://github.com/cligs/conha19/blob/main/metadata_free.csv)

Durante el transcurso del curso, realizaremos algunos ejercicios que nos permitirán preparar y analizar la información.

La evaluación comprenderá los siguientes aspectos:

- **Código Fuente**: Claridad, uso adecuado de variables, estructuras de datos, bucles y funciones.
- **Análisis y Resultados**: Profundidad y relevancia del análisis realizado en el texto elegido.
- **Presentación**: Explicar el proceso, los desafíos enfrentados y los resultados obtenidos.

El formato de presentación será en un cuaderno de Google Colab, en el cual estará contenido el código y la explicación de los diferentes procesos del programa.
