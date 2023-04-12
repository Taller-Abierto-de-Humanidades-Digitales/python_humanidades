# igualdad 

"""perro = "firulais"
gato = "salem"
pez = "nemo"
print(perro == gato)

# desigualdad 


print(perro != pez)"""


# mayor que y manor que 

"""print(5 > 3)
print(5 < 3)"""


"""for i in range(0, 10):
  print(i, i >= 5)


from random import randint

numero = randint(1, 100)

print(numero)
#print(numero <= 50 and numero >= 25)

print(numero <= 50 or numero >= 25)"""

"""perro = "firulais"
gato = "salem"

print(perro != "firulais" and gato == "salem")"""
# operadores de pertenencia 

"""perro = "firulais"

Lista_perros = ["firulais", "snoppy", "scooby doo", "lukanikos"]

print(perro not in Lista_perros)
"""

# operadores de pertenencia con caracteres de caracteres 

"""s= "hola mi nombre es Isabel"

print("Isabel"  not in s)"""

# sentencia if, elif, else


if 5 < 3:
    print("5 es mayor que 3")




    ###### SEMANA 6

    

    print("Listado de bibliografica".upper())
for clave, valor in bibliografia.items():
        print(f"""
        Identificador: {clave}
        Título: {valor["titulo"]}
        Autor: {valor["autor"][0]["apellido"]}, {valor["autor"][0]["nombre"]}
        Editorial: {valor["Publisher"]}
        Lugar: {valor["lugar"]}
        Fecha: {valor["fecha"]}
        Número: {valor["numero"]}
        Url: {valor["url"]}
        """)





##### el print para la revistas 
# 
print("Listado de referencias".upper())
for clave, valor in bibliografia.items():
        print(f"""
        Identificador: {clave}
        Tipo: {valor["tipo"]}
        Título: {valor["titulo"]}
        Autor: {valor["autor"][0]["nombre"]}, {valor["autor"][0]["apellido"]}
        Editorial: {valor["Publisher"]}
        Revista: {valor["revista"]}
        Lugar: {valor["lugar"]}
        Fecha: {valor["fecha"]}
        Número: {valor["numero"]}
        Url: {valor["url"]}
        """)
        




         print(f"""
        Identificador: {clave}
        Título: {valor["titulo"]}
        fecha: {valor["fecha"]}
        Revista: {valor["revista"]}

        """)



##### ejercicio 2 prints 

for clave, valor in bibliografia.items():
     if valor["tipo"] == "Artículos academicos":
           print(f"""
        Identificador: {clave}
        Tipo: {valor["tipo"]}
        Título: {valor["titulo"]}
        Autor: {valor["autor"][0]["nombre"]}, {valor["autor"][0]["apellido"]}
        Editorial: {valor["Publisher"]}
        Url: {valor["url"]}
        """)

for clave, valor in bibliografia.items():
     if valor["tipo"] == "video":
          print(f"""
        Identificador: {clave}
        Tipo: {valor["tipo"]}
        Título: {valor["titulo"]}
        Canal: {valor["canal"]}
        Url: {valor["url"]}
        """)
         

         