# Proyecto: Analizador de Texto
# Primera Parte
texto = input("Ingrese un texto: ")
letras = input("Ingrese 3 letras: ")
texto = texto.lower()
letras = letras.lower()
lista = list(letras)
letra1 = lista[0]
letra2 = lista[1]
letra3 = lista[2]
conteo1 = texto.count(letra1)
conteo2 = texto.count(letra2)
conteo3 = texto.count(letra3)
print("La primera letra aparece en el texto: " + str(conteo1) + " veces")
print("La segunda letra aparece en el texto: " + str(conteo2) + " veces")
print("La tercera letra aparece en el texto: " + str(conteo3) + " veces")

# Segunda Parte
lista2 = list(texto.split(" "))
largo = len(lista2)
print("El Texto tiene " + str(largo) + " palabras")

# Tercera Parte
texto2 = list(texto)
primera_letra = texto2[0]
ultima_letra = texto2[-1]
print("la primera letra del texto es: " + primera_letra.upper())
print("La ultima letra del texto es: " + ultima_letra.lower())

# Cuarta Parte
lista3 = list(texto.split(" "))
lista3.reverse()
texto3 = " ".join(lista3)
print(texto3)

# Quinta Parte
condicion = "python" in lista2
dic = {True:"si",False:"no"}
print("La Palabra Python se encuentra dentro del texto?: " + dic[condicion])