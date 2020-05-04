class Circulo:

    @staticmethod
    def pi():  #metodo estatico, como las propiedades de clase, pertenecen a la clase y no a la instancia pero se puede instanciar tmb
        return 3.14159
    
    def __init__(self, radio):
        self.radio = radio

    def area(self): #metodos de instancia
        return self.pi()*self.radio*self.radio
       
   

circulo1 = Circulo(4)
print(circulo1.area())