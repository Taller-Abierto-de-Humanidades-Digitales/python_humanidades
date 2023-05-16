from busqueda_2_intento import *
from biblioteca import biblioteca



def menu():
    print("1. Buscar por título")
    print("2. Buscar por autor")
    print("3. Buscar por fecha")
    print("4. Buscar por palabra clave")
    print("5. Salir")
    opcion = input("Ingrese una opción: ")
    return opcion

#########IMPLEMENTAR MENU DE SALIDA???############

def main():
    opcion = menu()
    while opcion != "5":
        if opcion == "1":
            titulo = input("Ingrese el título: ")
            biblio= biblioteca()
            tipoo= input(("Ingrese el tipo de texto: "))
            rta=buscatitulo(tipoo, titulo, biblio)
            if rta==[]:
                print('\n\n No hay titulos que correspondan con la busqueda')
            print(formateador(rta))
            #break
        elif opcion == "2":
            input_autor = input("Ingrese el autor: ")
            tipo = input("Ingrese el tipo de texto: ")
            resp=(busqueda(input_autor, 'author', tipo))
            if resp== []:
                print('\n\n No hay autores que correspondan con la busqueda')
            print(formateador(resp))

        elif opcion == "3":
            fecha= input("ingrese la fecha que desea buscar: ")
            tip = input("Ingrese el tipo de texto que desea buscar: ")
            biblio= biblioteca()
            respues= (busqueda(fecha, "issued", tip))
            if respues== []:
                print('\n\n No hay elementos que correspondan con la busqueda')
            print(formateador(respues))
           
        elif opcion == "4":
            palabra_clave = input("Ingrese la palabra clave que desea buscar: ")
            tipp = input("Ingrese el tipo de texto que desea buscar: ")
            respuesta= (busqueda(palabra_clave, "title", tipp))
            if respuesta == []:
                print('\n\n No hay elementos que correspondan con la busqueda')
            print(formateador(respuesta))
        else:
            print("opción inválida")
        opcion = menu()
    pass

if __name__ == "__main__":
    main()

