#Ejercicio 3: Manipulación de cadenas de texto
frase = "El desierto más grande del planeta es un mundo de hielo."
frase1 = "   El desierto más grande del planeta es un mundo de hielo.   "

print(f"Esta es la frase en minúsculas: {frase.lower()}")

print(f"Esta es la frase en mayússculas: {frase.upper()}")

print(f"Esta es la frase con la primera letra en mayúscula: {frase.capitalize()}")

print(f"Esta es la frase con la primera letra de cada palabra en mayúscula: {frase.title()}")

print(f"Esta es la frase con la mayúscula convertida en minúscula y visceversa: {frase.swapcase()}")

print(f"Esta es la frase con espacios al inicio y al final: {frase1}")

print(f"Esta es la frase con eliminación de espacios del inicio y final: {frase1.strip()}")

frase = frase.replace("del planeta", "de la tierra")
print(f"Esta es la frase con reemplazo de palabras: {frase}")

print(f"Esta es la frase dividida en palabras: {frase.split()}")