##lower(): Convierte todas las letras de la frase a minúsculas

oracion1 = "Seguiremos cantando. Un canto a mi tierra, un canto de resistencia"
print(oracion1.lower())

##upper(): Convierte todas las letras de la frase a mayúsculas

oracion1 = "Seguiremos cantando. Un canto a mi tierra, un canto de resistencia"
print(oracion1.upper())

##capitalize(): Convierte la primera letra de la frase a mayúscula

oracion1 = "Seguiremos cantando. Un canto a mi tierra, un canto de resistencia"
print(oracion1.capitalize())

##title(): Convierte la primera letra de cada palabra de la frase a mayúscula

oracion1 = "Seguiremos cantando. Un canto a mi tierra, un canto de resistencia"
print(oracion1.title())

##swapcase(): Convierte todas las letras de la frase a mayúsculas y minúsculas

oracion1 = "    Seguiremos cantando. Un canto a mi tierra, un canto de resistencia   "
print(oracion1.swapcase())

##strip(): Elimina los espacios en blanco al inicio y al final de la frase

oracion1 = "    Seguiremos cantando. Un canto a mi tierra, un canto de resistencia   "
print(oracion1.strip())

##replace(): Reemplaza una palabra por otra en la frase

oracion1 = "Seguiremos cantando. Un canto a mi tierra, un canto de resistencia"
palabra1 = "canto"
print(palabra1)
print(F"Seguiremos cantando. Un {palabra1} a mi tierra, un {palabra1} de resistencia")
palabra2 = "grito"
print(palabra2)

print(oracion1.replace(palabra1, palabra2))


##split(): Divide la frase en palabras

oracion1 = "Seguiremos cantando. Un canto a mi tierra, un canto de resistencia"
print(oracion1.split())