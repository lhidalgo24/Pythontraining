nombre = input("Cual es tu nombre?: ")
ventas = input("Cuanto has vendido?: ")
ventas = float(ventas)
comision = round(ventas*13/100,2)
print(f"Hola {nombre}! , tus comisiones ganadas este son: {comision}")
