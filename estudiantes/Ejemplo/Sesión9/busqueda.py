from biblioteca import busqueda_simple

def menu():
    print("1. Buscar por título")
    print("2. Buscar por autor")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")
    return opcion


def main():
    opcion = menu()
    while opcion != "3":
        if opcion == "1":
            titulo = input("Ingrese el título: ")
            busqueda_simple("titulo", titulo)
        elif opcion == "2":
            autor = input("Ingrese el autor: ")
            try:
                busqueda_simple("autor", autor)
            except TypeError:
                print("No se encontraron resultados")
        else:
            print("opción inválida")
        opcion = menu()


if __name__ == "__main__":
    main()