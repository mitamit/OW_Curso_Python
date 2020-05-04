contador = 0

while contador <= 10:
    if contador == 5:
        continue
    if contador == 6:
        break

    print(contador)
    contador+=1
else:
    print("El while no ha terminado")