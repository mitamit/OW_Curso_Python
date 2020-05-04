class Lapiz :
    """ El metodo init se ejecuta cuando se crea una instancia, 
        pudiendose setear a la hora de instanciarla, aún teniendo valores por default
    """ 
    #init = constructor
    def __init__(self, color = "Amarillo", contiene_borrador = False, contiene_grafito = True): 

        self.color = color
        self.contiene_borrador = contiene_borrador
        self.contiene_grafito = contiene_grafito
    
    #metodos
    def dibujar(self):
        print("El lápiz está dibujando")

    def borrar(self):
        if self.es_valido_para_borrar():
            print("El lápiz está borrando")
        else:
            print("El lápiz no puede borrar")

    def es_valido_para_borrar(self):
        return self.contiene_borrador

#instanciamos los objetos de la clase

lapiz1 = Lapiz("Verde", True, True) #nos devuelve True en contiene_borrador
lapiz1 = Lapiz() #nos devuelve False en contiene_borrador por el metodo init, sin valores coge los default
lapiz1.dibujar()
lapiz1.borrar()