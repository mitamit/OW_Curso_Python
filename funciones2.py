def suma(valor1, valor2, valor3):
    return valor1 + valor2 + valor3

resultado = suma(10, 20, 30)
print(resultado)



def division(valor1, valor2):
    return valor1/valor2

result = division(valor2 = 10, valor1 = 100)
print(result)



def multiplica(valor1, valor2 = 4):
    return valor1 * valor2

resultad = multiplica(19)
print(resultad)


def multiples_valores():
    return "string", 1, True, 25.6

string, entero, bol, floa = multiples_valores()
print(string)
print(entero)
print(bol)
print(floa)


def mostrar_resultado( funcion ):
    print(funcion)
    
mi_funcion = multiplica
mostrar_resultado(mi_funcion(6,8))
