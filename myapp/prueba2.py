from controler import persistencia

base = persistencia("base.dat")

lisandro = base.busca("username","password")
print lisandro.listMascotas

base.cerrar()
