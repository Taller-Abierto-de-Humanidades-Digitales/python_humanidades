#objeto = open(nombre_archivo, modo)
""" 
p1 = "El guardagujas\n\nJuan José Arreola\n\nEl forastero llegó sin aliento a la estación desierta. Su gran valija, que nadie quiso cargar, le había fatigado en extremo. Se enjugó el rostro con un pañuelo, y con la mano en visera miró los rieles que se perdían en el horizonte. Desalentado y pensativo consultó su reloj: la hora justa en que el tren debía partir.\nAlguien, salido de quién sabe dónde, le dio una palmada muy suave. Al volverse el forastero se halló ante un viejecillo de vago aspecto ferrocarrilero. Llevaba en la mano una linterna roja, pero tan pequeña, que parecía de juguete. Miró sonriendo al viajero, que le preguntó con ansiedad:\n"
p2 = "-Usted perdone, ¿ha salido ya el tren?"
p3 = "-¿Lleva usted poco tiempo en este país?"
p4 = "-Necesito salir inmediatamente. Debo hallarme en T. mañana mismo."

parrafos = [p1, p2, p3, p4]

for p in parrafos:
    with open(r"estudiantes\Ejemplo\Sesión11\arreola.txt", 'a', encoding='utf-8') as f:
        f.write(p + "\n")
 """

f = open(r"E:\Biblioteca\el_quijote.txt", 'r', encoding='utf-8')
for r in f.readlines():
    if "molino" in r:
        with open(r"estudiantes\Ejemplo\Sesión11\resultado.txt", 'a', encoding='utf-8') as f:
            f.write(r + "\n")