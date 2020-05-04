class Animal:
    @property
    def terrestre(self):
        return True

class Felino(Animal):
    #para poder heredar los metodos tienen que ser publicos no privados
    @property
    def garras_retractiles(self):
        return True
    def cazar(self):
        print("El felino está cazando")

class Gato(Felino):
    pass
class Puma(Felino):
    pass

gato = Gato()
puma = Puma()
print(gato.garras_retractiles)
gato.cazar()
print(puma.terrestre)