# For loops

países = ['Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Guyana', 'Perú']

for país in países: 
    print(país)

for país in países: 
    print(país)

print('Son países sudamericanos')

#secuencia = [ 1, 2, 3, 4, 5, 6,]

for numero in range (1,7):
    print(numero)

for numero in range (2,30,8):
    print(numero)

#se le pone un numero mas pues cuenta el cero como numero 
#no olvidar los dos puntos al final 

#llenar listas con loops 

secuencia = []
for numero in range(2, 100, 5):
    secuencia.append(numero)

print(secuencia)

iniciales = []
finales = []
longitud = []
for pais in países: 
    iniciales.append(pais[0])
    finales.append(pais[-1])
    longitud.append(len(pais))

print(iniciales,finales, longitud)
promedio = sum(longitud) / len(países)
print (f"los nombres tienen en promedio {round(promedio,2)} caracteres.")

#loops anidados
frase = "Era la estación de las lluvias en Bangkok".split()

for palabra in frase: 
    print (palabra)

for palabra in frase: 
    for letra in palabra: 
    print (letra , end=' ')

