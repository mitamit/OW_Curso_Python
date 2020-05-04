#un decorador es una funcion q recibe como parametro otra función para poder crear otra funcion
def decorador( func ):
    def nueva_funcion():
        print('vamos a decorar la funcion')
        func()
        print('ya se decoro la funcion')
    return nueva_funcion


@decorador
def saluda():
    print('Hola Mundo')

saluda()

#MAS COMPLEJIDAD, funcion con parametros

def decorador_argumentos( func ):
    def nueva_funcion(*args, **kwargs):
        print('Prueba para decorador con argumentos')
        func(*args, **kwargs)
        print('entro en el decorador más flexible')
    return nueva_funcion

@decorador_argumentos
def suma(n1, n2):
    print(n1 + n2)

suma(10,10)


#decorador con parametros

def decorador_param(is_valid):
    def decorador1( func ):
        def before_action():
            print("Antes de la accion")
        def afther_action():
            print("Después de la accion")
        def nueva_funcion(*args, **kwargs):
            if is_valid:
                before_action()
            resultado = func(*args, **kwargs)
            afther_action()
            return resultado
        return nueva_funcion
    return decorador1

@decorador_param(is_valid = False) #si es False no se ejecuta before_action()
def resta(n1, n2):
    return n1 - n2
        
result = resta(5,1)
print(result)



