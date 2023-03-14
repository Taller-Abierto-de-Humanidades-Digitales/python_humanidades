items = []

def busqueda (titulo):
   for buscar in Catalogo_bibliografia:
     if buscar.lower() in Catalogo_bibliografia[titulo].lower():
        items.append(Catalogo_bibliografia[titulo])
        print(f"{titulo} se encuentra en los siguentes items: /n {items}")


busqueda(titulo=)
       


############

       def busqueda(titulo):
    print(f"{titulo} si se encuentra dentro d ela busqueda de la palabra clave")

    titulo = Catalogo_bibliografia[titulo]

############


Catalogo_bibliografia = {"001" : {
    "tipo" : "Libro",
    "autor" : [{"nombre" : "Sarah J.", "apellido" : "Jackson"}],
    "titulo" : "#HashtagActivism: Networks of Race and Gender Justice",
    "Publisher" : "The MIT Press",
    "fecha" : 2020,
    "lugar" : "Cambridge, Massachusetts",
    "url" : "https://direct.mit.edu/books/book/4597/HashtagActivismNetworks-of-Race-and-Gender-Justice"
    },

    "002" : {
    "tipo" : "Capítulo de Libro",
    "autor" : [{"nombre" : "Roopika", "apellido" : "Risam"}],
    "titulo" : "Decolonizing the Digital Humanities in Theory and Practice",
    "Publisher" : "New York",
    "fecha" : 2018,
    "lugar" : "Routledge",
    "url" : "https://www.taylorfrancis.com/books/9781317549093/chapters/10.4324/9781315730479-8"
    },

    "003" : {
    "tipo" : "Capítulo de libro",
    "autor" : [{"nombre" : "Kim", "apellido" : "Gallon"}],
    "titulo" : "Making a Case for the Black Digital Humanities",
    "Publisher" : "University of Minnesota Press",
    "fecha" : 2016,
    "lugar" : "Minnesota, EE.UU",
    "url" : "https://www.jstor.org/stable/10.5749/j.ctt1cn6thb.7"
    },

    "004" : {
    "tipo" : "Libro",
    "autor" : [{"nombre" : "Patricia Hill", "apellido" : "Collins"}],
    "titulo" : "Black feminist thought: knowledge, consciousness, and the politics of empowerment",
    "Publisher" : "Routledge",
    "fecha" : 2000,
    "lugar" : "New York",
    },

    "005" : {
    "tipo" : "Capítulo de libro",
    "autor" : [{"nombre" : "Safiya Umoja", "apellido" : "Noble"}],
    "titulo" : "Toward a Critical Black Digital Humanities",
    "Publisher" : "University of Minnesota Press",
    "fecha" : 2019,
    "lugar" : "Minnesota",
    },

    "006" : {
    "tipo" : "Artículos académicos",
    "autor" : [{"nombre" : "Kattya", "apellido" : "Hernández"}],
    "titulo" : "Cuerpos insurgentes: territorios de re-existencia de las y los afrodescendientes",
    "revista" : "La manzana de la discordia",
    "volumen" : 14,
    "numero" : 1,
    "fecha" : 2019,
    "lugar" : "Colombia",
    "url" :  "https://dialnet.unirioja.es/servlet/articulo?codigo=7446265",
    },

    "007" : {
    "tipo" : "Artículos académicos",
    "autor" : [{"nombre" : "Ochy", "apellido" : "Curiel"}],
    "titulo" : "El régimen heterosexual y la nación. Aportes del lesbianismo feminista a la antropología",
    "revista" : "La manzana de la discordia",
    "volumen" : 6,
    "numero" : 1,
    "fecha" : 2012,
    "lugar" : "Colombia",
    "url" :  "https://bibliotecadigital.univalle.edu.co/handle/10893/3501",
    },

    "008" : {
    "tipo" : "Artículos académicos",
    "autor" : [{"nombre" : "Rachel", "apellido" : "Kuo"}],
    "titulo" : "Racial justice activist hashtags: Counterpublics and discourse circulation",
    "revista" : "New Media & Society",
    "volumen" : 20,
    "numero" : 2,
    "fecha" : 2018,
    "lugar" : "New York",
    "url" :  "https://journals.sagepub.com/doi/10.1177/1461444816663485",
    },

    "009" : {
    "tipo" : "Videos",
    "autor" : "Black Enterprise",
    "titulo" : "What is Afrofuturism?",
    "Canal" : "youtube",
    "fecha" : 2018,
    "url" :  "https://www.youtube.com/watch?v=AgXujySEuIE",
    },

    "010" : {
    "tipo" : "Videos",
    "autor" : "The Berkman Klein Center for Internet & Society",
    "titulo" : "Kishonna L. Gray: Examining Black Feminism in the Digital Era",
    "Canal" : "youtube",
    "fecha" : 2017,
    "url" :  "https://www.youtube.com/watch?v=7fYeL3WH4Xk",
    },

    "011" : {
    "tipo" : "Videos",
    "autor" : "HistoryVille",
    "titulo" : "Sarah Baartman: The Tragic Exploitation of an African Woman",
    "Canal" : "youtube",
    "fecha" : 2022,
    "url" :  "https://www.youtube.com/watch?v=-CSeXTbr2ng",
    },

}

