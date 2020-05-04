diccionario = {'a': True, 1: "esto es un string", (1,2): False} #las llaves son inmutables

#almacenar
diccionario['b'] = "nuevo string" #creamos clave valor
diccionario['a'] = False #si encuentra la llave actualiza sino crea

#obtener datos
valor = diccionario['a']
valor = diccionario.get('z', False) #sino encuentra z regresa False sino devuelve el valor

#eliminar
del diccionario[1]

print(diccionario)
print(valor)

llaves = diccionario.keys() #objeto iterable
llaves = list(diccionario.keys()) #convierte en array las llaves
valores = list(diccionario.values()) #convierte en array los valores
print(llaves)
print(valores)

diccionario2 = {2: "esto es string del segundo diccionario", "t": 239, 4: True}
diccionario.update(diccionario2) #diccionario2 se añade a diccionario
print(diccionario)
