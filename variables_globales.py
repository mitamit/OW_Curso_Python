
def palindromo(frase):
    frase = frase.replace(' ', '') #variables locales no modifican las variable de fuera
    return frase == frase[::-1]

frase = "anita lava la tina" #variable global
resultado = palindromo(frase)
print(resultado)

def mod_var_global():
    global variable_global #con global podemos modificar las variables globales dentro de funciones
    variable_global = "variable global modificada"

variable_global = "Esto es una variable global"
print(variable_global)
mod_var_global()
print(variable_global)


def crea_global():
    global nueva_variable #crear dentro de una función
    nueva_variable = "esto es una variable global"

crea_global()
print(nueva_variable)


