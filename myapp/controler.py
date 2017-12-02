import shelve
from duenio import Duenio
from duenio import Mascota

class persistencia(object):

	def __init__(self,file_name):
		self.base_Datos = shelve.open(file_name)

	def agrega(self,usuario):
		self.base_Datos[usuario.userName] = usuario

	def busca(self,usuario,password):
		if usuario in self.base_Datos and self.base_Datos[usuario].contrasenia == password:
			return self.base_Datos[usuario]
		else:
			return None

	def cerrar(self):
		self.base_Datos.close()
