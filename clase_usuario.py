class Usuario:

    def __init__(self, username, password, email):
        self.username = username
        self.__password = self.generar_password(password) #atributo privado, las instancias no pueden acceder
        self.email = email

    def generar_password(self, password):
        return password.upper()

    def get_password(self): #metodo que retorna un atributo privado, se llama en la instancia en vez del atributo en si
        return self.__password

eduardo = Usuario("Eduardo", "eduardo123", "eduardo@cf.com")

print(eduardo.username, eduardo.email, eduardo.get_password())
