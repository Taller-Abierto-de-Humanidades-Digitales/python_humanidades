cuento = "Arrasado el jardín, profanados los cálices y las aras, entraron a caballo los hunos en la biblioteca monástica y rompieron los libros incomprensibles y los vituperaron y los quemaron, acaso temerosos de que las letras encubrieran blasfemias contra su dios, que era una cimitarra de hierro. Jorge Luis Borges, 'Los teólogos'."

## Concatenación

concatenar = "Arrasado "  + "el " + "jardín"
# print(concatenar)

# cada espacio es un caracter.

## Obtener el longitud de una cadena

# print(len(cuento))

## comparar traducciones

trad1 = """
        FORTINBRÁS Cuatro capitanes portarán a Hamlet marcialmente al catafalco, pues, de habérsele brindado, habría sido un gran rey. Su muerte será honrada con sones militares y ritos de guerrero. Llevaos los cadáveres. Esta escena, más propia de batalla, aquí disuena. Vamos, que disparen los soldados
        """

trad2 = """
        FORTIMBRÁS.-  Cuatro de mis capitanes lleven al túmulo el cuerpo de Hamlet con las insignias correspondientes a un guerrero. ¡Ah! Si él hubiese ocupado el trono, sin duda hubiera sido un excelente Monarca... Resuene la música militar por donde pase la pompa fúnebre, y hagánsele todos los honores de la guerra... Quitad, quitad de ahí esos cadáveres. Espectáculo tan sangriento, más es propio de un campo de batalla que de este sitio... Y vosotros, haced que salude con descargas todo el ejército.
        """

diff = len(trad2) - len(trad1)
print(f"La diferencia entre las dos traducciones es de {diff} caracteres.")

## Acceder a una posición en el texto

palabra = "casa"

final = palabra[0] # primer caracter
final2 = palabra[1] # segundo caracter
final3 = palabra[-1] # último caracter
#print(final, final2, final3)

palabra_plur = "perros"

#print(f"La palabra {palabra_plur} es plural porque termina en {palabra_plur[-1]}")

primera_palabra = cuento[0:8]
#print(primera_palabra)
#print(cuento[:8])
#print(cuento[8:])
#print(cuento[-8:])

## Reemplazar una cadena por otra: replace()

frase = "Arrasado el jardin"

frase = frase.replace("jardin", "jardín")
#print(frase)

trad1 = trad1.replace(",", "").replace(".", "")
trad2 = trad2.replace(",", "").replace(".", "")
diff = len(trad2) - len(trad1)
print(f"La diferencia entre las dos traducciones es de {diff} caracteres.")

## método find()

ubicacion = cuento.find("jardín")
print(ubicacion)

encontrar = cuento.find("información")
print(encontrar)

## método count()

print(cuento.count(" "))

# startswith() y endswith()

print(cuento.startswith("Arrasado"))
print(cuento.endswith("arrasado"))


## in

print("jardin" in frase)

print(cuento.startswith("En un lugar de la Mancha"))
print(cuento.endswith("Jorge Luis Borges, 'Los teólogos'."))
print("cimitarra" in cuento)

## upper() y lower()

print(frase.upper())
print(frase.lower())

nombre = "Agustín González Hiriarte"

print(nombre.capitalize())
print(nombre.title())
print(nombre.swapcase())

## strip()

frase2 = " Arrasado el jardín "
print(frase2)
print(frase2.split())

## split()

print(cuento.split())