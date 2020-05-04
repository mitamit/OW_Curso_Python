class Circulo:
    #variable de clase, pertenece a la clase y no al objeto, pero se puede utilizar en toda la clase y metodos
    #existe una normal entre desarrolladores en poner _ antes de la variable de clase para no modificarla _pi 
    pi = 3.14159
    
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return self.pi*self.radio*self.radio
       

circulo1 = Circulo(4)
circulo2 = Circulo(6)
print(circulo1.radio)
print(circulo2.radio)
print(circulo1.area())
print(Circulo.pi) #no necesito instanciar un objeto para usar la variable de clase

