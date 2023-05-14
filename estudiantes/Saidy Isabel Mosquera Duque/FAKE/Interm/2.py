import json
import re

def buscar_datos(archivo, palabra_clave, tipo, coincidencia):
    with open(archivo) as f:
        datos = json.load(f)
    resultados = []
    for d in datos:
        if tipo in d['type']:
            if coincidencia == 'exacta':
                if palabra_clave == d['title'] or palabra_clave in d['authors'] or palabra_clave == d['date'] or palabra_clave in d['keywords']:
                    resultados.append(d)
            else:
                if re.search(palabra_clave, d['title']) or palabra_clave in d['authors'] or re.search(palabra_clave, d['date']) or palabra_clave in d['keywords']:
                    resultados.append(d)
    return resultados

def formatear_resultado(resultados):
    for r in resultados:
        print("Título:", r['title'])
        print("Autor(es):", ', '.join(r['authors']))
        print("Fecha de publicación:", r['date'])
        print("Palabras clave:", ', '.join(r['keywords']))
        print("Tipo de elemento:", r['type'])
        print("-----------------------------------------")



def menu_busqueda():
    archivo = "datos.json"
    palabra_clave = input("Ingrese la palabra clave de búsqueda: ")
    tipo_busqueda = input("Seleccione el tipo de búsqueda (título, autor, fecha o palabra clave): ")
    tipo_elemento = input("Seleccione el tipo de elemento a filtrar (libro, artículo, tesis o cualquier otro tipo de elemento): ")
    coincidencia = input("Seleccione el tipo de coincidencia (exacta o parcial): ")
    resultados = buscar_datos(archivo, palabra_clave, tipo_busqueda, coincidencia)
    resultados_filtrados = []
    for r in resultados:
        if tipo_elemento in r['type']:
            resultados_filtrados.append(r)
    formatear_resultado(resultados_filtrados)
        
        
def menu_busqueda():
    archivo = "datos.json"
    palabra_clave = input("Ingrese la palabra clave de búsqueda: ")
    tipo_busqueda = input("Seleccione el tipo de búsqueda (título, autor, fecha o palabra clave): ")
    tipo_elemento = input("Seleccione el tipo de elemento a filtrar (libro, artículo, tesis o cualquier otro tipo de elemento): ")
    coincidencia = input("Seleccione el tipo de coincidencia (exacta o parcial): ")
    resultados = buscar_datos(archivo, palabra_clave, tipo_busqueda, coincidencia)
    resultados_filtrados = []
    for r in resultados:
        if tipo_elemento in r['type']:
            resultados_filtrados.append(r)
    formatear_resultado(resultados_filtrados)