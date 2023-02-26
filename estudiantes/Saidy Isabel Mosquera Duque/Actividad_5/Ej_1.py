# Ejercicio 1  
libros = ["Harry Potter y la piedra filosofal; J. K. Rowling; 1997; Ficción", "Mi hombre Seducción; Jodi Ellen Malpas; 2012; Novela erótica", "El código Da Vinci; Dan Brown; 2003; Novela", "La cupula; Stephen King; 2017; Novela", "Los hombres que no amaban a las mujeres; Stieg Larsson; 2011; Misterio"]

libros_clave = []

palabra_clave = "Novela"

for libos in libros:
    if palabra_clave.lower() in libos.lower():
        libros_clave.append(libos)
        print(f"la plabra clave {palabra_clave} está en: {libros_clave}")

    else: 
        print(f" la palabra clave {palabra_clave} no sie encuentra la lista de libros")
    


 










