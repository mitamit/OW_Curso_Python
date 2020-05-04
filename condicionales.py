fruta = "kiwi"

#no hay llaves, enter y tab
if fruta == "manz" : 
    print('kiwi')
elif fruta == "manzana" :
    print('manzana')

elif fruta == "pera" :
    pass #no quiero salida para que no pete ponemos pass

else :
    print('no son iguales')



#mensaje = "El valor es kiwi" if fruta == "kiwi" else "No son iguales"
#print(mensaje)

#True = 1
#False = 0

valor = None
valor2 = 20

if valor :  # [], () {}, '', 0, None   ---> la variables vacias retornan 0 es decir False
    print('Es verdad')
else:
    print('No es verdad')

if valor and valor2 < 30 :
    print('Es verdad')
else:
    print('No es verdad')

if valor or valor2 > 14:
    print('Es verdad')
else:
    print('No es verdad')




