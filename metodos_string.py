curso = "Curso"
my_string = "codigo facilito"

result = "{} de {}".format(curso, my_string)
print(result) 

result = "{a} de {b}".format(b = curso, a = my_string) #con alias

#formato

#result = result.lower() #minusculas
#result = result.upper() #mayusculas
#result = result.title() #como titulo
print(result) 

#busqueda

pos = result.find('facilito')
print(pos)
count = result.count('c')
print(count)

#substitucion

new_string = result.replace('c', 'x') #cambia las c por x
print(new_string)
new_string2 = result.split(' ') #devuelve un array con el contenido entre los espacios
print(new_string2)








