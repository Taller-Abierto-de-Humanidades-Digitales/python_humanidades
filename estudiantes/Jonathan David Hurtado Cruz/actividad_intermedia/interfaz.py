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

#########IMPLEMENTAR MENU DE SALIDA############

def main():
    opcion = menu()
    while opcion != "5":
        if opcion == "1":
            titulo = input("Ingrese el título: ")
            #######AGREGAR TIPO TEXTO##########
            biblio= biblioteca()
            rta=buscatitulo("article-journal", titulo, biblio)
            if rta==[]:
                print('\n\n No hay titulos que correspondan con la busqueda')
            print(formateador(rta))
            #break
        elif opcion == "2":
            input_autor = input("Ingrese el autor: ")
            tipo = input("Ingrese el tipo de texto: ")
            print(input_autor)
            try:
                print(formateador(busqueda(input_autor, 'author', tipo)))
              
            except TypeError:
                print("No se encontraron resultados")######<------ cambiar por un if que diga cuando hay error
        elif opcion == "3":
            tip = input("Ingrese el tipo de texto que desea buscar: ")
            biblio= biblioteca()
            fecha= input("ingrese la fecha que sea buscar: ")
            autorr = input("Ingrese el autor: ")
            try:
                busqueda(fecha, autorr, tip) 
            except TypeError:
                print("No se encontraron resultados")

        elif opcion == "4":
            palabra_clave = input("Ingrese la palabra clave que desea buscar: ")
            tipp = input("Ingrese el tipo de texto que desea buscar: ")
            autorrr = input("Ingrese el autor que desea buscar: ")
            try:
                busqueda(palabra_clave, autorrr, tipp) 
            except TypeError:
                print("No se encontraron resultados")
           
        else:
            print("opción inválida")
        opcion = menu()
    pass

if __name__ == "__main__":
    main()

