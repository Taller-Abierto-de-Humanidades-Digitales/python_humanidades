##-------------------------------------------------------------------------------
# Módulo con diferentes funciones para las busquedas

# Función buscador en biblioteca por título
def busquedortitulo(tipodocumento: str, cadenaclave:str, biblioteca:list) -> list:
    resultadobusqueda = []

    if tipodocumento != 'todo':
        for elemento in biblioteca:
            if elemento['type'] in tipodocumento and cadenaclave.lower() in elemento['title'].lower():
                resultadobusqueda.append(int(biblioteca.index(elemento)))
    else:
        for elemento in biblioteca:
            if cadenaclave.lower() in elemento['title'].lower():
                resultadobusqueda.append(int(biblioteca.index(elemento)))
    return resultadobusqueda


# Función buscador en biblioteca por autor
def busquedorautor (tipodocumento: str, cadenaclave:str, biblioteca:list) -> list:
    resultadobusqueda = []

    if tipodocumento != 'todo':
        for elemento in biblioteca:
            if elemento['type'] in tipodocumento and len(cadenaclave.split(',')) == 2:
                nombre,apellido = cadenaclave.split(',')
                try:
                    for autor in elemento['author']:    
                        if nombre.lower() in autor['given'].lower() and apellido.lower() in autor['family'].lower() and int(biblioteca.index(elemento)) not in resultadobusqueda:
                            resultadobusqueda.append(int(biblioteca.index(elemento)))
                except:
                    continue
            elif elemento['type'] in tipodocumento and len(cadenaclave.split(',')) != 2:
                try:
                    for autor in elemento['author']:
                        autor = ' '.join(valor.lower() for valor in autor.values())
                        if cadenaclave.lower() in autor and int(biblioteca.index(elemento)) not in resultadobusqueda:
                            resultadobusqueda.append(int(biblioteca.index(elemento)))
                except:
                    continue
    else:
        for elemento in biblioteca:
            if len(cadenaclave.split(',')) == 2:
                nombre,apellido = cadenaclave.split(',')
                try:
                    for autor in elemento['author']:    
                        if nombre.lower() in autor['given'].lower() and apellido.lower() in autor['family'].lower() and int(biblioteca.index(elemento)) not in resultadobusqueda:
                            resultadobusqueda.append(int(biblioteca.index(elemento)))
                except:
                    continue
            elif len(cadenaclave.split(',')) != 2:
                try:
                    for autor in elemento['author']:
                        autor = ' '.join(valor.lower() for valor in autor.values())
                        if cadenaclave.lower() in autor and int(biblioteca.index(elemento)) not in resultadobusqueda:
                            resultadobusqueda.append(int(biblioteca.index(elemento)))
                except:
                    continue
    return resultadobusqueda

# Función buscador en biblioteca por fecha
def buscadorfecha(tipodocumento: str, cadenaclave:str, biblioteca:list) -> list:
    resultadobusqueda = []

    if tipodocumento != 'todo':
        if len(cadenaclave.split(',')) == 1:
            for elemento in biblioteca:
                try:
                    if elemento['type'] in tipodocumento and cadenaclave == elemento['issued']['date-parts'][0][0]:
                        resultadobusqueda.append(int(biblioteca.index(elemento)))
                except:
                    continue
        elif len(cadenaclave.split(',')) == 2:
            for elemento in biblioteca:
                try:
                    if elemento['type'] in tipodocumento and len(elemento['issued']['date-parts'][0]) >= 2 and int(cadenaclave.split(',')[0]) == int(elemento['issued']['date-parts'][0][0]) and int(cadenaclave.split(',')[1]) == int(elemento['issued']['date-parts'][0][1]):
                        resultadobusqueda.append(int(biblioteca.index(elemento)))
                except:
                    continue
        elif len(cadenaclave.split(',')) == 3:
            for elemento in biblioteca:
                try:
                    if elemento['type'] in tipodocumento and len(elemento['issued']['date-parts'][0]) == 3 and int(cadenaclave.split(',')[0]) == int(elemento['issued']['date-parts'][0][0]) and int(cadenaclave.split(',')[1]) == int(elemento['issued']['date-parts'][0][1]) and int(cadenaclave.split(',')[2]) == int(elemento['issued']['date-parts'][0][2]):
                        resultadobusqueda.append(int(biblioteca.index(elemento)))
                except:
                    continue

    else:
        if len(cadenaclave.split()) == 1:
            for elemento in biblioteca:
                try:
                    if cadenaclave == elemento['issued']['date-parts'][0][0]:
                        resultadobusqueda.append(int(biblioteca.index(elemento)))
                except:
                    continue
        elif len(cadenaclave.split(',')) == 2:
            for elemento in biblioteca:
                try:
                    if len(elemento['issued']['date-parts'][0]) >= 2 and int(cadenaclave.split(',')[0]) == int(elemento['issued']['date-parts'][0][0]) and int(cadenaclave.split(',')[1]) == int(elemento['issued']['date-parts'][0][1]):
                        resultadobusqueda.append(int(biblioteca.index(elemento)))
                except:
                    continue
        elif len(cadenaclave.split(',')) == 3:
            for elemento in biblioteca:
                try:
                    if len(elemento['issued']['date-parts'][0]) == 3 and int(cadenaclave.split(',')[0]) == int(elemento['issued']['date-parts'][0][0]) and int(cadenaclave.split(',')[1]) == int(elemento['issued']['date-parts'][0][1]) and int(cadenaclave.split(',')[2]) == int(elemento['issued']['date-parts'][0][2]):
                        resultadobusqueda.append(int(biblioteca.index(elemento)))
                except:
                    continue

    return resultadobusqueda    

