if 10 > 9:
    print("Es correcto")

x = True
if x:
    print("Es correcto")

if 5==2:
    print("Es correcto")
else:
    print("No es correcto")

mascota = "perro"
if  mascota == "gato":
    print("Tienes un gato")
elif mascota == "perro":
    print("Tienes un perro")
elif mascota == "pez":
    print("Tienes un pez")
else:
    print("No se qué animal tienes")


edad = 16
calificacion = 9

if edad<18:
    print("Eres menor de edad")
    if calificacion >= 7:
        print("Aprobado")
    else:
        print("Desaprobado")
else:
    print("Eres adulto")