
class Duenio(object):
    def __init__(self,nombre, userName,listMascotas,contrasenia):
        self.nombre=nombre
        self.userName=userName
        self.listMascotas=listMascotas
        self.contrasenia=contrasenia

		
	def getUsername(self):
		return userName
		
		
	def getPassword(self):
		return contrasenia

	def getMacotas(self):
		return listMacotas
	
	
		

class Mascota(object):
    def __init__(self,nombre, raza,edad,sexo,disponible):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        self.sexo=sexo

		
	def getRaza(self):
		return raza
		
		
	def getEdad(self):
		return edad

	def getNombre(self):
		return nombre
		
	
	

		
		
