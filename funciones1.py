def factorial_numero():
    numero = 5
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    print(factorial)

factorial_numero()




def factorial_cualq_num(numero):
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial

resultado = factorial_cualq_num(8)
print(resultado)

