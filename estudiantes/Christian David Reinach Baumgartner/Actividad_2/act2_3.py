#Ejercicio 3
# El tercer ejercicio consiste en un programa que toma una frase y aplica ciertas funciones.

frase= "Hosszú távon a kutya végül elkötelezi magát a macska mellett"
fraseespaciada= " Hosszú távon a kutya végül elkötelezi magát a macska mellett " #Frase con espacios al inicio y al final
#La frase en español es "A la larga, el perro se acaba comprometiendo con el gato"


print(f'La frase en minúsculas es "{frase.lower()}". \n La frase en mayúsculas es "{frase.upper()}". \
     \n La frase con su primera letra en mayúscula es "{frase.capitalize()}". \
     \n La frase con cada palabra iniciada en mayúscula es "{frase.title()}". \
     \n La frase con las minúsculas en mayúsculas y las mayúsculas en minúsculas es "{frase.swapcase()}". \
     \n La frase con espacios al inicio y final es "{fraseespaciada}" y sin tales es "{fraseespaciada.strip()}". \
     \n La frase con la palabra "kutya" reemplazada por "kacsa" es "{frase.replace("kutya", "kacsa")}".\
     \n La frase dividida en palabras es {frase.split()}.')


 