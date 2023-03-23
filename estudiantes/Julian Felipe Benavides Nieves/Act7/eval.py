from Act7_JulianBenavides import busquedapalabra, bus_anio_palabra, entradabiblio

def main():
    # Entrada de datos
    biblio = entradabiblio()
    # Busqueda de palabras
    busquedapalabra(biblio)
    # Busqueda de año y palabra
    bus_anio_palabra(biblio)

if __name__ == '__main__':
    main()