print('-------------------------------------------')
print('ACTIVIDAD 6: EJERCICIO 1')

libros = ['Cuentos completos 1;Isaac Asimov;2009;Ficción;Libro;Debolsillo;Estados Unidos', 
          'Cuentos completos 2;Isaac Asimov;2009;Ficción;Libro;Debolsillo;Estados Unidos', 
          'De Animales a Dioses;Yuval Noah Harari;2015;Historia General;Libro;Debate;Israel', 
          'Homo Deus;Yuval Noah Harari;2016;Historia General;Libro;Debate;Israel', 
          'Prohibido Nacer;Trevor Noah;2017;Autobiografía;Libro;Blackie Books;España', 
          'Somos Luces Abismales;Carolina Sanín;2018;Ensayos Literarios;Libro;Penguin Random House;Colombia', 
          'Muerte con Pingüino;Andrei Kurkov;1996;Novela;Libro;Blackie Books;España', 
          'Que Viva la Música!;Andrés Caicedo;1977;Novela;Libro;Debolsillo;Colombia',
          'The Beach;Alex Garland;1996;Novela;Libro;Viking;Reino Unido',
          'La teoria del todo;Arturo Quirantes;2018;Divulgación;Libro;National Geographic;España',
          'Breve historia de la ciencia;Tom Jackson;2022;Divulgación;Libro;BLUME (Naturart);España',
          'Ensayo sobre la ceguera;Jose Saramago;1995;Novela;Libro;Debolsillo;España']

bibliografia = {"000" : {
    "tipo" : "",
    "autor" : [{"nombre" : "", "apellido" : ""}],
    "titulo" : "",
    "editorial" : "",
    "fecha" : 0,
    "lugar" : ""
    },
}

for l in libros:
    clave = int(list(bibliografia.keys())[-1]) + 1
    clave = str(clave).zfill(3)    
    
    if len(l.split(';')[1].split(' ')) > 2:
        nombre = l.split(';')[1].split(' ')[:2]
        nombre = ' '.join(nombre)
        
    else:
        nombre = l.split(';')[1].split(' ')[0]
        
    
    bibliografia[clave] = {
        "tipo":l.split(';')[4],
        'autor':{'nombre':nombre,'apellido': l.split(';')[1].split(' ')[-1]},
        'titulo':l.split(';')[0],
        'editorial':l.split(';')[5],
        'fecha':l.split(';')[2],
        'lugar':l.split(';')[6]
    }

del bibliografia['000']

print('LISTA DE LIBROS')
print()

for clave in bibliografia:
    print(f'''
    Identificador: {clave}
    Título: {bibliografia[clave]['titulo']}
    Autor: {bibliografia[clave]['autor']['nombre']} {bibliografia[clave]['autor']['apellido']}
    Editorial: {bibliografia[clave]['editorial']}
    Lugar: {bibliografia[clave]['lugar']}
    Fecha: {bibliografia[clave]['fecha']}
    ''')
    
print('-------------------------------------------')
print('ACTIVIDAD 6: EJERCICIO 2')

# LISTAS ARTÍCULOS Y VIDEOS

artrevistas = ['Artículo  Revista;Steven Heller;Dreaming in Colors;Eye Magazine Ltd.;2016;Londrés, Reino Unido;Eye: The International Review of Graphic Design; 23;91;https://www.proquest.com/docview/234948863/E32953D8051F41A5PQ/2?accountid=34489','Artículo  Revista;Peter L. Forberg; Critical Design as Theory, Experiment, and Data: A Sociologically-Informed Approach to Visualizing Networks of Loss;;2022;Providence, Estados Unidos;Digital Humanities Quarterly;16;4;https://ezproxy.uniandes.edu.co:8443/login?url=https://www.proquest.com/scholarly-journals/critical-design-as-theory-experiment-data/docview/2715485146/se-2','Artículo  Revista;Antony Tang;What makes software design effective?;Delft University of Technology;06-10-2010;Paises Bajos;Design Studies;31;6;https://www-sciencedirect-com.ezproxy.uniandes.edu.co/science/article/pii/S0142694X10000669']

artperiodico = ['Artículo Periódico;Kashmir Hill;This Tool Could Protect Artists From A.I.-Generated Art That Steals Their Style;13-02-2023;Nueva York, Estados Unidos;The New York Times;Business;https://www.nytimes.com/2023/02/13/technology/ai-art-generator-lensa-stable-diffusion.html','Artículo Periódico;Dan Sinykin;How computational analysis is teaching us to read in new ways;30-07-2018;Washington, Estados Unidos;The Washington Post;Posteverything, Perspective;https://www.washingtonpost.com/news/posteverything/wp/2018/07/30/how-computational-analysis-is-teaching-us-to-read-in-new-ways/','Artículo Periódico;Laura Pappano;Learning to Think Like a Computer;09-04-2017;New York, Estados Unidos; The New York Times;Education Life;https://www.nytimes.com/2017/04/04/education/edlife/teaching-students-computer-code.html']

