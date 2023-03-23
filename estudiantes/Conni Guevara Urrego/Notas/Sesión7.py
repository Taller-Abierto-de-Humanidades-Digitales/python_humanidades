##Funciones: Introducción - Marzo 07

""" def saludar(nombre):
    print(f"Hola {nombre}, ¿qué tal la vida?")

nombres = ["Juan", "Camila", "Antonio"]

saludar(nombres) """

def saludar(nombre, nacimiento, lugar_nacimiento="Colombia"):
    """Saludar a una persona y decirle su edad

    Parámetros
    ----------

    nombre: str
        Nombre de la persona a saludar
    nacimiento: int
        Año de nacimiento de la persona (AAAA)
    lugar_nacimiento: str
        País de nacimiento de la persona
        default: Colombia
"""
    print(f"Hola {nombre}. Tienes {2023 - int(nacimiento)} años, y naciste en {lugar_nacimiento}")

nombre = input("Ingresa tu nombre: ")

try:
    fecha_nacimiento = int(input("Ingresa tu año de nacimiento: "))
except ValueError:
    print("La fecha de nacimiento es incorrecta. Asegurate que es el año completo (AAAA)")
    fecha_nacimiento = int(input("Ingresa tu año de nacimiento: "))
    saludar(nombre, fecha_nacimiento)
except:
    raise


