nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]
ciudades = ['Lima','Madrid','Mexico']

combinados = list(zip(nombres,edades,ciudades))

print(combinados)

for nombre,edad,ciudades in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudades}")