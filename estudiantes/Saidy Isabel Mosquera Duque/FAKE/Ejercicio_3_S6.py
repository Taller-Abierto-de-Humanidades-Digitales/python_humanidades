bibliografia = {"001" : {
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

}


###### REVISTAS 

lista_revistas = [
    "Kattya Hernández; Cuerpos insurgentes: territorios de re-existencia de las y los afrodescendientes; 2019; La manzana de la discordia; 14; 1; https://dialnet.unirioja.es/servlet/articulo?codigo=7446265", "Ochy Curiel; El régimen heterosexual y la nación. Aportes del lesbianismo feminista a la antropología; 2012; La Manzana de la Discordia; 6; 1; https://bibliotecadigital.univalle.edu.co/handle/10893/3501","Rachel Kuo; Racial justice activist hashtags: Counterpublics and discourse circulation; 2018; New Media & Society; 20; 2; https://journals.sagepub.com/doi/10.1177/1461444816663485"
]


for elemento in lista_revistas:
    clave = int(list(bibliografia.keys())[-1]) + 1
    clave = str(clave).zfill(3)

    bibliografia[clave] = {
        "tipo": "Artículos academicos",
        "autor": [{"nombre": elemento.split(";")[0].split(" ")[0], "apellido": elemento.split(";")[0].split(" ")[1]}],
        "titulo": elemento.split(";")[1],
        "revista": elemento.split(";")[3],
        "fecha": int(elemento.split(";")[2]),
        "vol": int(elemento.split(";")[4]), 
        "numero" : int(elemento.split(";")[5]),
        "url" : elemento.split(";")[-1],

    }



#######  VIDEOS 
lista_videos = [
    "What is Afrofuturism?; Black Enterprise; 2018; https://www.youtube.com/watch?v=AgXujySEuIE", "Kishonna L. Gray: Examining Black Feminism in the Digital Era; The Berkman Klein Center for Internet & Society; 2017; https://www.youtube.com/watch?v=7fYeL3WH4Xk", "Sarah Baartman: The Tragic Exploitation of an African Woman; HistoryVille; 2022; https://www.youtube.com/watch?v=-CSeXTbr2ng"
]


for elemento in lista_videos:
    clave = int(list(bibliografia.keys())[-1]) + 1
    clave = str(clave).zfill(3)


    bibliografia[clave] = {
        "tipo": "video",
        "titulo": elemento.split(";")[0],
        "canal": elemento.split(";")[1],
        "fecha": int(elemento.split(";")[2]),
        "url" : elemento.split(";")[-1],
    }



clave = "Artículos academicos"

Resultado = []

for busqueda in bibliografia.items():
    if busqueda["tipo"] == clave:
        print(Resultado.append(bibliografia))