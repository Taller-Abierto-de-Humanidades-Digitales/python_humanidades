"""
- `+`: Concatena dos cadenas de texto
- `*`: Repite una cadena de texto un número de veces
- `in`: Verifica si una cadena de texto está contenida en otra
- `not in`: Verifica si una cadena de texto no está contenida en otra
- `==`: Verifica si dos cadenas de texto son iguales
- `!=`: Verifica si dos cadenas de texto son diferentes
"""

frase = "esta es una frase nada original"
frase2 = "esta sí es una frase original"

print(f"Esta es la frase concatenada: {frase + 'Pero'+ frase2}")
print(f"Esta es la frase repetida: {frase * 3}")
print(f"Esta es la frase in: {'sí'in frase2}")


print(f"Esta es la frase not in: {'no' not in frase2}")
print(f"Esta es la frase igual: {frase == frase2}")
print(f"Esta es la frase diferente: {frase != frase2}")


