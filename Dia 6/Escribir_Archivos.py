archivo = open('Prueba.txt','r')
archivo.close()

archivo = open('Prueba.txt','w')
archivo.write('soy el nuevo texto')
archivo.writelines(['hola','soy','el','nuevo','texto'])
archivo.close()


lista = ['hola','soy','el','nuevo','texto']

archivo = open("Prueba.txt",'w')
for p in lista:
    archivo.writelines(p + '\n')
archivo.close()

