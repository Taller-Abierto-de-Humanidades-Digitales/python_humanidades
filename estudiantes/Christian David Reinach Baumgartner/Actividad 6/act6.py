
#   NOTA: ME DISCULPO POR LA TARDANZA EN LA ENTREGA DE ESTE EJERCICIO; HE TENIDO ALGUNAS OCUPACIONES CON MIS DEBERES
#   COMO ASISTENTE GRADUADO

#Ejercicio 1
catalog=['Walter Rudin; Real and Complex Analysis; 1966; McGraw-Hill; Nueva York', 'Stefan Banach; Théorie des opérations linéaires; 1932; Instytut Matematyczny Polskiej Akademii Nauk; Varsovia', 'Stan Wagon; The Banach-Tarski Paradox; 1985; Cambridge University Press; Nueva York', "Gregory Moore; Zermelo's Axiom of Choice; 1982; Springer-Verlag; Nueva York", 'Andrei Kolmogorov; Grundbegriffe der Wahrscheinlichkeitsrechnung; 1933; Springer; Berlín', 'Donald Cohn; Measure Theory; 2015; Birkhäuser; Nueva York', 'Frigyes Riesz; Functional Analysis; 1955; Dover Publications; Nueva York', 'Bernt Øksendal; Stochastic Differential Equations; 1982; Springer; Oslo']

print(len(catalog))
bibliografia = {"000" : {
    "tipo" : "",
    "autor" : [{"nombre" : "", "apellido" : ""}],
    "titulo" : "",
    "editorial" : "",
    "fecha" : 0,
    "lugar" : ""
    },
}

  #Añadir elementos al diccionario

for elemento in catalog:
    clave = int(list(bibliografia.keys())[-1]) + 1
    clave = str(clave).zfill(3)
    bibliografia[clave] = {
        "tipo": "libro",
        "autor": [{"nombre": elemento.split("; ")[0].split(" ")[0], "apellido": elemento.split("; ")[0].split(" ")[1]}],
        "titulo": elemento.split("; ")[1],
        "editorial": elemento.split("; ")[3],
        "fecha": int(elemento.split("; ")[2]),
        "lugar": elemento.split("; ")[-1]
    }
  
del bibliografia["000"]
print(bibliografia)

  #Imprime organizadamente el diccionario
for clave, valor in bibliografia.items():
    if valor[ 'tipo'] == "libro":
        print (f"Identificador: {clave},\
               \n Título: {valor['titulo']}\
               \n Autor: {valor['autor'][0]['apellido']}, {valor['autor'][0]['nombre']},\
               \n Editorial: {valor ['editorial']},\
               \n Lugar: {valor['lugar']},\
               \n Fecha: {valor ['fecha']}.")
        



#Ejercicio 2


 #Creación de listas adicionales

articulos=["James Herbert; Turner's Uncertain Angel; The Journal of Religion; 91; 4; 2011; https://www.journals.uchicago.edu/doi/abs/10.1086/660904?journalCode=jr", "Philipp Metzner, Lars Putzig, Illia Horenko; Analysis of Persistent Nonstationary Time Series and Applications; Communications in Applied Mathematics and Computational Science; 7; 2; 2012; https://projecteuclid.org/journals/communications-in-applied-mathematics-and-computational-science/volume-7/issue-2/Analysis-of-persistent-nonstationary-time-series-and-applications/10.2140/camcos.2012.7.175.full", "Aihua Zhang, Chen Chen, Hamid Karimi; A New Adaptive LSSVR with Online Multikernel RBF Tuning to Evaluate Analog Circuit Performance; Abstract and Applied Analysis; 2013; sin número; 2013; https://www.hindawi.com/journals/aaa/2013/231735/"]
columnas=["Esther Felden; Wie China seine Top-Studenten in Deutschland kontrolliert; Deutsche Welle; Investigación; 2023; https://p.dw.com/p/4OIIU", "Shlomit Lasky; Metropolitan Museum benennt Gemälde von Degas um; Deutsche Welle; Kunst in Kriegszeiten; 2023; https://p.dw.com/p/4NbtC"]
youtube=["Izaak Weiss; Double Pendulum Chaos Demonstration; 2016; https://youtu.be/pEjZd-AvPco"]


  #Añadir artículos al diccionario

