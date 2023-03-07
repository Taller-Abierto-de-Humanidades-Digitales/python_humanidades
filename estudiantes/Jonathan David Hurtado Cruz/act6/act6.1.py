libro1 = ["Fiodor Dostoyenvski; El jugador; 1886; Realist; novela; Alianza editorial; Rusia","Simone deBeauvoir; Sangre de los otros; 1944; Histórica; novela; Seix Barral; Francia", "Albert Camus; El extrajenro; 1942; Existencialismo; novela; Éditions Gallimard; Francia", "Jean-Paul Sartre; La Naúsea; 1938; Existencialismo; novela; Éditions Gallimard; Francia","Franz Kafka; La Metaformosis; 1915; Existencialismo; novela; Kurt Wolff Verlag; Alemania"]

bibliografia = {"000" : {
    "tipo" : "",
    "autor" : [{"nombre" : "", "apellido" : ""}],
    "titulo" : "",
    "editorial" : "",
    "fecha" : 0,
    "lugar" : "" 
   }
}


for lib in libro1:
    clave = int(list(bibliografia.keys())[-1]) + 1
    clave = str (clave).zfill(3)

 # if len (lib.split("; ")[0].split(" ")) > 2:
        #nombre = lib.split("; ")[0].split(' ')[:2]
      
    
   # else: 
        #nombre = lib.split("; ")[0].split(' ')[0] """

       
    bibliografia[clave] = {
        "tipo":lib.split('; ')[4],
        'autor':[{"nombre": lib.split(";")[0].split(" ")[0], "apellido": lib.split(";")[0].split(" ")[1]}],
        'titulo':lib.split('; ')[1],
        'editorial':lib.split('; ')[5],
        'fecha':lib.split('; ')[2],
        'lugar':lib.split('; ')[6]
    }

""" if bibliografia:
    print("El diccionario bibliogafía no está vacío")
elif bibliografia:
    print("El diccionario bibliografía puede estar vacío")
else:
    print("Los diccionarios están vacíos") """
    

for clave, valor in bibliografia.items():
    if valor["tipo"] == "novela":
       print(f"""
        Identificador: {clave}
        Título: {valor["titulo"]}
        Autor: {valor["autor"][0]["apellido"]}, {valor["autor"][0]["nombre"]}
        Editorial: {valor["editorial"]}
        Lugar: {valor["lugar"]}
        Fecha: {valor["fecha"]}
       """) 
        
        
#print(bibliografia)

##Ejercicio 2 

revistas = ["Vincent Ducatteeuw; Critical Reflections on Cinema Belgica: The Database for New Cinema History in Belgium; 2023; Journal of Open Humanities Data; 9; 1; https://doi.org/10.5334/johd.91", "Li Nguyen; Automatic Language Identification in Code-Switched Hindi-English Social Media Text; 2021; Journal of Open Humanities Data; 7; 7;https://doi.org/10.5334/johd.44 ", "Mei-Shin Wu; Computer-Assisted Language Comparison: State of the Art; 2020; Journal of Open Humanities Data; 6; 2; https://doi.org/10.5334/johd.12 "]


periodico = ["Noticias DW; Documental francés gana el Oso de Oro en la Berlinale; cultura; 25.02.2023; https://p.dw.com/p/4NzKy", "Noticias DW; Los Grammy Latinos se entregarán en España en 2023; cultura; 24.02.2023; https://p.dw.com/p/4Nxh4"]

video = ["Darin McNabb; El existencialismo: una introducción 1/2; 2013; https://www.youtube.com/watch?v=JotchOUEdfk"]


for lib in periodico:
    clave = int(list(bibliografia.keys())[-1]) + 1
    clave = str (clave).zfill(3)

bibliografia[clave] = {
        "fecha":lib.split('; ')[3],
        'periodico':[{"nombre": lib.split(";")[0].split(" ")[0], "apellido": lib.split(";")[0].split(" ")[1]}],
        'titulo':lib.split('; ')[1],
        'seccion':lib.split('; ')[2],
        'url': lib.split('; ')[4]

    }


for lib in revistas:
    clave = int(list(bibliografia.keys())[-1]) + 1
    clave = str (clave).zfill(3)

bibliografia[clave] = {
        "revista":lib.split('; ')[3],
        'autor':[{"nombre": lib.split(";")[0].split(" ")[0], "apellido": lib.split(";")[0].split(" ")[1]}],
        'titulo':lib.split('; ')[1],
        'volumen':lib.split('; ')[4],
        'fecha':lib.split('; ')[2],
        'numero':lib.split('; ')[5],
        'url': lib.split('; ')[6]

    }

for lib in video:
    clave = int(list(bibliografia.keys())[-1]) + 1
    clave = str (clave).zfill(3)

bibliografia[clave] = {
        'canal':[{"nombre": lib.split(";")[0].split(" ")[0], "apellido": lib.split(";")[0].split(" ")[1]}],
        'titulo':lib.split('; ')[1],
        'fecha':lib.split('; ')[2],
        'url': lib.split('; ')[3]

    }



print (bibliografia)
hheee
