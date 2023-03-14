##El cuarto ejercicio consiste en escribir un programa que tome una frase y aplique los siguientes operadores:

##+: Concatena dos cadenas de texto

texto1 = "Bello puerto del mar mi Buenaventura,"
print(texto1)

texto2 = "donde se aspira siempre la brisa pura"
print(texto2)

print(texto1 + " " + texto2)

##*: Repite una cadena de texto un número de veces

texto3 = "Aguacero e mayo dejalo caer"
print(texto3)

print(texto3*10)

##in: Verifica si una cadena de texto está contenida en otra

lista_texto4 = ["Toda",  "buena", "novela", "es", "una", "adivinanza", "del", "futuro"]
print(lista_texto4)
print("adivinanza" in lista_texto4)
print("novelon" in lista_texto4)

##not in: Verifica si una cadena de texto no está contenida en otra

print("correr" not in lista_texto4)
print("buena" not in lista_texto4)

##==: Verifica si dos cadenas de texto son iguales

lista_texto5 = ["Lo", "que", "el", "alma", "hace", "por", "su" "cuerpo", "es", "lo", "que", "el", "artista", "hace", "por", "su", "pueblo"]
print(lista_texto5)

print(lista_texto4 == lista_texto5)

lista_texto6 = ["por", "por", "el", "alma", "hace", "Lo", "es" "cuerpo", "su", "que", "el", "lo", "artista", "hace", "que", "su", "pueblo"]
print(lista_texto6)

print(lista_texto5 == lista_texto6)

##!=: Verifica si dos cadenas de texto son diferentes

print(lista_texto4 != lista_texto6)

##Cada operador debe ser aplicado a la frase e imprimirla usando format(). Por ejemplo, si la frase es hola mundo, el programa debe imprimir: """