# Función buscador en biblioteca por palabras clave

def buscadorpalabrasclave(tipodocumento: str, cadenaclave:str, exactitudbusqueda: str, biblioteca:list) -> list:
    resultadobusqueda = []
    list_cadenaclave = (cadenaclave.lower().split(','))
    
    for elemento in biblioteca:
        cadenabusqueda = ''    
        for clave,valor in elemento.items():
            if isinstance(valor, str):
                cadenabusqueda += ' ' + valor
            elif clave == 'author' or clave == 'director' or clave == 'editor' or clave == 'guest' or clave == 'contributor' or clave == 'performer' or clave == 'producer' or clave == 'translator':
                for sujeto in valor:
                    for nombre in sujeto.values():
                        cadenabusqueda += ' ' + nombre

        if tipodocumento != 'todo':
            if elemento['type'] in tipodocumento and exactitudbusqueda == '2':
                for cadena in list_cadenaclave:
                    if cadena.lower() in cadenabusqueda.lower():
                        resultadobusqueda.append(int(biblioteca.index(elemento)))
                        break
            elif elemento['type'] in tipodocumento and exactitudbusqueda == '1':
                list_verificacion = []
                for cadena in list_cadenaclave:
                    if cadena.lower() in cadenabusqueda.lower() and cadena.lower() not in  list_verificacion:
                        list_verificacion.append(cadena.lower())
                list_verificacion.sort()
                list_cadenaclave.sort()
                if list_verificacion == list_cadenaclave:
                    resultadobusqueda.append(int(biblioteca.index(elemento)))        
                
        else:
            if exactitudbusqueda == '2':
                for cadena in list_cadenaclave:
                    if cadena.lower() in cadenabusqueda.lower():
                        resultadobusqueda.append(int(biblioteca.index(elemento)))
                        break
            elif exactitudbusqueda == '1':
                list_verificacion = []
                for cadena in list_cadenaclave:
                    if cadena.lower() in cadenabusqueda.lower() and cadena.lower() not in  list_verificacion:
                        list_verificacion.append(cadena.lower())
                list_verificacion.sort()
                list_cadenaclave.sort()
                if list_verificacion == list_cadenaclave:
                    resultadobusqueda.append(int(biblioteca.index(elemento)))        
    
    return resultadobusqueda

if __name__ == "__main__": 
    from biblioteca import biblioteca
    
    from interfaz import interfaz

    opciondocumento,tipodocumento,opcionbusqueda,cadenaclave,exactitudbusqueda = interfaz()

    resultadobusqueda = buscadorpalabrasclave(tipodocumento,cadenaclave,exactitudbusqueda, biblioteca())

    print(f'Se encontraron {len(resultadobusqueda)}')
    print(resultadobusqueda)
    for indice in resultadobusqueda:
        print(biblioteca()[indice]['title'])