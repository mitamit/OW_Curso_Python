lista = [1,2,3,4,5,6,7,8,9,10]

for valor in lista:
    pass

nuevo_rango = range(10,100)
for valor in nuevo_rango:
    pass

for indice, valor in enumerate(lista): #con enumerate podemos coger el indice y el valor
    print(valor, " tiene el indice ", indice)
    
diccionario = {'a': 1, 'b': 2, 'c': 3}
for llave, valor in diccionario.items():
    print("La llave", llave, "tiene el valor de", valor)    