mi_archivo = open("Prueba.txt")
print(mi_archivo)
print(mi_archivo.read())
mi_archivo.close()
mi_archivo = open("Prueba.txt")
print(mi_archivo.readline())
print(mi_archivo.readline())
print(mi_archivo.readline())
mi_archivo.close()
mi_archivo = open("Prueba.txt")
todas = mi_archivo.readlines()

todas = todas[1]

print(todas)