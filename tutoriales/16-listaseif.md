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

# Combinar listas y sentencias `if`

Para finalizar esta sección, veamos cómo podemos combinar listas y sentencias `if`. En general, lo que se busca es que a través de una condición, se pueda evaluar el contenido de un listado y realizar una operación con estos valores.

Veamos un ejemplo:

```{code-cell} ipython3
novelas_siglo_XIX = ["María", "Sacrificio y recompensa", "Gil Gómez, el insurgente", "Martín Garatuza : memorias de la Inquisición", "Tres episodios mexicanos", "Vida de Juan Facundo Quiroga"]

# separar subtítulos

for novela in novelas_siglo_XIX:
    if ":" in novela:
        titulo, subtitulo = novela.split(":")
        # reemplazar el título original por el nuevo
        novelas_siglo_XIX[novelas_siglo_XIX.index(novela)] = titulo

print(novelas_siglo_XIX)
```

Aquí hemos construido un pequeño programa que toma una lista de novelas del siglo XIX y separa el subtítulo de la novela a partir de un patrón que consiste en los dos puntos `:`. En este caso, el programa permite descartar en cada iteración si se cumple con la condición de que el valor del nombre de la novela contenga un subtítulo. Solamente cuando se cumple, se realiza la operación, en todo otro caso, se omite.

## Sentencias `ìf` en listas de comprensión

También es posible utilizar sentencias `if` en listas de comprensión. Veamos un ejemplo:

```{code-cell} ipython3

novelas_siglo_XIX = ["María", "Sacrificio y recompensa", "Gil Gómez, el insurgente", "Martín Garatuza : memorias de la Inquisición", "Tres episodios mexicanos", "Vida de Juan Facundo Quiroga"]

# separar subtítulos

subtitulos = [novela.split(" : ")[1] for novela in novelas_siglo_XIX if ":" in novela]

print(subtitulos)
```

Debes tener en cuenta que en esta sintaxis no es posible utilizar las sentencias `else` o `elif`, por lo que solamente deberás utilizarla para validar una condición de verdad.
