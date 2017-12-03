
class Duenio(object):
    def __init__(self,nombre, userName,listMascotas,contrasenia):
        self.nombre=nombre
        self.userName=userName
        self.listMascotas=listMascotas
        self.contrasenia=contrasenia


	def getUsername(self):
		return self.userName
<<<<<<< 7065c21ba04269e4d705d4a3c177b2c0e23008f8:myapp/clases/duenio.py
		
		
=======


>>>>>>> Agrege una clase que permite persistencia:myapp/duenio.py
	def getPassword(self):
		return self.contrasenia

	def getMacotas(self):
		return self.listMacotas
<<<<<<< 7065c21ba04269e4d705d4a3c177b2c0e23008f8:myapp/clases/duenio.py
		
	def getNombre(self):
		return self.nombre
		
	def setUsername(self,user):
		self.userName=user
		
	def setMascotas(self,mascotas):
		self.mascotas=mascotas
	
	def setPassword(self, password):
		self.contrasenia=password
		
	def setNombre(self, nombre):
		self.nombre=nombre
		
	
		
=======



>>>>>>> Agrege una clase que permite persistencia:myapp/duenio.py

class Mascota(object):
    def __init__(self,nombre, raza,edad,sexo,disponible):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        self.sexo=sexo
        self.disponible=disponible

	def getRaza(self):
		return self.raza
<<<<<<< 7065c21ba04269e4d705d4a3c177b2c0e23008f8:myapp/clases/duenio.py
		
		
=======


>>>>>>> Agrege una clase que permite persistencia:myapp/duenio.py
	def getEdad(self):
		return self.edad

	def getNombre(self):
		return self.nombre
<<<<<<< 7065c21ba04269e4d705d4a3c177b2c0e23008f8:myapp/clases/duenio.py
		
	def getSexo(self):
		return self.sexo
		
	def getDisponible(self):
		return self.disponible
		
	def setRaza(self,raza):
		self.raza=raza
		
	def setSexo(self,sexo):
		self.sexo=sexo
	
	def setEdad(self,edad):
		self.edad=edad
	
	def setdisponible(self,disponible):
		self.disponible=disponible
	
	def setNombre(self, nombre):
		self.nombre=nombre		
		
	
	

		
		
=======
>>>>>>> Agrege una clase que permite persistencia:myapp/duenio.py
