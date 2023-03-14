####### Ejercicio 1: 

Catalogo = ["Libro; Sarah Jackson; #HashtagActivism: Networks of Race and Gender Justice; The MIT Press; 2020; Massachusetts; https://direct.mit.edu/books/book/4597/HashtagActivismNetworks-of-Race-and-Gender-Justice", "Libro Capítulo; Roopika Risam; Decolonizing the Digital Humanities in Theory and Practice; Routledge; 2018; New York; https://www.taylorfrancis.com/books/9781317549093/chapters/10.4324/9781315730479-8", "Libro Capítulo; Kim Gallon; Making a Case for the Black Digital Humanities; University of Minnesota Press; 2016; Minnesota; https://www.jstor.org/stable/10.5749/j.ctt1cn6thb.7", "Libro; Patricia_Hill Collins; Black feminist thought: knowledge, consciousness, and the politics of empowerment; Routledge; 2000; New York", "Libro Capítulo; Safiya_Umoja Noble; Toward a Critical Black Digital Humanities; University of Minnesota Press; 2019; Minnesota; "]

# de esta manera se estructural los diccionarios 

bibliografia = {"000" : {
    "tipo" : "",
    "autor" : [{"nombre" : "", "apellido" : ""}],
    "titulo" : "",
    "editorial" : "",
    "fecha" : 0,
    "lugar" : "",
    "url" : ""
    },
}


# Para automatizar las claves de los diccionarios 
for c in Catalogo:
    clave = int(list(bibliografia.keys())[-1]) + 1
    
    clave = str(clave).zfill(3)

 # se fracmenta la categoria de autor para poder llamar el nombre y el apellido por separada y crear un diccionario interno   

    if len(c.split("; ")[0].split(" ")) > 2:
        nombre = c.split("; ")[1].split(" ")[:2]
    else:
        nombre = c.split("; ")[1].split(" ")[1]


# se trasforma la lista en un diccionario 
    bibliografia[clave] = {
        "tipo": c.split("; ")[0],
        "autor": [{"nombre": c.split("; ")[1].split(" ")[0], "apellido": c.split("; ")[1].split(" ")[1]}],
        "titulo": c.split("; ")[2],
        "editorial": c.split("; ")[3],
        "fecha": int(c.split("; ")[4]),
        "lugar": c.split("; ")[5],
        "url": c.split("; ")[-1],
    }


 # este funcion? permite borra  


del bibliografia['000']



###### Ejercicio 2:  

# Agregar Articulos y Videos 


lista_revistas = [
    "Artículos academicos; Kattya Hernández; Cuerpos insurgentes: territorios de re-existencia de las y los afrodescendientes; La manzana de la discordia; 2019; Colombia; 14; 1; https://dialnet.unirioja.es/servlet/articulo?codigo=7446265", "Artículos academicos; Ochy Curiel; El régimen heterosexual y la nación. Aportes del lesbianismo feminista a la antropología; La Manzana de la Discordia; 2012; Colombia; 6; 1; https://bibliotecadigital.univalle.edu.co/handle/10893/3501", "Artículos academicos; Rachel Kuo; Racial justice activist hashtags: Counterpublics and discourse circulation; New Media & Society; 2018; New York; 20; 2; https://journals.sagepub.com/doi/10.1177/1461444816663485"
]


lista_videos = [
    "What is Afrofuturism?; Black Enterprise; 2018; https://www.youtube.com/watch?v=AgXujySEuIE", "Kishonna L. Gray: Examining Black Feminism in the Digital Era; The Berkman Klein Center for Internet & Society; 2017; https://www.youtube.com/watch?v=7fYeL3WH4Xk", "Sarah Baartman: The Tragic Exploitation of an African Woman; HistoryVille; 2022; https://www.youtube.com/watch?v=-CSeXTbr2ng"
]


####### PROGRAMA

for c in lista_revistas:
    clave = int(list(bibliografia.keys())[-1]) + 1
    clave = str(clave).zfill(3)
    bibliografia[clave] = {
        "tipo": c.split("; ")[0],
        "autor": [{"nombre": c.split("; ")[1].split(" ")[0], "apellido": c.split("; ")[1].split(" ")[1]}],
        "titulo": c.split("; ")[2],
    }

bibliografia[clave]['revista'] = 'hola'


print(f"""
        Identificador: {clave}
        Revista: {valor['autor']}
        """)