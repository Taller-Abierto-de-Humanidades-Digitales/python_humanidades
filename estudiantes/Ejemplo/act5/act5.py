libros = [
    "Después de 1945: la latencia como origen del presente; Hans Ulrich Gumbrecht; 2015; historia conceptual",
    "De papel. En torno a sus dos mil años de historia; Nicholas Basbanes; 2014; historia del libro",
    "No logo. El poder de las marcas; Naomi Klein; 2014; historia del diseño",
    "Teoría de la interpretación; Paul Ricoeur; 2017; filosofía",
    "Más allá del cuerpo. Ensayos en torno a la corporalidad; Francisco González Crussí; 2021; ensayo",
    "Fiction in the Archives. Pardon Tales and Their Tellers in Sixteenth-Century France; Natalie Zemon Davis; 1987; historia"
]

# Ejercicio 1

""" palabra_clave = "Python"
resultado = []

for l in libros:
    if palabra_clave.lower() in l.lower():
        resultado.append(l)

if len(resultado) > 0:
    print(resultado)
else:
    print("NO se obtuvieron resultados") """

## Ejercicio 2
""" 
fecha = 2014
direccion = "ant"

resultado = []

for l in libros:
    if direccion == "ant":
        if int(l.split("; ")[2]) <= fecha:
            resultado.append(l)
    else:
        if int(l.split("; ")[2]) >= fecha:
            resultado.append(l)

if len(resultado) > 0:
    print(resultado)
else:
    print("No hay resultados") """

## Ejercicio 3

""" genero = "historia"

 resultado = []

for l in libros:
    if genero.lower() in l.lower().split("; ")[-1]:
        resultado.append(l) 

resultado = [l for l in libros if genero.lower() in l.lower().split("; ")[-1]]

if len(resultado) > 0:
    print(resultado)
else:
    print("NO hay resultados") """

## Ejercicio 4
""" 
historia = []
filosofia = []
otros = []

for l in libros:
    if "historia" in l.lower().split("; ")[-1]:
        historia.append(l)
    elif "filosofía" in l.lower().split("; ")[-1]:
        filosofia.append(l)
    else:
        otros.append(l)

print("Libros de historia".upper())
for l in historia:
    elementos = l.split("; ")
    print(f"- {elementos[1]}, {elementos[0]} ({elementos[2]}), {elementos[3]}")

print("Libros de filosofía".upper())
for l in filosofia:
    elementos = l.split("; ")
    print(f"- {elementos[1]}, {elementos[0]} ({elementos[2]}), {elementos[3]}")

print("Otros".upper())
for l in otros:
    elementos = l.split("; ")
    print(f"- {elementos[1]}, {elementos[0]} ({elementos[2]}), {elementos[3]}") """

#Ejercicio 5 

autor = "Heidegger"
fecha = 2014

resultado = []
resultado_parcial = []

for l in libros:
    if autor.lower() in l.lower().split("; ")[1] and int(fecha) == int(l.split("; ")[2]):
        resultado.append(l)
    elif autor.lower() in l.lower().split("; ")[1] or int(fecha) == int(l.split("; ")[2]):
        resultado_parcial.append(l)

if len(resultado) > 0:
    print(f"Libros de {autor} publicados en {fecha}")

    for r in resultado:
        elementos = r.split("; ")
        print(f"- {elementos[0]} ({elementos[2]}), {elementos[-1]}")
elif len(resultado_parcial) > 0:
    print(f"Resultado parcial")
    for r in resultado_parcial:
        elementos = r.split("; ")
        print(f"- {elementos[0]} ({elementos[2]}), {elementos[-1]}")
else:
    print("No hay coincidencias")