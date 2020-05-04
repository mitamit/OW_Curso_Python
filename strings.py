my_string = "Hola Mundo!!"
print(my_string)
my_string_salto = """ Este es un string con\nsaltos de linea """
print(my_string_salto)

string1 = "Hola que ase"
string2 = "palangana"

final_message = string1 + " " + string2 #1
print(final_message)
final_message2 = "%s %s" %(string1, string2) #2 
print(final_message2)
final_message3 = "{} {}".format(string1, string2) #3
print(final_message3)
