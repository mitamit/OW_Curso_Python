class Usuario:

    def __init__(self, username, password, email):
        self.username = username
        self.__password = self.__generar_password(password) #atributo privado, las instancias no pueden acceder
        self.email = email

    def __generar_password(self, password):
        return password.upper()

    """ Las properties sirven para modificar las propiedades privadas """

    #con property podemos visualizar y setterar el atributo privado password
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, valor):
        self.__password = self.__generar_password(valor)


eduardo = Usuario("Eduardo", "eduardo234", "eardo@cf.com")
print(eduardo.password)
eduardo.password = "Nuevo Password"
print(eduardo.password)