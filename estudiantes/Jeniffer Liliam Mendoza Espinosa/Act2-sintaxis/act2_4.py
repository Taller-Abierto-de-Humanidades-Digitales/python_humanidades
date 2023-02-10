#Ejercicio 4: Operadores con cadenas de texto

frase1 = "El desierto más grande del planeta "
frase2 = "es un mundo de hielo"

print(f"Esta es la frase concatenada: {frase1 + frase2}")

print(f"Esta es la frase repetida 2 veces: {frase1 * 2}")

print(f'La palabra "grande" está en la primera frase: {"grande" in frase1}?')

print(f'¿La palabra "mundo" no está en la primera frase: {"mundo" not in frase1}')

print(f'La primera frase es igual a la segunda: {frase1 == frase2}')

print(f'La primera frase es diferente a la segunda: {frase1 != frase2}')
