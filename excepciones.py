try:
    print(2/0)
except ZeroDivisionError as ex:
    print(ex)
    print("No se puede dividir entre 0")


try:
    lista = ['hola', 2]
    print(lista[9])
except IndexError:
    print('No es posible, este indice no existe')

#cuando no se sabe el tipo de error 
try:
    lista = ['hola', 34, True]
    print(lista[4])
except Exception as exc:
    print(exc)
