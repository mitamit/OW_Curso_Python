my_list = ["strings", 5, 5.5, True]
my_list.append(6) #añade al final
my_list.insert(1, "CUALQUIER COSA") #añade en la posicion que queremos
my_list.remove(5) #qué queremos borrar
my_list.pop() #borra el ultimo valor del array
print(my_list)

my_integer_list = [1,3,5,90, 10, 23, 56]
my_integer_list.sort() #ordena ascendente
my_integer_list.sort(reverse=True) #ordena descendente
print(my_integer_list)

mi_lista1 = [2, 4, 6]
mi_lista2 = [9, 4]
mi_lista1.extend(mi_lista2) #une las dos lista, con append meteria un array dentro de otro
print(mi_lista1)


