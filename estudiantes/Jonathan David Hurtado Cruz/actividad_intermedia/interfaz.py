from busqueda_2_intento import busqueda 
from busqueda_2_intento import buscatitulo
from biblioteca import biblioteca

def menu():
    print("1. Buscar por título")
    print("2. Buscar por autor")
    print("3. Buscar por tipo de texto")
    print("4. Salir")
    opcion = input("Ingrese una opción: ")
    return opcion


def main():
    opcion = menu()
    while opcion != "4":
        if opcion == "1":
            titulo = input("Ingrese el título: ")
            biblio= biblioteca()
            buscatitulo("article-journal", titulo, biblio)
        elif opcion == "2":
            autor = input("Ingrese el autor: ")
            tipo = input("Ingrese el tipo de texto: ")
            palabra = input("Ingrese la palabra clave para buscar: ")
            try:
                busqueda(palabra, autor, tipo) 
                
            except TypeError:
                print("No se encontraron resultados")
        elif opcion == "3":
            tipo = input("Ingrese el tipo de texto que desea buscar: ")
            biblio= biblioteca()
            try:
                busqueda(palabra, autor, tipo) 
            except TypeError:
                print("No se encontraron resultados")
        else:
            print("opción inválida")
        opcion = menu()


if __name__ == "__main__":
    main()