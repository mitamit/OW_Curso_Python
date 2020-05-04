class Animal:
    @property
    def terrestre(self):
        return True

class Mascota:
    nombre = ""
    def mostrar_nombre(self):
        print(self.nombre)

class Felino(Animal):
    #para poder heredar los metodos tienen que ser publicos no privados
    @property
    def garras_retractiles(self):
        return True
    def cazar(self):
        print("El felino está cazando")

class Gato(Felino, Mascota):
    def gato_cazador(self):
        self.cazar()


gato = Gato()
gato.nombre = "Nova"
gato.mostrar_nombre()