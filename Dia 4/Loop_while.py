monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo más dinero")


respuesta = 's'
while respuesta == 's':
    respuesta = input("Quieres seguir? (s/n)")
else:
    print("Gracias")

respuesta = 's'
while respuesta == 's':
    pass
    break
print("Hola")

nombre = input("Tu nombre:")
for letra in nombre:
    if letra == 'r':
        break
    print(letra)

nombre = input("Tu nombre:")
for letra in nombre:
    if letra == 'r':
        continue
    print(letra)