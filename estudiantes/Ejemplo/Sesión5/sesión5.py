# Operadores lógicos

## Operaciones de igualdad

perro = "Firulais"
gato = "Gardfield"
#print(perro.lower() == "firulais")

## Operaciones de desigualdad

#print(perro != gato)

## operaciones mayor que y menor que

""" print(5 > 3)
print(5 < 3)

from random import randint

numero = randint(1, 100)
print(numero)
print(numero < 50) """

""" print(5 <= 5)
print(5 <= 6) """


""" for i in range(0, 10):
    print(i, i >= 5) """

## múltiples condiciones
""" 
from random import randint

numero = randint(1, 100)

print(numero)
print(numero <= 25 or numero >= 75)

perro = "Firulais"
gato = "Gardfield"

print(perro == "Firulais" and gato == "Gardfield" and perro != "Firulais") """

## Operadores de pertenencia

""" perro = "Firulais"

lista_perros = ["Firulais", "Snoopy", "Scooby Doo", "Lukanikos"]

print(perro not in lista_perros) """

## operador de pertenencia con cadenas de caracteres

""" s = "Hola mi nombre es Jairo"

print("Jairo" not in s) """

# Sentencias if, elif y else

""" if 5 < 3:
    print("5 es mayor que 3") """

presidentesColXXI = ["Álvaro Uribe", "Juan Manuel Santos", "Iván Duque", "Gustavo Petro"]
presidentesCol8090 = ["Virgilio Barco", "César Gaviria", "Ernesto Samper", "Andrés Pastrana"]
# Nombra un presidente de Colombia del siglo XXI

respuesta = "Lleras Restrepo"

if respuesta in presidentesColXXI:
    print(f"¡Así es! {respuesta} fue o es presidente de Colombia en el S. XXI")
elif respuesta in presidentesCol8090:
    print(f"{respuesta} fue un presidente entre 1980 y 2002")
else:
    print(f"ERROR: {respuesta} no fue presidente de Colombia en el S. XXI")


## listados e if

novelas_siglo_XIX = ["María", "Sacrificio y recompensa", "Gil Gómez, el insurgente", "Martín Garatuza : memorias de la Inquisición", "Tres episodios mexicanos", "Vida de Juan Facundo Quiroga"]

# separar subtítulos

""" for novela in novelas_siglo_XIX:
    if " : " in novela:
        titulo, subtitulo = novela.split(" : ")
        novelas_siglo_XIX[novelas_siglo_XIX.index(novela)] = titulo

print(novelas_siglo_XIX) """

subtitulo = [novela.split(" : ")[0] for novela in novelas_siglo_XIX if ":" in novela]
print(subtitulo)