vidyoutube = ['Vídeo Youtube;;Maratón HD de la Red Colombiana de Humanidades Digitales: Santiago Ojeda y Juan Pablo Moya;15-09-2020;Facultad de Artes y Humanidades Uniandes;https://www.youtube.com/watch?v=Ijf8Ysq2pFg&t=124s','Vídeo Youtube;Sergio Rodríguez;Glosario HD: Visualización de datos;27-03-2021;Red Colombiana de Humanidades Digitales;https://www.youtube.com/watch?v=hU758BJazyo&t=2s','Vídeo Youtube;Nicolás Schurmann;Aprende GIT ahora! curso completo GRATIS desde cero;18-02-2022;HolaMundo;https://www.youtube.com/watch?v=VdGzPZ31ts8&t=2904s']

#LISTADO ELEMENTOS SUMADOS

nuevos_elementos = artrevistas + artperiodico + vidyoutube

for l in nuevos_elementos:
    clave = int(list(bibliografia.keys())[-1]) + 1
    clave = str(clave).zfill(3)    

    if len(l.split(';')[1].split(' ')) > 2:
        nombre = l.split(';')[1].split(' ')[:2]
        nombre = ' '.join(nombre)
        
    else:
        nombre = l.split(';')[1].split(' ')[0]
    
        
    bibliografia[clave] = {
        "tipo":l.split(';')[0],
        'autor':{'nombre':nombre,'apellido': l.split(';')[1].split(' ')[-1]},
        'titulo':l.split(';')[2],
    }

    if 'revista' in bibliografia[clave]['tipo'].lower():
        valores = l.split(';')[3:10]
        subclaves = ['editorial', 'fecha', 'lugar', 'revista', 'volumen', 'numero', 'url']
        for subclave, valor in zip(subclaves, valores):
            bibliografia[clave][subclave] = valor
  
    elif 'Artículo Periódico' in bibliografia[clave]['tipo']:
        valores = l.split(';')[3:8]
        subclaves = ['fecha', 'lugar', 'periodico', 'seccion', 'url']
        for subclave, valor in zip(subclaves, valores):
            bibliografia[clave][subclave] = valor
            
    elif 'youtube' in bibliografia[clave]['tipo'].lower():
        valores = l.split(';')[3:6]
        subclaves = ['fecha', 'canal','url']
        for subclave, valor in zip(subclaves, valores):
            bibliografia[clave][subclave] = valor

# IMPRESIÓN CATÁLOGO

print('// BIBLIOGRAFÍA //')
print('La lista tiene:', len(bibliografia,),' elementos')
print()

print('LISTA DE LIBROS')
print()
for clave in bibliografia:
    if 'libro' in bibliografia[clave]['tipo'].lower():
        print(f'''
            Identificador: {clave}
            Tipo: {bibliografia[clave]['tipo']}
            Título: {bibliografia[clave]['titulo']}
            Autor: {bibliografia[clave]['autor']['nombre']} {bibliografia[clave]['autor']['apellido']}
            Editorial: {bibliografia[clave]['editorial']}
            Lugar: {bibliografia[clave]['lugar']}
            Fecha: {bibliografia[clave]['fecha']}
            ''')

print()
print('LISTA DE ARTÍCULOS DE REVISTAS')
print()
for clave in bibliografia:
    if 'revista' in bibliografia[clave]['tipo'].lower():
        print(f'''
            Identificador: {clave}
            Tipo: {bibliografia[clave]['tipo']}
            Título: {bibliografia[clave]['titulo']}
            Autor: {bibliografia[clave]['autor']['nombre']} {bibliografia[clave]['autor']['apellido']}
            Editorial: {bibliografia[clave]['editorial']}
            Lugar: {bibliografia[clave]['lugar']}
            Fecha: {bibliografia[clave]['fecha']}
            Revista: {bibliografia[clave]['revista']}
            Volumen: {bibliografia[clave]['volumen']}
            Número: {bibliografia[clave]['numero']}
            Url: {bibliografia[clave]['url']}
            ''')

print()
print('LISTA DE ARTÍCULOS DE PERIÓDICOS')
print()
for clave in bibliografia:
    if 'periódico' in bibliografia[clave]['tipo'].lower():
        print(f'''
            Identificador: {clave}
            Tipo: {bibliografia[clave]['tipo']}
            Título: {bibliografia[clave]['titulo']}
            Autor: {bibliografia[clave]['autor']['nombre']} {bibliografia[clave]['autor']['apellido']}
            Lugar: {bibliografia[clave]['lugar']}
            Fecha: {bibliografia[clave]['fecha']}
            Periódico: {bibliografia[clave]['periodico']}
            Sección: {bibliografia[clave]['seccion']}
            Url: {bibliografia[clave]['url']}
            ''')

