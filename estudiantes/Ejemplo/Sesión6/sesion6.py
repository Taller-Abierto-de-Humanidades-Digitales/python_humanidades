protagonistas = {
    "Jerry": {"nombre": "Jerry Seinfeld",
              "año_nacimiento": 1954,
              "nacionalidad": "Estadounidense",
              "género": "Masculino"},
    "George": {
        "nombre": "Jason Alexander",
        "año_nacimiento": 1959,
        "nacionalidad": "Estadounidense",
        "género": "Masculino"
    },
    "Elaine": {
        "nombre": "Julia Louis-Dreyfus",
        "año_nacimiento": 1961,
        "nacionalidad": "Estadounidense",
        "género": "Femenino"
    },
    "Kramer": {
        "nombre": "Michael Richards",
        "año_nacimiento": 1949,
        "nacionalidad": "Estadounidense",
        "género": "Masculino"
    }
}

""" if protagonistas:
    actor = protagonistas['Elaine']
    print(actor)
    actriz = actor['nombre']
    print(actriz)
else:
    print("No hay elementos en el diccionario") """
""" 

protagonistas["George"]["empleos"] = ["Rick Bahr Properties", "Sanalac", "Pendant Publishing", "New York Yankees", "Play Now", "Kruger Industrial Smoothing"]
for l in protagonistas['George']['empleos']:
    print(l.upper())


protagonistas["George"]["prometida"] = {
    "nombre": "Susan",
    "año_nacimiento": 1960,
    "nacionalidad": "Estadounidense",
    "género": "femenino"
}

print(protagonistas["George"]['prometida']['nombre'])

del protagonistas['George']['empleos']
del protagonistas['George']['prometida']
print(protagonistas["George"]) """

protagonistas["Elaine"]["nombre"] = "Julia Scarlett Elizabeth Louis-Dreyfus"
print(protagonistas["Elaine"])