for elemento in articulos:
    clave = int(list(bibliografia.keys())[-1]) + 1
    clave = str(clave).zfill(3)
    if len(elemento.split("; ")[0].split(", ")) == 1:
        bibliografia[clave] = {
        "tipo": "artículo científico",
        "autor": [{"nombre": elemento.split("; ")[0].split(" ")[0], "apellido": elemento.split("; ")[0].split(" ")[1]}],
        "titulo": elemento.split("; ")[1],
        "fecha": int(elemento.split("; ")[5])
        }
            
        bibliografia[clave]['revista']=elemento.split("; ")[2]  #Creo las pertinentes
        bibliografia[clave]['volumen']=elemento.split("; ")[3]
        bibliografia[clave]['número']=elemento.split("; ")[4]
        bibliografia[clave]['url']=elemento.split("; ")[6]
    else:
        bibliografia[clave] = {
        "tipo": "artículo científico",
        "autor": [{"nombre": elemento.split("; ")[0].split(", ")[0].split(" ")[0], "apellido": elemento.split("; ")[0].split(", ")[0].split(" ")[1]}, {"nombre": elemento.split("; ")[0].split(", ")[1].split(" ")[0], "apellido": elemento.split("; ")[0].split(", ")[1].split(" ")[1]}, {"nombre": elemento.split("; ")[0].split(", ")[2].split(" ")[0], "apellido": elemento.split("; ")[0].split(", ")[2].split(" ")[1]}],
        "titulo": elemento.split("; ")[1],
        "fecha": int(elemento.split("; ")[5])
        }
            
        bibliografia[clave]['revista']=elemento.split("; ")[2]  #Creo las categorías pertinentes
        bibliografia[clave]['volumen']=elemento.split("; ")[3]
        bibliografia[clave]['número']=elemento.split("; ")[4]
        bibliografia[clave]['url']=elemento.split("; ")[6]



  #Añadir columnas de prensa
for elemento in columnas:
    clave = int(list(bibliografia.keys())[-1]) + 1
    clave = str(clave).zfill(3)
    bibliografia[clave] = {
        "tipo": "artículo de prensa",
        "autor": [{"nombre": elemento.split("; ")[0].split(" ")[0], "apellido": elemento.split("; ")[0].split(" ")[1]}],
        "titulo": elemento.split("; ")[1],
        "fecha de publicación": int(elemento.split("; ")[4])
        }
    bibliografia[clave]['periódico']=elemento.split("; ")[2]  #Creo las categorías pertinentes
    bibliografia[clave]['sección']=elemento.split("; ")[3]
    bibliografia[clave]['url']=elemento.split("; ")[5]       


  #Añadir vídeo de YouTube
for elemento in youtube:
    clave = int(list(bibliografia.keys())[-1]) + 1
    clave = str(clave).zfill(3)
    bibliografia[clave] = {
        "tipo": "vídeo de YouTube",
        "titulo": elemento.split("; ")[1]     
        }
    bibliografia[clave]['canal']=elemento.split("; ")[0]  #Creo las categorías pertinentes
    bibliografia[clave]['fecha de publicación']=int(elemento.split("; ")[2])
    bibliografia[clave]['url']=elemento.split("; ")[3]       

#Por cuestiones de eficiencia, creo que sería mejor imprimir todo por categorías de una vez.
#Ejercicio 3

