# For Loops

paises = ['Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Perú', 'Surinam', 'Uruguay', 'Venezuela']

""" for variable in paises:
    print(variable)
 """

#secuencia = [1,2,3,4,5,6]

""" for numero in range(10, 0, -1):
    print(numero) """

## Llenar los listados con loops

""" secuencia = []

for numero in range(2, 100, 5):
    secuencia.append(numero)

print(secuencia) """

""" iniciales = []
finales = []
longitud = []

for pais in paises:
    iniciales.append(pais[0])
    finales.append(pais[-1])
    longitud.append(len(pais))

print(iniciales, finales, longitud)
promedio = sum(longitud) / len(paises)
print(f"Los nombres de los paises sudamericanos tienen en promedio {round(promedio, 2)} caracteres.")
 """


## loops anidados

frase = "Era la estación de las lluvias en Bangkok".split()
""" 
for palabra in frase:
    for letra in palabra:
        print(letra, end=' ')
    print() """

""" for numero in range(1, 100):
    print(numero, end=' ')
 """

""" for pais in paises[-3:]:
    print(pais)
 """


paises_capitales = [
    ['Argentina', 'Buenos Aires'],
    ['Bolivia', 'La Paz'],
    ['Brasil', 'Brasilia'],
    ['Chile', 'Santiago de Chile'],
    ['Colombia', 'Bogotá'],
    ['Ecuador', 'Quito'],
    ['Guyana', 'Georgetown'],
    ['Paraguay', 'Asunción'],
    ['Perú', 'Lima'],
    ['Surinam', 'Paramaribo'],
    ['Uruguay', 'Montevideo'],
    ['Venezuela', 'Caracas']
]

""" capitales = []

for pais_capital in paises_capitales:
    capitales.append(pais_capital[1]) """
""" 
## combinar dos listas en una iteración

for pais, capital in zip(paises, capitales):
    print(f"La capital de {pais} es {capital}.")
 """


## Listas de comprensión

capitales = [pais_capital[1] for pais_capital in paises_capitales]

print(capitales)
