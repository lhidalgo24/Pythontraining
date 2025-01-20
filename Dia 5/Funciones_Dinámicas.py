def chequear_3_cifras(numero):
    return numero in range(100,1000)

suma = 586 + 402

resultado = chequear_3_cifras(suma)
print(resultado)

def chequear_3_cifrass(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False

suma = [55,99,6000]

resultado = chequear_3_cifrass(suma)
print(resultado)


def chequear_3_cifrasss(lista):
    lista_3_cifras = []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

suma = [555,99,600]

resultado = chequear_3_cifrasss(suma)
print(resultado)
