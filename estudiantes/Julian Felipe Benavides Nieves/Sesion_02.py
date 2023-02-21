cuento = "Arrasado el jardín, profanados los cálices y las aras, entraron a caballo los hunos en la biblioteca monástica y rompieron los libros incomprensibles y los vituperaron y los quemaron, acaso temerosos de que las letras encubrieran blasfemias contra su dios, que era una cimitarra de hierro. Jorge Luis Borges, 'Los teólogos'."

# ## Concatenación

# concatenar = "Arrasado" + " "  + "el" + " " + "jardín"
# print(concatenar)

# # cada espacio es un caracter

# ## Obteneter la longitud de una cadena de texto

# print(len(cuento))

# ## comparar traducciones

# trad1 = """
#         FORTINBRÁS Cuatro capitanes portarán a Hamlet marcialmente al catafalco, pues, de habérsele brindado, habría sido un gran rey. Su muerte será honrada con sones militares y ritos de guerrero. Llevaos los cadáveres. Esta escena, más propia de batalla, aquí disuena. Vamos, que disparen los soldados
#         """
# trad2 = """
#         FORTIMBRÁS.-  Cuatro de mis capitanes lleven al túmulo el cuerpo de Hamlet con las insignias correspondientes a un guerrero. ¡Ah! Si él hubiese ocupado el trono, sin duda hubiera sido un excelente Monarca... Resuene la música militar por donde pase la pompa fúnebre, y hagánsele todos los honores de la guerra... Quitad, quitad de ahí esos cadáveres. Espectáculo tan sangriento, más es propio de un campo de batalla que de este sitio... Y vosotros, haced que salude con descargas todo el ejército.
#         """

# diff = len(trad2) - len(trad1)
# print(f"La diferencia de caracteres de las traducciones es de {diff} caracteres.")

## Acceder a una posición en el texto

# palabra = "casa"

# final1 = palabra[0]
# final2 = palabra[1]
# final3 = palabra[2]
# final4 = palabra[-1]
# print(final1+final2+final3+final4+final3)

# casaplural = final1+final2+final3+final4+final3
# print(f"La palabra {casaplural} es plural porque termina en {casaplural[-1]}")

# Escoger varios caracteres seguidos

# print(cuento[0:8])
# print(cuento[8:])
# print(cuento[-8:])

## Reemplazar una cadena por otra

frase = "Arrasando el jardin"

# print(frase)

# frase = frase.replace("jardin","jardín" )

# print(frase)

# print(len(trad1))
# trad1 = trad1.replace(",","").replace(".","")
# print(len(trad1))

## Metodo find()

# ubicación = cuento.find("jardín")
# print(ubicación)

# # cuendo no esta la cadena en la variable

# encontra = cuento.find("burro")
# print(encontra)

## Contar cuentas veces esta una cadena en la variable

# print(cuento.count("os"))

## Inicia con o finaliza con

# starwith() endswith() 
# entraga una booleana (true ,false)

# print(cuento.startswith("Arrasado"))
# print(cuento.startswith("Pepe"))
# print(cuento.endswith("'Los teólogos'."))
# print(cuento.endswith("'Burro"))

## Esta en

# print("jardín" in cuento)
# print("misfits" in cuento)

## Upper y lower

# Todo en mayusculas o minúsculas y viceversa

# print(frase.upper())
# print(frase.lower())
# print(frase.swapcase())

## Primera letra de la cadena

# nombre = "juliAn beNavides"

# print(nombre.capitalize())

## Primera letra de cada palabra

# print(nombre.title())

## Quitar espacios inciales y finales - strip()

# frase2 = " pepe perez   "
# print(frase2)
# print(frase2.strip())

## Separar los conjuntos de caracteres que estan separados por espacios

print(frase.split())
print(frase.split(" "))
print(frase.split(","))

