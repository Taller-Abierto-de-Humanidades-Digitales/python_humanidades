bibliografia = {'000': {'tipo': '', 'autor': [{'nombre': '', 'apellido': ''}], 'titulo': '', 'editorial': '', 'fecha': 0, 'lugar': ''}, '001': {'tipo': 'novela', 'autor': [{'nombre': 'Fiodor', 'apellido': 'Dostoyenvski'}], 'titulo': 'El jugador', 'editorial': 'Alianza editorial', 'fecha': '1886', 'lugar': 'Rusia'}, '002': {'tipo': 'novela', 'autor': [{'nombre': 'Simone', 'apellido': 'de-Beauvoir'}], 'titulo': 'Sangre de los otros', 'editorial': 'Seix Barral', 'fecha': '1944', 'lugar': 'Francia'}, '003': {'tipo': 'novela', 'autor': [{'nombre': 'Albert', 'apellido': 'Camus'}], 'titulo': 'El extrajenro', 'editorial': 'Éditions Gallimard', 'fecha': '1942', 'lugar': 'Francia'}, '004': {'tipo': 'novela', 'autor': [{'nombre': 'Jean-Paul', 'apellido': 'Sartre'}], 'titulo': 'La Naúsea', 'editorial': 'Éditions Gallimard', 'fecha': '1938', 'lugar': 'Francia'}, '005': {'tipo': 'novela', 'autor': [{'nombre': 'Franz', 'apellido': 'Kafka'}], 'titulo': 'La Metaformosis', 'editorial': 'Kurt Wolff Verlag', 'fecha': '1915', 'lugar': 'Alemania'}, '006': {'fecha': '25.02.2023', 'periodico': [{'nombre': 'Noticias', 'apellido': 'DW'}], 'titulo': 'Documental francés gana el Oso de Oro en la Berlinale', 'seccion': 'cultura', 'url': 'https://p.dw.com/p/4NzKy', 'tipo': 'periódico'}, '007': 
{'fecha': '24.02.2023', 'periodico': [{'nombre': 'Noticias', 'apellido': 'DW'}], 'titulo': 'Los Grammy Latinos se entregarán en España en 2023', 'seccion': 'cultura', 'url': 'https://p.dw.com/p/4Nxh4', 'tipo': 'periódico'}, '008': {'revista': 'Journal of Open Humanities Data', 'autor': [{'nombre': 'Vincent', 'apellido': 'Ducatteeuw'}], 'titulo': 'Critical Reflections on Cinema Belgica: The Database for New Cinema History in Belgium', 'volumen': '9', 'fecha': '2023', 'numero': '1', 'url': 'https://doi.org/10.5334/johd.91', 'tipo': 'Articulo academico'}, '009': {'revista': 'Journal of Open Humanities Data', 'autor': [{'nombre': 'Li', 'apellido': 'Nguyen'}], 'titulo': 'Automatic Language Identification in Code-Switched Hindi-English Social Media Text', 'volumen': '7', 'fecha': '2021', 'numero': '7', 'url': 'https://doi.org/10.5334/johd.44 ', 'tipo': 'Articulo academico'}, '010': {'revista': 'Journal of Open Humanities Data', 'autor': [{'nombre': 'Mei-Shin', 'apellido': 'Wu'}], 'titulo': 'Computer-Assisted Language Comparison: State of the Art', 'volumen': '6', 'fecha': '2020', 'numero': '2', 'url': 'https://doi.org/10.5334/johd.12 ', 'tipo': 'Articulo académico'}, '011': {'canal': [{'nombre': 'Darin', 'apellido': 'McNabb'}], 'titulo': 'El existencialismo: una introducción 1/2', 'fecha': '2013', 'url': 'https://www.youtube.com/watch?v=JotchOUEdfk', 'tipo': 'video'}}

#ejercicio 1

def buscar():
    """buscador por título a través de carácteres"""
     
    """parametros (argumentos)
    --------
    - Imput busca palabra en catálogo
    - palabra debe ser guardada en variable palabra
    - la función busca entre palabras mayúsuculas y mininúsculas
    - Se muestra mensaje si no ve coincidencia
    """

