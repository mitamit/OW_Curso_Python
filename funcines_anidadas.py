def validacion(num1, num2):
    return num1 > 0 and num2 > 0

def division(num1, num2):
    if validacion(num1, num2): 
        return num1 / num2

resultado = division(8, 5)
print(resultado)

#anidadas

def div(num1, num2):
    def validacion():
        return num1 > 0 and num2 > 0

    if validacion(): 
        return num1 / num2

result = div(3,9)
print(result)

