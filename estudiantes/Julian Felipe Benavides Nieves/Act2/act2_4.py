# +: Concatena dos cadenas de texto
# *: Repite una cadena de texto un número de veces
# in: Verifica si una cadena de texto está contenida en otra
# not in: Verifica si una cadena de texto no está contenida en otra
# ==: Verifica si dos cadenas de texto son iguales
# !=: Verifica si dos cadenas de texto son diferentes

frase = "Bogotá esta muy soleada "
frase2 =  "pero hace mucho frío"
palabraen = "Bogotá" in frase
palabrano = "Cúcuta" not in frase
igualdad = frase == frase2
desigualdad = frase != frase2

print(f"Esta es la frase concatenada: {frase + frase2}")
print(f"Esta es la frase repetida 3 veces: {frase * 3}")
print(f"La palabra Bogotá esta en la frase: {palabraen}") 
print(f"La palabra Cúcuta no esta en la frase: {palabrano}")
print(f"Las frases son iguales: {igualdad}")
print(f"Las frases no son iguales: {desigualdad}")