palabra = input('¿Cuál es la palabra que desea buscar?: ')
resultado_completo = []
resultado_similar = []
resultado_diferente = []

for lib in bibliografia:
            palabras_claves = bibliografia[lib]['titulo'].split(" ")
            for caracteres in palabras_claves:
                if palabra.lower() == caracteres.lower():
                    resultado_completo.append(bibliografia[lib]['titulo'])
                    
        
for lib in bibliografia:
            if palabra.lower() in bibliografia[lib]['titulo'].lower():
                resultado_similar.append(bibliografia[lib]['titulo'])
        
for lib in resultado_similar:
            if lib not in resultado_completo:
                resultado_diferente.append(lib)
if len(resultado_completo) > 0:
    print(f'para tu búsqueda, se encontraron {len(resultado_completo)} títulos que incluyen la palabra "el{palabra}":')
    
for lib1 in resultado_completo:
                print(f'- {lib1}')
        
if len(resultado_diferente) > 0:
    print(f'para tu búsqueda se encontraron {len(resultado_diferente)} títulos que contienen los caracteres "{palabra}":')
    for lib1 in resultado_diferente:
                print(f'- {lib1}')
elif len(resultado_completo) == 0:
                print(f'No se encontraron elementos que incluyan la palabra "{palabra}".')

#ejercicio 2


def buscador(titulos: str, año: int):
        """"Esta función busca por año y titulo un libro del diccionario

        parámetros
        ----------------
        titulos: str
        tiene el título de los textos
        
        año: int
        Año de publicaciones de los textos

        """
        
palabras = input ('ponga una palabra clave del título que desea encontrar: ')
resultado_completado = []
resultado_similarizado = []
resultado_diferenciado = []


for libs in bibliografia:
                palabras_clavesss = bibliografia[libs]['titulo'].split(" ")
                for caracteresss in palabras_clavesss:
                    if palabras.lower() == caracteresss.lower():
                        resultado_completado.append(bibliografia[libs]['titulo'])
                        
            
for libs in bibliografia:
                if palabras.lower() in bibliografia[libs]['titulo'].lower():
                    resultado_similarizado.append(bibliografia[libs]['titulo'])

for libs in resultado_similar:
                if libs not in resultado_completado:
                    resultado_diferenciado.append(libs)
if len(resultado_completado) > 0:
        
        print(f'para tu búsqueda, se encontraron {len(resultado_completado)} títulos que incluyen la palabra "el{palabras}":')


for lib2 in resultado_completado:
                    print(f'- {lib2}')

                
            
if len(resultado_diferenciado) > 0:
        print(f'para tu búsqueda se encontraron {len(resultado_diferenciado)} títulos que contienen los caracteres "{palabras}":')
        for lib2 in resultado_diferenciado:
                    print(f'- {lib2}')


                    
elif len(resultado_completado) == 0:
                    print(f'No se encontraron títulos que incluyan la palabra "{palabras}".')




#ejercicio 3

def añadir(catalogo__):
     elemento1 = input("Ponga el tipo de elemento que desea agregar al diccionario. Recuerde que el tipo de texto es una categoría que demuestra una característica del texto, por ejemplo, es una novela, perioódico o articulo academico. Recuerde escribir cuál es el tipo de texto conservando las tíldes de la oración anterior: ")
     elemtentos  = [catalogo__[x]['tipo'].lower() for x in catalogo__]
     listatipo = list(set(elemtentos))
     elemento = {}
     if elemento1.lower() in listatipo:
            for lib3 in catalogo__:
                 if catalogo__[lib3]['tipo'].lower()== elemento1.lower():
                    lista=list(catalogo__[lib3].keys())
                    extension=len(lista)
                    break
            indicador = int(list(catalogo__.keys())[-1]) + 1
            indicador = str(indicador).zfill(3)
            for lib4 in range(extension-1):                 
                 elemento[lista[lib4+1]]=input(f"Ingrese {lista[lib4+1]}:")
            catalogo__[indicador] = elemento
            print("Muy bien, ya agregó un elemento al catálogo.")
     else:
          print("no es posible ingresar este tipo. ")       
                 
añadir(bibliografia)

print(bibliografia)




