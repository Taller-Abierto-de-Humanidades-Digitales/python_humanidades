# Modulo para formatear e impresión de los resultados

def formatobusqueda(biblioteca:list, resultadobusqueda:list)->list:
    formatoresultados = []
    for indice in resultadobusqueda:
        referencia = ''
        for clave, valor in biblioteca[indice].items():
            if clave == 'id':
                referencia += f'{clave}: {valor}\n'
            elif clave == 'title':
                referencia += f'{clave}: {valor}\n'
        for clave, valor in biblioteca[indice].items():
            if clave != 'title' and clave != 'id':
                referencia += f'{clave}: {valor}\n'
        formatoresultados.append(referencia)
    return formatoresultados

def impreresultados (formatoresultados:list):    
    print(f'\nSe encontraron {len(formatoresultados)} resultado(s).\n')
    contador = 0
    for referencia in formatoresultados:
        contador += 1
        print(f'[{contador}]--------------------------------------------------')
        print(referencia,'\n')
    print('------------------------------------------')
    print(f'\nSe encontraron {len(formatoresultados)} resultado(s).\n')

# if __name__ == "__main__": 
#     from biblioteca import biblioteca
#     biblioteca = biblioteca()
#     resultadobusqueda = [9, 14, 144, 173, 306, 479, 705, 737]
#     impreresultados(formatobusqueda(biblioteca,resultadobusqueda))
        



