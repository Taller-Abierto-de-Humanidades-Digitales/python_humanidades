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

# Sentencias `if`, `elif` y `else`

Con las pruebas condicionales obtenemos un valor booleano de verdad o falsedad. Para que nuestro programa tome una decisión, debemos utilizar la sentencia (*statement*) `if`. En términos simples, la setnencia `if` valida si un valor es verdadero y realiza una acción. Un ejemplo es el siguiente:

```{code-cell} ipython3
if 5 > 3:
    print("5 es mayor que 3")
```

Podemos leerlo de la siguiente forma:

> **Si** 5 **es** mayor que 3, **entonces** imprime "5 es mayor que 3".

Es decir, siempre estamos usando este esquema: Si algo es verdad, entonces haz algo.

```{admonition} La verdad
:class: tip
Ten en cuenta que hablamos aquí de una verdad lógica, no de una verdad experimental o testimonial. Por ejemplo:

> presidenteColombia = "Benito Juárez"

> if presidenteColombia == "Benito Juárez":

> print(f"¡Es verdad! El presidente actual de Colombia es {presidenteColombia}")

>       "¡Es verdad! El presidente actual de Colombia es Benito Juárez"

En este caso, la verdad es que el presidente de Colombia actual es Benito Juárez, porque así se estableció en el dato. La verdad es lógica (p es igual a q), no experimental (p es igual a q porque lo observé) o producto de la evidencia (p es igual a q porque lo puedo demostrar).
```

Teniendo en cuenta lo anterior, podemos validar un valor y establecer una acción a partir de allí. Por ejemplo, podemos validar si "Benito Juárez" fue uno de los presidentes de Colombia del siglo XXI:

```{code-cell} ipython3

presidentesColXXI = ["Álvaro Uribe", "Juan Manuel Santos", "Iván Duque", "Gustavo Petro"]

# ¿Fue Benito Juárez presidente de Colombia en el siglo XXI?

if "Benito Juárez" in presidentesColXXI:
    print("¡Es verdad! Benito Juárez fue presidente de Colombia en el siglo XXI")
```

Observa que el valor de verdad no se cumple y que utilizamos un operador de pertenencia para validar si el valor de la variable `presidenteColombia` se encuentra dentro de la lista `presidentesColXXI`. En este caso, el valor de verdad es falso, por lo que no se ejecuta la acción. Podemos hacer que en lugar de validar la pertenencia, validemos la no pertenencia:

```{code-cell} ipython3
if "Benito Juárez" not in presidentesColXXI:
    print("¡Es verdad! Benito Juárez no fue presidente de Colombia en el siglo XXI")
```

También podemos establecer en una sola operación si el valor pertenece o no pertenece y en cada caso realizar una acción, para ello nos valdremos de la sentencia `else`.

## Sentencia `else`

La sentencia `else` permite que ejecutemos una acción en caso de que la condición de verdad no se cumpla. Por ejemplo:

```{code-cell} ipython3

# ¿Fue Benito Juárez presidente de Colombia en el siglo XXI?

if "Benito Juárez" in presidentesColXXI:
    print("¡Es verdad! Benito Juárez fue presidente de Colombia en el siglo XXI")
else:
    print("No es cierto. Benito Juárez no fue presidente de Colombia en el siglo XXI")
```

Nuevamente, podemos leer esta sentencia de la siguiente manera:

> **Si** "Benito Juárez" **está** en la lista `presidentesColXXI`, **entonces** imprime "¡Es verdad! Benito Juárez fue presidente de Colombia en el siglo XXI". **De lo contrario**, imprime "No es cierto. Benito Juárez no fue presidente de Colombia en el siglo XXI".

## Sentencia `elif`

Ahora, no siempre encontramos una sola condición de verdad que queremos cumplir, en ciertas ocasiones podremos intentar validad si una condición se cumple y si no se cumple, intentar validar otra condición. Para ello, utilizamos la sentencia `elif` (*else if*). Por ejemplo, podemos validar si "Benito Juárez" fue presidente de Colombia en el siglo XXI o si "Juan Manuel Santos" fue presidente de Colombia en el siglo XXI:

```{code-cell} ipython3

# ¿Fue Benito Juárez o Juan Manuel Santos presidente de Colombia en el siglo XXI?

if "Benito Juárez" in presidentesColXXI:
    print("¡Es verdad! Benito Juárez fue presidente de Colombia en el siglo XXI")
elif "Juan Manuel Santos" in presidentesColXXI:
    print("¡Es verdad! Juan Manuel Santos fue presidente de Colombia en el siglo XXI")
else:
    print("No es cierto. Ni Benito Juárez ni Juan Manuel Santos fueron presidentes de Colombia en el siglo XXI")
```

