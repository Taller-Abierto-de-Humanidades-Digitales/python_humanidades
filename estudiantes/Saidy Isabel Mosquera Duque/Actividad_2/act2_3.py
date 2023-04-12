# Ejercicio 3: Manipulación de cadenas de texto

frase = " He decidido apostar por el amor. El odio es una carga demasiado pesada. 'Martin Luther King, Jr.' "

frase2 = " he decidiDo apostar por el AMOR. el ODIO es una carga demasiado pesada. 'martin Luther King, Jr.' "

print(f"Esta es la frase en mayusculas: {frase.upper()}")

print(f"Esta es la frase en minúsculas: {frase.lower()}")


print(f"Esta es la frase con la primera letra de la frase en mayúscula:{frase2.capitalize()}")

print(f"esta es la frase con la primera letra de la frase en mayúscula:{frase.capitalize()}")


print(f"Esta es la frase con la primera letra de cada palabra en mayúscul:{frase.title()}")

print(f"Esta es la frase con todas las letras de la frase en mayúsculas y minúsculas:{frase.swapcase()}")

# PRUEBA CON ALGUNAS MODIFICACIONES EN LA VARIABLE (frase2) : print(f"Esta es la frase con todas las letras de la frase en mayúsculas y minúsculas:{frase2.swapcase()}")

# Remplazar

""" Hola, Jairo. Un para de interrogantes que Pregunta: porque no quita las '' (comillas simples) cuando le ejecuto remplazar.
 Sin embargo, no me muestra ningún error en el proceso. Algo similar me sucedió al ejecutar (capitalize())
"""

print(frase.replace(".","") .replace(",","") .replace(" '' ", ""))

print(f'Esta es la frase remplazando los puntos por @: {frase.replace(".","@")}')

print(frase.split())

print(f"Esta es la frase dividida en plabras: {frase. split()}")