import json

# Cargar datos de un archivo CSL-JSON
with open('datos.json') as f:
    datos = json.load(f)

# Función para buscar elementos que coinciden con los criterios de búsqueda
def buscar_elementos(titulo=None, autor=None, anio=None, palabras_clave=None, tipo=None, coincidencia_exacta=False):
    resultados = []
    for elemento in datos:
        # Comprobar si el elemento cumple con el tipo de elemento deseado
        if tipo is not None and elemento['type'] != tipo:
            continue
        # Comprobar si el título coincide con el criterio de búsqueda
        if titulo is not None:
            if coincidencia_exacta:
                if elemento.get('title') != titulo:
                    continue
            else:
                if titulo.lower() not in elemento.get('title').lower():
                    continue
        # Comprobar si el autor coincide con el criterio de búsqueda
        if autor is not None:
            if coincidencia_exacta:
                if autor not in [a.get('family') for a in elemento.get('author', [])]:
                    continue
            else:
                if not any(autor.lower() in a.get('family', '').lower() for a in elemento.get('author', [])):
                    continue
        # Comprobar si el año de publicación coincide con el criterio de búsqueda
        if anio is not None:
            if coincidencia_exacta:
                if elemento.get('issued', {}).get('date-parts', [[]])[0][0] != anio:
                    continue
            else:
                if str(anio) not in ''.join(str(p) for p in elemento.get('issued', {}).get('date-parts', [[]])[0]):
                    continue
        # Comprobar si alguna palabra clave coincide con el criterio de búsqueda
        if palabras_clave is not None:
            if coincidencia_exacta:
                if not any(p in elemento.get('keyword', []) for p in palabras_clave):
                    continue
            else:
                if not any(p.lower() in ''.join(elemento.get('keyword', [])).lower() for p in palabras_clave):
                    continue
        # Si el elemento cumple con todos los criterios de búsqueda, agregarlo a los resultados
        resultados.append(elemento)
    return resultados

# Función para formatear los resultados de la búsqueda
def formatear_resultados(resultados):
    for elemento in resultados:
        print('---')
        print(f'Título: {elemento.get("title")}')
        autores = ', '.join([f"{a.get('family', '')}, {a.get('given', '')}" for a in elemento.get('author', [])])
        print(f'Autor(es): {autores}')
        anio = elemento.get('issued', {}).get('date-parts', [[]])[0][0]
        print(f'Año de publicación: {anio}')
        palabras_clave = ', '.join(elemento.get('keyword', []))
        print(f'Palabras clave: {palabras_clave}')

# Ejemplo de uso
resultados = buscar_elementos(titulo='Redes neuronales', tipo='article', coincidencia_exacta=True)
formatear_resultados(resultados)