print()
print('LISTA DE VIDEOS DE YOUTUBE')
print()
for clave in bibliografia:
    if 'youtube' in bibliografia[clave]['tipo'].lower():
        print(f'''
            Identificador: {clave}
            Tipo: {bibliografia[clave]['tipo']}
            Título: {bibliografia[clave]['titulo']}
            Autor: {bibliografia[clave]['autor']['nombre']} {bibliografia[clave]['autor']['apellido']}
            Fecha: {bibliografia[clave]['fecha']}
            Canal: {bibliografia[clave]['canal']}
            Url: {bibliografia[clave]['url']}
            ''')


print('-------------------------------------------')
print('ACTIVIDAD 6: EJERCICIO 3')
print()


errorselecc = True
while errorselecc:
    seleccion = input('''Ingrese la letra correspondiente al tipo de material que esta buscando: '
    'a. libro, b. artículo revista, c. artículo periódico, d. video youtube
    ''')

    if seleccion == "a":
        errorselecc = False
    elif seleccion == "b":
        errorselecc = False
    elif seleccion == "c":
        errorselecc = False
    elif seleccion == "d":
        errorselecc = False
    else:
        print("Selección errada, intente de nuevo.")


if 'a' == seleccion:
    print('LISTA DE LIBROS')
    print()

    for clave in bibliografia:
        if 'libro' in bibliografia[clave]['tipo'].lower():
            print(f'''
            Identificador: {clave}
            Título: {bibliografia[clave]['titulo']}
            Autor: {bibliografia[clave]['autor']['nombre']} {bibliografia[clave]['autor']['apellido']}
            Editorial: {bibliografia[clave]['editorial']}
            Lugar: {bibliografia[clave]['lugar']}
            Fecha: {bibliografia[clave]['fecha']}
            ''')

elif 'b' == seleccion:
    print()
    print('LISTA DE ARTÍCULOS DE REVISTAS')
    print()
    for clave in bibliografia:
        if 'revista' in bibliografia[clave]['tipo'].lower():
            print(f'''
                Identificador: {clave}
                Tipo: {bibliografia[clave]['tipo']}
                Título: {bibliografia[clave]['titulo']}
                Autor: {bibliografia[clave]['autor']['nombre']} {bibliografia[clave]['autor']['apellido']}
                Editorial: {bibliografia[clave]['editorial']}
                Lugar: {bibliografia[clave]['lugar']}
                Fecha: {bibliografia[clave]['fecha']}
                Revista: {bibliografia[clave]['revista']}
                Volumen: {bibliografia[clave]['volumen']}
                Número: {bibliografia[clave]['numero']}
                Url: {bibliografia[clave]['url']}
                ''')

elif 'c' == seleccion:
    print()
    print('LISTA DE ARTÍCULOS DE PERIÓDICOS')
    print()
    for clave in bibliografia:
        if 'periódico' in bibliografia[clave]['tipo'].lower():
            print(f'''
                Identificador: {clave}
                Tipo: {bibliografia[clave]['tipo']}
                Título: {bibliografia[clave]['titulo']}
                Autor: {bibliografia[clave]['autor']['nombre']} {bibliografia[clave]['autor']['apellido']}
                Lugar: {bibliografia[clave]['lugar']}
                Fecha: {bibliografia[clave]['fecha']}
                Periódico: {bibliografia[clave]['periodico']}
                Sección: {bibliografia[clave]['seccion']}
                Url: {bibliografia[clave]['url']}
                ''')

elif 'd' == seleccion:
    print()
    print('LISTA DE VIDEOS DE YOUTUBE')
    print()
    for clave in bibliografia:
        if 'youtube' in bibliografia[clave]['tipo'].lower():
            print(f'''
                Identificador: {clave}
                Tipo: {bibliografia[clave]['tipo']}
                Título: {bibliografia[clave]['titulo']}
                Autor: {bibliografia[clave]['autor']['nombre']} {bibliografia[clave]['autor']['apellido']}
                Fecha: {bibliografia[clave]['fecha']}
                Canal: {bibliografia[clave]['canal']}
                Url: {bibliografia[clave]['url']}
                ''')

print('-------------------------------------------')
print('ACTIVIDAD 6: EJERCICIO 4')
print()

resultado = {}

for clave in bibliografia:
    if 'lugar' in bibliografia[clave].keys() and bibliografia[clave]['lugar'].split(', ')[-1] not in resultado.keys():
        resultado[bibliografia[clave]['lugar'].split(', ')[-1]] = 1
    
    elif 'lugar' in bibliografia[clave].keys() and bibliografia[clave]['lugar'].split(', ')[-1] in resultado.keys():
        resultado[bibliografia[clave]['lugar'].split(', ')[-1]] = resultado[bibliografia[clave]['lugar'].split(', ')[-1]] + 1

print('RESULTADOS')
print()
for pais,veces in resultado.items():
    print(f'{pais}:',veces)
print()