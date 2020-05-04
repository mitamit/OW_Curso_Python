def generador(*args):
    """ con return daría error, yield no muestra todos los valores """
    for valor in args:
        yield valor *10 

for valor in generador(1,2,3,4,5,6,7,8,9):
    print(valor)

def generador2(*args):
    for valor in args:
        yield valor *20, True, "Esto es un generador"

for valor1, valor2, valor3 in generador2(1,4,6):
    print(valor1, valor2, valor3)