# lower(): Convierte todas las letras de la frase a minúsculas
# upper(): Convierte todas las letras de la frase a mayúsculas
# capitalize(): Convierte la primera letra de la frase a mayúscula
# title(): Convierte la primera letra de cada palabra de la frase a mayúscula
# swapcase(): Convierte todas las letras de la frase a mayúsculas y minúsculas
# strip(): Elimina los espacios en blanco al inicio y al final de la frase
# replace(): Reemplaza una palabra por otra en la frase
# split(): Divide la frase en palabras


frase = """ Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía 
había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo.  """

print(f"\nEsta es la frase en minúsculas: {frase.lower()}")
print(f"\nEsta es la frase en mayúsculas: {frase.upper()}")
print(f"\nEsta es la frase con la primera letra en mayúsculas: {frase.strip().capitalize()}")
print(f"\nEsta es la frase con la primera letra de cada palabra en mayúscula: {frase.title()}")
print(f"\nEsta es la frase con las mayúsculas y las minúsculas invertidas: {frase.swapcase()}")
print(f"\nEsta es la frase sin espacios al principio y al final: {frase.strip()}")
print(f"\nEsta es la frase con las palabras separadas por comas: {frase.split()}")

# Tuve que hacer una trampa acá porque no me dejaba hacer el remplazo de esta forma:
# print(f"Esta es la frase si todas las 'a' fueron arrobas: {frase.replace("a" , "@")}")
# entonces modifique la variable de forma independiente y me funcionó

frase = frase.replace("a" , "@")
print(f"\nEsta es la frase si todas las 'a' fueron arrobas: {frase}")