```{admonition} Nota
:class: tip

Técnicamente, podemos utilizar la sentencia `elif` tantas veces como queramos, pero es recomendable no abusar de esta. En primer lugar, el código puede hacerse muy complejo para leer y de depurar, pues la cantidad de decisiones que se toman en un solo bloque de codigo pueden ser demasiadas. En general, si es necesario tomar muchas decisiones es mejor utilizar una estructura de datos que permita evitar esto, como un diccionario o una lista de diccionarios (los veremos en la siguiente sección).
```

## Algunos consejos para hacer más eficiente el código

La sentencia `if` es muy útil para validar condiciones y tomar decisiones. Nuestras computadoras hacen que hoy en día no sea un problema tan grande, sin embargo, al sumar cada uno de los pasos que hacemos es factible que el programa se ejecute en mucho mayor tiempo del necesario. Antes de que nos enfrentemos a una situación en la que el programa se demore demasiado, es importante tener en cuenta algunos consejos para hacer más eficiente el código.

1. **Ordenar las condiciones en función de su probabilidad de ocurrencia**: En caso de que sepamos que una condición es más probable que se cumpla que otra, es conveniente colocarla al principio de la sentencia `if`. Esto se debe a que Python realiza la evaluación en orden secuencial. De esta manera, si la primera condición se cumple, no evaluará las demás. Por ejemplo, en el siguiente programa queremos convertir el listado de países a sus códigos ISO3. En este caso, sabemos que el país que más aparece es México. Por lo tanto, podemos colocar la condición de México al principio:

```{code-cell} ipython3

paises_de_origen = ["Colombia", "México", "Argentina", "México", "México", "España", "México", "Perú", "Chile", "Estados Unidos", "Colombia", "México", "México", "España", "México", "Perú", "Chile", "Estados Unidos", "Colombia", "México", "México", "España", "México", "Perú", "Chile", "Estados Unidos", "Colombia", "México", "México", "España", "México", "Perú", "Chile", "Estados Unidos", "Colombia", "México", "México", "España", "México", "Perú", "Chile", "Estados Unidos", "Colombia", "México", "México", "España", "México", "Perú", "Chile", "Estados Unidos", "Colombia", "México", "México", "España", "México", "Perú", "Chile", "Estados Unidos", "Colombia", "México", "México", "España", "México", "Perú", "Chile", "Estados Unidos", "Colombia", "México", "México", "España", "México", "Perú", "Chile", "Estados Unidos", "Colombia", "México", "México", "España", "México", "Perú", "Chile", "Estados Unidos", "Colombia", "México", "México", "España", "México", "Perú", "Chile", "Estados Unidos", "Colombia", "México", "México", "España", "México", "Perú"]

codigos_iso3 = []

for pais in paises_de_origen:
    if pais == "México":
        codigos_iso3.append("MEX")
    elif pais == "Colombia":
        codigos_iso3.append("COL")
    elif pais == "Argentina":
        codigos_iso3.append("ARG")
    elif pais == "España":
        codigos_iso3.append("ESP")
    elif pais == "Perú":
        codigos_iso3.append("PER")
    elif pais == "Chile":
        codigos_iso3.append("CHL")
    elif pais == "Estados Unidos":
        codigos_iso3.append("USA")
    else:
        codigos_iso3.append("OTRO")

print(codigos_iso3)
```

En este listado la diferencia de ejecución entre el código con la condición de México al principio y el código con la condición de México al final es muy pequeña. Pero si esta lista tuviera 1000 elementos o más, o la operación fuese más compleja, la diferencia empezaría a ser más significativa.

2. **Aprovechar los operadores lógicos**: En caso de que tengamos que validar varias condiciones, podemos aprovechar los operadores lógicos para hacer más eficiente el código garantizando que solamente si la primera condición es verdadera se evalúe la segunda. Por ejemplo:

```{code-cell} ipython3

# ¿Fueron Benito Juárez y Juan Manuel Santos presidentes de Colombia en el siglo XXI?

if "Benito Juárez" in presidentesColXXI and "Juan Manuel Santos" in presidentesColXXI:
    print("¡Es verdad! Benito Juárez y Juan Manuel Santos fueron presidentes de Colombia en el siglo XXI")
```

En este caso, el programa no evaluará la segunda condición (`"Juan Manuel Santos" in presidentesColXXI`) porque ya sabemos que la primera condición (`"Benito Juárez" in presidentesColXXI`) es falsa. De esta manera, el programa no evalúa la segunda condición y se ahorra tiempo de ejecución.

Existen otras estrategias para hacer más eficiente el código, pero estas dos son muy valiosas y pueden ser de utilidad cuando trabajamos con proyectos en los cuales la cantidad de datos y la velocidad de ejecución son importantes.
