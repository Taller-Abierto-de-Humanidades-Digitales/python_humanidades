bibliografia = {'000': {'tipo': '', 'autor': [{'nombre': '', 'apellido': ''}], 'titulo': '', 'editorial': '', 'fecha': 0, 'lugar': ''}, '001': {'tipo': 'novela', 'autor': [{'nombre': 'Fiodor', 'apellido': 'Dostoyenvski'}], 'titulo': 'El jugador', 'editorial': 'Alianza editorial', 'fecha': '1886', 'lugar': 'Rusia'}, '002': {'tipo': 'novela', 'autor': [{'nombre': 'Simone', 'apellido': 'deBeauvoir'}], 'titulo': 'Sangre de los otros', 'editorial': 'Seix Barral', 'fecha': '1944', 'lugar': 'Francia'}, '003': {'tipo': 'novela', 'autor': [{'nombre': 'Albert', 'apellido': 'Camus'}], 'titulo': 'El extrajenro', 'editorial': 'Éditions Gallimard', 'fecha': '1942', 'lugar': 'Francia'}, '004': {'tipo': 'novela', 'autor': [{'nombre': 'Jean-Paul', 'apellido': 'Sartre'}], 'titulo': 'La Naúsea', 'editorial': 'Éditions Gallimard', 'fecha': '1938', 'lugar': 'Francia'}, 
'005': {'tipo': 'novela', 'autor': [{'nombre': 'Franz', 'apellido': 'Kafka'}], 'titulo': 'La Metaformosis', 'editorial': 'Kurt Wolff Verlag', 'fecha': '1915', 'lugar': 'Alemania'}, '006': {'fecha': '24.02.2023', 'periodico': [{'nombre': 'Noticias', 'apellido': 'DW'}], 'titulo': 'Los Grammy Latinos se entregarán en España en 2023', 'seccion': 'cultura', 'url': 'https://p.dw.com/p/4Nxh4'}, '007': {'revista': 'Journal of Open Humanities Data', 'autor': [{'nombre': 'Mei-Shin', 'apellido': 'Wu'}], 'titulo': 'Computer-Assisted Language Comparison: State of the Art', 'volumen': '6', 'fecha': '2020', 'numero': '2', 'url': 'https://doi.org/10.5334/johd.12 '}, '008': {'canal': [{'nombre': 'Darin', 'apellido': 'McNabb'}], 'titulo': 'El existencialismo: una introducción 1/2', 'fecha': '2013', 'url': 'https://www.youtube.com/watch?v=JotchOUEdfk'}}


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