print("----------------------------------------------------------------------------")
print("LISTADO DE LIBROS")
print("----------------------------------------------------------------------------")
for clave, valor in bibliografia.items():
    if valor[ 'tipo'] == "libro":        
        print (f"Identificador: {clave}\
               \n Título: {valor['titulo']}\
               \n Autor: {valor['autor'][0]['apellido']}, {valor['autor'][0]['nombre']}\
               \n Editorial: {valor ['editorial']},\
               \n Lugar: {valor['lugar']}\
               \n Fecha: {valor ['fecha']}")
        

    
print("----------------------------------------------------------------------------")
print("LISTADO DE ARTÍCULOS CIENTÍFICOS")
print("----------------------------------------------------------------------------")
for clave, valor in bibliografia.items():
    if valor[ 'tipo'] == "artículo científico":
        if len(valor['autor']) == 1:
            print (f"Identificador: {clave}\
               \n Título: {valor['titulo']}\
               \n Autor: {valor['autor'][0]['apellido']}, {valor['autor'][0]['nombre']}\
               \n Revista: {valor ['revista']}\
               \n Volumen: {valor['volumen']}\
               \n Número: {valor ['número']}\
               \n Fecha: {valor['fecha']}\
                   \n URL: {valor['url']}")
        else:
            print(f"Identificador: {clave}\
                \n Título: {valor['titulo']}\
               \n Autor: {valor['autor'][0]['apellido']}, {valor['autor'][0]['nombre']}; {valor['autor'][1]['apellido']}, {valor['autor'][1]['nombre']}; {valor['autor'][2]['apellido']}, {valor['autor'][2]['nombre']} \
               \n Revista: {valor ['revista']}\
               \n Volumen: {valor['volumen']}\
               \n Número: {valor ['número']}\
               \n Fecha: {valor['fecha']}\
                   \n URL: {valor['url']}")
            

print("----------------------------------------------------------------------------")
print("LISTADO DE ARTÍCULOS DE PRENSA")
print("----------------------------------------------------------------------------")
for clave, valor in bibliografia.items():
    if valor['tipo']== "artículo de prensa":
        print(f"Identificador: {clave}\
               \n Título: {valor['titulo']}\
               \n Autor: {valor['autor'][0]['apellido']}, {valor['autor'][0]['nombre']}\
               \n Periódico: {valor ['periódico']}\
               \n Sección: {valor['sección']}\
               \n Fecha: {valor['fecha de publicación']}\
               \n URL: {valor['url']}")

print("----------------------------------------------------------------------------")
print("LISTADO DE VÍDEOS DE YOUTUBE")
print("----------------------------------------------------------------------------")
for clave, valor in bibliografia.items():
    if valor['tipo'].lower()=="vídeo de youtube":
        print(f"Identificador: {clave}\
               \n Título: {valor['titulo']}\
               \n Canal: {valor['canal']}\
               \n Fecha: {valor['fecha de publicación']}\
               \n URL: {valor['url']}")
  
#Ejercicio 4

  #Diccionario de ciudades
ciudadesporlibros={"Nueva York": 0,
                   "Berlín": 0,
                   "Varsovia": 0,
                   "Oslo":0}

  #Contar ciudades
for clave, valor in bibliografia.items():
    if valor['tipo']=="libro":
        if valor['lugar']=="Nueva York":
            ciudadesporlibros["Nueva York"]+=1
        elif valor['lugar']=="Berlín":
            ciudadesporlibros["Berlín"]+=1
        elif valor['lugar']=="Varsovia":
            ciudadesporlibros["Varsovia"]+=1
        else:
            ciudadesporlibros["Oslo"]+=1
print("----------------------------------------------------------------------------")
print("CIUDADES POR LIBROS")
print("----------------------------------------------------------------------------")
print(f" Berlín={ciudadesporlibros['Berlín']}\
      \n Nueva York={ciudadesporlibros['Nueva York']}\
      \n Oslo={ciudadesporlibros['Oslo']}\
      \n Varsovia={ciudadesporlibros['Varsovia']}")