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