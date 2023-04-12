# Modulo de intefaz con el usuario

def interfaz() -> tuple:
    """
    Pide al usuario la información para la busqueda en el catálogo

    Parámetros
    ----------
    No tiene parámetros de entrada.
    
    Retorno
    -------
    opciondocumento: string
        Número entre 1 y 4 que define el tipo de documentos a buscar
    tipodocumento: string
        cadena con el tipo de documento según selección
    opcionbusqueda: string
        Número entre 1 y 4 que define el tipo de busqueda a realizar
    cadenaclave: string
        Cadenas de caracteres con los elementos a buscar
    exactitudbusqueda: string
        Definición de la exactitud de la busqueda para palabras claves
    """
    exactitudbusqueda = ' '

    errorselecc = True
    while errorselecc:
        opciondocumento = input('''
                        Tipeé el tipo de busqueda a realizar (# + enter):
                        [1] Libro, [2] Artículo, [3] Tesis, [4] Cualquiera
                        ''')
        if opciondocumento.strip() == "":
            print("Error: Debe ingresar un valor. Intente de nuevo.")
            # continue
        elif int(opciondocumento) >= 1 and int(opciondocumento) <= 4:
            if opciondocumento == "1":
                print('Seleccionó la opción para [2] Artículo')
                tipodocumento = 'book'
            elif opciondocumento == "2":
                tipodocumento = 'article-journal, article-magazine, article-newspaper'
            elif opciondocumento == "3":
                tipodocumento = 'thesis'
            elif opciondocumento == "4":
                tipodocumento = 'todo'
            print(f'Seleccionó la opción {opciondocumento}. {tipodocumento}')
            errorselecc = False
        else:
            print("Selección errada, intente de nuevo.")

    errorselecc = True
    while errorselecc:
        opcionbusqueda = input('''
                            Tipeé el número del tipo de busqueda a realizar:
                            [1] Título, [2] Autor, [3] Fecha, [4] Palabra clave
                            ''')
        if opcionbusqueda == "1":
            print('Seleccionó la opción para [1] Título')
            cadenaclave = input('Escriba el título del libro o palabras claves para su busqueda: ')
            print(f'\nBuscando el título "{cadenaclave}" en {tipodocumento}...')
            errorselecc = False
        elif opcionbusqueda == "2":
            print('Seleccionó la opción para [2] Autor')
            cadenaclave = input("""
            Escriba la palabra clave para el autor. 
            Para una busqueda más precisa escriba el nombre y el apellido separados por "coma" sin espacios (ej.: nombre,apellido): """)
            print(f'\nBuscando el autor "{cadenaclave}" en {tipodocumento}...')
            errorselecc = False
        elif opcionbusqueda == "3":
            print('Seleccionó la opción para [3] Fecha')
            cadenaclave = input("""
            Escriba el año de publicación. 
            Para una busqueda más precisa escriba la fecha separada por "comas" (ej.: AAAA,MM ó AAAA,MM,DD): """)
            print(f'\nBuscando la fecha "{cadenaclave}" en {tipodocumento}...')
            errorselecc = False
        elif opcionbusqueda == "4":
            print('Seleccionó la opción para [4] Palabra clave')
            cadenaclave = input("""
            Escriba palabras claves separadas por "comas" (ej.: palabra1,palabra2,palabra3...): """)
            errorseleccexactitud = True
            while errorseleccexactitud:
                exactitudbusqueda = input("""
                Seleccione presición de la busqueda. [1] contiene todas las palabras (and), [2] contiene alguna de las palabra (or):  """)
                if exactitudbusqueda == '1':
                    print('Seleccionó [1] contiene todas las palabras (and) ')
                    errorseleccexactitud = False
                elif exactitudbusqueda == '2':
                    print('Seleccionó [2] contiene alguna de las palabra (or)')
                    errorseleccexactitud = False
                else:  
                    print("Selección errada, intente de nuevo.")        
            print(f'\nBuscando las palabras "{cadenaclave}" en {tipodocumento}...')
            errorselecc = False
        else:
            print("Selección errada, intente de nuevo.")
    return opciondocumento, tipodocumento, opcionbusqueda, cadenaclave, exactitudbusqueda

if __name__ == "__main__":
    print(interfaz())