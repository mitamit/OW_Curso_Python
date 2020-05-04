def suma(valor_uno, valor_dos):
    return valor_uno + valor_dos

resultado = suma(5, 10)
print(resultado)

#con lambdas, son funciones pequeñas de una sola linea para calculos simples y muy siplificadas
mi_variable = lambda valor1, valor2 : valor1 + valor2
result = mi_variable(10, 50)
print(result)

#por ejemplo poner formatos a las frases
formato = lambda sentencia : '¿{}?' .format(sentencia)
res = formato('puedes hacer esto una pregunta')
print(res)

#lo mas simple, siempre debe retornar algo sino peta
no_valor = lambda : 10
print(no_valor())