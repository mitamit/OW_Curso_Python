#lista = []
#for valor in range(0, 101):
    #lista.append(valor)
#print(lista)



#con compren
lista = [valor for valor in range(0, 101)] #rellena la lista directamente del 0 al 100
print(lista)

lista = [valor for valor in range(0, 101) if valor % 2 == 0] #rellena la lista con los pares
print(lista)

tupla = tuple((valor for valor in range(0, 101) if valor % 2 != 0)) #para generar una tupla con numeros impares
print(tupla)

diccionario = {indice:valor for indice, valor in enumerate(lista) if indice < 10} #crear diccionario indice:valor
print(diccionario)