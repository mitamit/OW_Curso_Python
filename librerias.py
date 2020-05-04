import random
import datetime
import time

#random
lista = ['hola', 34, True, 34.9]
valor1 = random.randint(0,10) #rango entre los que elegira random
valor2 = random.choice(lista) #elige un valor de la lista random
random.shuffle(lista) #ordena los objetos de la lista de manera random
print(valor1)
print(valor2)
print(lista)

#datetime
print(datetime.datetime.now())

#time
for i in range(100):
    time.sleep(0.5) #imprime del 0 al 99 con un delay de medio segundo
    print(i)

