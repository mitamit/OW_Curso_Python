def suma(*argumentos):
    print(argumentos)
print(suma(1,2,3,4,"heo"))


def suma2(*args): #con el asterisco decimos que pueden ser varios argumentos
    resultado = 0
    for valor in args:
        resultado = resultado + valor
    return resultado
resultado = suma2(4,9,3,3,2,122,332)
print(resultado)

#se pueden crear diccionarios con ** 
def suma3(**kwargs):
    print(kwargs)
    valor = kwargs.get('valor', 'no tiene valor')
    print(valor)

print(suma3(valor = 3, a = 500, b = True))


#  * n valores --> tuplas
#  ** n valores --> diccionario

