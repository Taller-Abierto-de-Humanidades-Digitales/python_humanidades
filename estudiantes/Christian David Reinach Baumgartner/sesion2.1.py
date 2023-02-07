cuento = "Arrasado el jardín, profanados los cálices y las aras, entraron a caballo los hunos en la biblioteca monástica y rompieron los libros incomprensibles y los vituperaron y los quemaron, acaso temerosos de que las letras encubrieran blasfemias contra su dios, que era una cimitarra de hierro. Jorge Luis Borges, 'Los teólogos'."

##Concatenación

concatenar = "Arrasado"  + " " + "el" +" "+"jardín"


trad1 = """
        FORTINBRÁS Cuatro capitanes portarán a Hamlet marcialmente al catafalco, pues, de habérsele brindado, habría sido un gran rey. Su muerte será honrada con sones militares y ritos de guerrero. Llevaos los cadáveres. Esta escena, más propia de batalla, aquí disuena. Vamos, que disparen los soldados
        """

trad2 = """
        FORTIMBRÁS.-  Cuatro de mis capitanes lleven al túmulo el cuerpo de Hamlet con las insignias correspondientes a un guerrero. ¡Ah! Si él hubiese ocupado el trono, sin duda hubiera sido un excelente Monarca... Resuene la música militar por donde pase la pompa fúnebre, y hagánsele todos los honores de la guerra... Quitad, quitad de ahí esos cadáveres. Espectáculo tan sangriento, más es propio de un campo de batalla que de este sitio... Y vosotros, haced que salude con descargas todo el ejército.
        """

diff = len(trad2) - len(trad1)
#print(f"La diferencia de longitud entre las dos traducciones es de {diff} caracteres")

palabra = "casa"
print(cuento[:-8])

