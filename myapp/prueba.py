from controler import persistencia
from duenio import Duenio
from duenio import Mascota

base = persistencia("base.dat")
mascota1 = Mascota("a","b","c","d",True)
mascota2 = Mascota("e","f","g","h",False)
lista =[mascota1,mascota2]
usuario = Duenio("hola","username",lista,"password")
base.agrega(usuario)
lisandro = base.busca("username","password")
print lisandro.listMascotas


base.cerrar()
