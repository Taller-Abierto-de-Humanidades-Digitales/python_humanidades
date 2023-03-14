
Catalogo = ["Libro; Sarah Jackson; #HashtagActivism: Networks of Race and Gender Justice; The MIT Press; 2020; Massachusetts; https://direct.mit.edu/books/book/4597/HashtagActivismNetworks-of-Race-and-Gender-Justice", "Libro Capítulo; Roopika Risam; Decolonizing the Digital Humanities in Theory and Practice; Routledge; 2018; New York; https://www.taylorfrancis.com/books/9781317549093/chapters/10.4324/9781315730479-8", "Libro Capítulo; Kim Gallon; Making a Case for the Black Digital Humanities; University of Minnesota Press; 2016; Minnesota; https://www.jstor.org/stable/10.5749/j.ctt1cn6thb.7", "Libro; Patricia_Hill Collins; Black feminist thought: knowledge, consciousness, and the politics of empowerment; Routledge; 2000; New York", "Libro Capítulo; Safiya_Umoja Noble; Toward a Critical Black Digital Humanities; University of Minnesota Press; 2019; Minnesota; "]


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


for c in Catalogo:
    clave = int(list(bibliografia.keys())[-1]) + 1
    
    clave = str(clave).zfill(3)



    if len(c.split("; ")[0].split(" ")) > 2:
        nombre = c.split("; ")[1].split(" ")[:2]
    else:
        nombre = c.split("; ")[1].split(" ")[1]


    bibliografia[clave] = {
        "tipo": c.split("; ")[0],
        "autor": [{"nombre": c.split("; ")[1].split(" ")[0], "apellido": c.split("; ")[1].split(" ")[1]}],
        "titulo": c.split("; ")[2],
        "editorial": c.split("; ")[3],
        "fecha": int(c.split("; ")[4]),
        "lugar": c.split("; ")[5],
        "url": c.split("; ")[-1],
    }


# funciona pero me inprimer 6 veces el mismo titulos/ la pregunta del millon es porque

"""for titulo in bibliografia:
    if len(c.split("; ")):
        titulo = c.split("; ")[2]
        print(titulo)
        """

# Esto me muestra solo los titulos 
del bibliografia['000']



"""

# Aqui el programa funciona a lo rudimentario pero funciona :)

resultado = []

palabra = input("Escribe una palabra clave del título que estas buscando: ")

for clave, valor in bibliografia.items():
           titulo = {valor["titulo"]}
           if  palabra.lower() in str(titulo).lower():
                resultado.append(titulo)
                print(f"se encontraron {len(resultado)}  los cuales son: {resultado}")
                
                """

resultado = []

def Busqueda(palabra):
   
   print(f"{palabra}")
   
   palabra = input("Escribe una palabra clave del título que estas buscando: ")

for clave, valor in bibliografia.items():
      titulo = {valor["titulo"]}


if  palabra in str(titulo).lower():
          resultado.append(titulo)
                
print(f"se encontraron {len(resultado)}  los cuales son: {resultado}")


