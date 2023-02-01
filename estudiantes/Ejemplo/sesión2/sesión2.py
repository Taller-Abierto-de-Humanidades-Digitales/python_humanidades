# Sintaxis básica de Python

# Comentario
"""
comentario
en línea
multilinea
"""

print("Hola mundo")

name = "Hola"
if name == "Hola":
    print("Hola mundo")

# Variables

nombre = "valor swe"
numero = 1253
decimal = 1.256
logicos = True
logicos2 = False

nombre1 = "Jairo"
guion = "valor2"

nombre_2 = "Antonio"

Numero = 89
numero = "kilo"

apellido = "Melo"
print(apellido)

# Operaciones con variables

numero = 5
numero = numero + Numero
print(numero)
numero = numero - Numero
print(numero)

nombre = "Juan" # cadena de caracteres string
apellido = "Pérez"

nombre_completo = nombre + apellido
print(nombre_completo)
nombre_completo_comprobacion = "J" + "u" + "a" + "n" + "P" + "é" + "r" + "e" + "z"
print(nombre_completo_comprobacion)
nombre_completo2 = nombre + " " + apellido
print(nombre_completo2)

nombre3 = nombre * 3
print(nombre3)

nacimiento = "1989"
fecha_actual = 2023

# formateo de cadenas

frase = f"{nombre} nació en {nacimiento}, tiene {fecha_actual - int(nacimiento)} años."
print(frase)
