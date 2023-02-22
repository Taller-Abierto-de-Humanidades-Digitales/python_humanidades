#apuntesclase

#sentencias y condicionales 

#operadores logicomatematicos 
## operaciones de igualdad

perro = "Pepe"
gato = "Pepo"
#print (perro == "Pepe")
print (perro == gato)
# el resultado es true or false 

## operaciones de desigualdad 

#print(perro != gato)

## Operaciones mayor que y menor que 

print(5 < 3)
print(5 > 3)

from random import randint
numero = randint (1,100)
print(numero)
print(numero < 50 )

#para igual 
print(5 <= 5)

for i in range(0, 10):
    print (i >= 5)

## multiples condiciones 
# 
from random import randint
numero = randint(1,100)

print(numero)
print(numero <= 50 and numero >= 25 )

#con and los dos tienen que ser verdaderos 
#con or los dos deben ser falsos 

print(perro == "Pepe" and gato == "Pepe")
print(perro == "Pepe" or gato != "Pepo")

#operadores de pertenencia 

lista_perros = ["Firulais", "Pepe", "Snoopy", "Scooby Doo", "Lukanikos"]
print(perro in lista_perros)
print(perro not in lista_perros)

#operador de pertenencia con cadenas de caracteres
s = "Hola"
print ("a" in s)
print ("b" in s)

#sentencias if, elif y else - tomar decisiones
## if es si , 

if 5 > 3:
    print("5 es mayor que 3")

presidentescol = ["Alvaro", "Juan", "Ivan", "Gustavo"]

respuesta = "Virgilio"

if respuesta in presidentescol: 
    print(f"asi es {respuesta} cierto")
else: 
    print (f"error {respuesta} no fue ")