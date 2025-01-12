texto = "Este es el texto de lovel"
resultado = texto.upper()
print(resultado)
resultado = texto[2].upper()
print(resultado)
resultado = texto.lower()
print(resultado)
resultado = texto.split()
print(resultado)
resultado = texto.split("t")
print(resultado)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)

resultado = texto.find("g")
print(resultado)

resultado = texto.replace("lovel","juan")
print(resultado)

resultado = texto.replace("e","x")
print(resultado)