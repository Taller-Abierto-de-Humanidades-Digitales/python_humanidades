# Operaciones lógicos

## Operaciones de igualdad

""" perro = "Lunis"
gato = "Lunis"
print(perro == gato)

perro = "Lunis"
gato = "Michi"
print(perro == gato)

perro = "Lunis"
gato = "Michi" """
#print(perro.lower() == "lunis")

## Operaciones de desigualdad

#print(perro != "gato")

## Operaciones mayor que - menor que

"""print(5 > 3)
print(5 < 3)"""

"""from random import randint

numero = randint(1, 100) --> aleatorio entre 1  - 100
print(numero)
print(numero < 50)"""

"""print(5 <= 5)
print(5 <= 5)"""

""" for i in range(0, 10):
    print(i, i >= 5) """

## Múltiples condiciones

""" from random import randint

numero = randint(1, 100)

print(numero)
print(numero <= 50 and numero >= 25) """

""" from random import randint

numero = randint(1, 100)

print(numero)
print(numero <= 50 or numero >= 25) --> Siempre será verdadero con "or" """ 

""" perro = "Firulais"
gato = "Gardfield"

print(perro != "Firulais" or gato == "Gardfield")
print(perro != "Firulais" or gato != "Gardfield" and perro == "Firularis") """

## Operadores de pertenencia

""" perro = "Lunetas"

lista_perros = ["Lunetas", "Firulais", "Snoopy", "Scooby Doo", "Lukanikos"]

print(perro in lista_perros) --> Pertenece Luetas a esta lista
print(perro not in lista_perros) --> No petenece Lunetas a esta lista """

## Operador de pertenencia con cadenas de caracteres

""" s = "Hola mi nombre es Conni"

print("Conni" not in s) """

## Sentencias if, elif y else --> Tomar decisiones

if 5 < 3:
    print("5 es mayor que 3")

presidentesColXXI = ["Álvaro Uribe", "Juan Mnauel Santos", "Iván Duque", "Gustavo Petro"]

# Nombre un presidente de Colombia del siglo XXI

respuesta = "Virgilio Barco"

if respuesta in presidentesColXXI:
    print(f"¡Así es! {respuesta}")
elif
else:
    print(f"ERORR {respuesta}")