Catalogo_bibliografia["001"]["titulo"]

########

titulos = bibliografia[clave]["titulo"]


def busqueda(palabra_clave):
    for clave, valor in bibliografia.items:


        print(f"{clave} si se encuentra dentro d ela busqueda de la palabra clave")


######

seleccion = []    
for clave, valor in bibliografia.items():
    titulos = bibliografia[clave]["titulo"]
    seleccion.append(bibliografia)
    print(titulos)

buscar = input("Ingresa la palabra clave que quieras buscar: ")

def resultado(busqueda):
    if buscar.lower() in titulos.lower():
        print(f"{busqueda} si se encuentra en estos libros")




######
#
# seleccion = []    

buscar = "Toward a Critical Black Digital Humanities"

def resultado(busqueda):
    for clave, valor in bibliografia.items():
        titulos = bibliografia[clave]["titulo"]
        seleccion.append(bibliografia)

    if buscar.lower() in titulos:
        print(f"{busqueda} si se encuentra en estos libros{seleccion}")
    else:
        print("la estas cagando chaval")    



 ######
 # 
 # 
seleccion = []    

buscar = "Toward"

def resultado(busqueda):
    for clave in bibliografia.items():
        if busqueda in titulos:
            titulos = bibliografia[clave]["titulo".split(" ")]

            print(f"{busqueda} si se encuentra en estos libros{seleccion}")
    else:
        print("la estas cagando chaval")          



# un total enredo 
if  titulo in bibliografia.keys()
      print("se encuentra")

def resultado(busqueda):
      print(busqueda)


for clave, valor in bibliografia.items():
           titulo = {valor["titulo"]}
           #print(titulo)

palabra_clave = "Toward"



# el programa funciona a lo rudimentarios. 
resultado = []

palabra = input("Escribe una palabra clave del título que estas buscando: ")

for clave, valor in bibliografia.items():
           titulo = {valor["titulo"]}
           if  palabra.lower() in str(titulo).lower():
                resultado.append(titulo)
                print(f"se encontraron {len(resultado)}  los cuales son: {resultado}")




# intento para el ejercicio 3/7
tipo = str(input())
autor = str(input())
titulo = str(input())
editorial = str(input())
fecha = int(input())
lugar = str(input())
url = input()


def nuevos_item(tipo, autor, titulo, editorial,fecha,lugar,url):
    for clave, valor in bibliografia.items():
        bibliografia[clave]["tipo"] = tipo
        bibliografia[clave]["autor"] = autor
        bibliografia[clave]["titulo"] = titulo
        bibliografia[clave]["editorial"] = editorial



 # 2
 
def nuevos_item(tipo, autor, titulo, editorial,fecha):

    for clave in bibliografia.items():

        tipo = str(input())
        bibliografia[clave]["tipo"] = tipo

        autor = str(input())
        bibliografia[clave]["autor"] = autor


        titulo = str(input())
        bibliografia[clave]["titulo"] = titulo

        editorial = str(input())
        bibliografia[clave]["editorial"] = editorial

    
        fecha = int(input())
        bibliografia[clave]["fecha"] = fecha       