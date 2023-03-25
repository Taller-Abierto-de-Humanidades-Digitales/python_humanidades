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


N_tipo = []
N_titulo = []

 

for c in Catalogo:
    clave = int(list(bibliografia.keys())[-1]) + 1
    
    clave = str(clave).zfill(3)


N_tipo = input("Escribe aqui si es un [capítulo de libro o libro]: ")
bibliografia["tipo"] = N_tipo

N_titulo = input("Escribe el tíitulo: ")
bibliografia["titulo"] = N_titulo


[N_titulo + N_tipo].A

print(f"El nuevo elemnto subido es: tipo:{N_tipo}, titulo:{N_titulo}")


#print(bibliografia)

