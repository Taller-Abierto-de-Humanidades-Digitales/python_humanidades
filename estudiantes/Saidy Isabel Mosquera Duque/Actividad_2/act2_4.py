# Ejercicio 4: Operadores con cadenas de texto

# Variables 

frase = " He decidido apostar por el amor. El odio es una carga demasiado pesada."



print(f"Esta es la frase concatenada: {frase + ' by Martin Luther King, Jr.'}")

print(f"Esta es la frase con tres repeticiones: {frase *3}")

print(f"Verificando si la frase contiene la palabra apostar: {'apostar' in frase}")

print(f"Verificando si la frase no contiene la palabra soñar: {'soñar' not in frase}")

print(f"Verificando si la frase no contiene la palabra odio: {'odio' not in frase}")

# Variables 
frase = " He decidido apostar por el amor. El odio es una carga demasiado pesada."
frase2 = " he decidiDo apostar por el AMOR. el ODIO es una carga demasiado pesada. 'martin Luther King, Jr.' "

#print(frase == frase2 and frase == "Mundo")
#print(frase == frase or frase == frase2)
#print(not(frase == frase2 and frase == "Mundo"))

print(f"Verificando si las frases son iguales: {frase == frase2}")

print(f"Verificando si las frases son iguales: {frase == frase}")

print(f"Verificando si las frases son diferentes: {frase != frase2}")

print(f"Verificando si las frases son diferentes: {frase != frase}")
