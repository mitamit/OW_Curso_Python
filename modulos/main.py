""" importa toda la calculadora y hay que llamarla como si fuera un objeto """
import calculadora

resultado = calculadora.suma(5,7)
print(resultado)

""" importa de otra manera, y podemos dar alias a los metodos de calculadora """
from calculadora import suma as s, resta as r, multiplicacion as m, division as division
result = r(10,5)
print(result)



