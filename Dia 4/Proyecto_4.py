from random import randint
nombre = input("Cual es tu nombre?: ")
print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")
numero = randint(1,100)
numero_intentos = 8
while numero_intentos > 0:
    n = int(input("Ingresa el número: "))
    if n<1 or n>100:
        print("Has elegido un número que no está permitido")
    elif n<numero:
        print("Respuesta incorrecta, elegiste un número menor al número secreto")
    elif n>numero:
        print("Respuesta incorrecta, elegiste un número mayor al número secreto")
    else:
        print(f"Lo lograste! has ganado, el número de intentos que te tomo es: {numero_intentos}")
        break
    numero_intentos -= 1

