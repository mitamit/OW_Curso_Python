from animals import Gato
from animals import Leon
from animals import Loro

gato = Gato("El nombre del gato es Manolo")
leon = Leon("El nombre del león es Pepito")
loro = Loro("El nombre del loro es Juanito")
print(gato.nombre, leon.nombre, loro.nombre)

print(loro.comer())