# Ensamble módulos y ejecutable
from biblioteca import biblioteca
biblioteca = biblioteca()

from interfaz import interfaz

from buscador import busquedortitulo,busquedorautor,buscadorfecha,buscadorpalabrasclave

from formato import formatobusqueda, impreresultados

print()
print(':: BIENVENIDO AL BUSCADOR BIBLIOGRÁFICO')
print('Ingrese los datos de la búsqueda')

inicio = True
while inicio:

    opciondocumento,tipodocumento,opcionbusqueda,cadenaclave,exactitudbusqueda = interfaz()

    resultadobusqueda = []

    if opcionbusqueda == '1':
        resultadobusqueda = busquedortitulo(tipodocumento,cadenaclave,biblioteca)
    elif opcionbusqueda == '2':
        resultadobusqueda = busquedorautor(tipodocumento,cadenaclave,biblioteca)
    elif opcionbusqueda == '3':
        resultadobusqueda = buscadorfecha(tipodocumento,cadenaclave,biblioteca)
    elif opcionbusqueda == '4':
        resultadobusqueda = buscadorpalabrasclave(tipodocumento,cadenaclave,exactitudbusqueda,biblioteca)

    impreresultados(formatobusqueda(biblioteca,resultadobusqueda))

    retorno = input("Tecleé [1] para repetir la busqueda ó [2] para salir:  ")
    
    salida = True
    while salida:
        if retorno == '1':
            salida = False
        elif retorno == '2':
            print('Seleccionó [2] salir')
            salida = False
            inicio = False
        else:  
            print("Selección errada, intente de nuevo.")     