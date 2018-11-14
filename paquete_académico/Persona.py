class Pais: #clase pais
	def __init__(self, p,c):
		self.nombre = p #inicializados conlos vaores que recibe
		self.capital = c

	def agregas_Pais(self,p):
		self.nombre= p

	def agregar_Capital(self,c):
		self.capital= c

	def obtener_Pais(self):
		return	self.nombre

	def obtener_Capital(self):
		return	self.capital

	def presentarPais(self):
		cadena = "Pais - %s - Capital - %s\n"%(self.obtener_Pais(),self.obtener_Capital())
		return cadena


class Persona():
	def __init__(self): # se define el __init__  con las variables a utilizar
		self.nombre = ""
		self.apellido = ""
		self.pais = ""
	def agregar_nombres(self,n): # agregamos la variable nombre
		self.nombre = n
	
	def agregar_apellido(self,p): #agregamos la variable apellido
		self.apellido = p

	def agregar_pais(self,pa): #agregamos la variable pais
		self.pais = pa
	
	def obtener_nombre(self): # obtener ciudad (retorna el valor)
		return self.nombre

	def obtener_apellido(self): # obtener ciudad (retorna el valor)
		return self.apellido

	def obtener_pais(self):
		return self.pais.presentarPais()	
	
	def presentarD (self): #funcion presentar datos
		cadena = "Informacion:\nNombres Completos:%s %s\nProcedencia: %s" % (self.nombre,self.apellido,self.pais.presentarPais())
		return cadena
	

class Estudiante(Persona):
	def __init__ (self):#funcion __init__ donde tenemos las variables a utilizar
		super(Estudiante, self).__init__()  #utilizamos el super para ocupar las funciones de la clase Empleado
		self.codigo = ""  # inicializacion de variables 
	
	def agregar_codigo (self, a):
		self.codigo = a
	
	def obtener_codigo (self):
		return self.codigo

	#funcion para presentar los datos
	def presentarD(self):
		cadena = ("%scodigo: %s\n"%(super(Estudiante, self).presentarD(),self.obtener_codigo()))
		return cadena 




class EstPresencial(Estudiante):
	def __init__ (self):#funcion __init__ donde tenemos las variables a utilizar
		super(EstudiantePrecencial, self).__init__()  #utilizamos el super para ocupar las funciones de la clase Empleado
		self.ciclo = ""  # inicializacion de variables 
		self.n_creditos = 0
	
	def agregar_ciclo (self, c):
		self.ciclo = c
	
	def obtener_ciclo (self):
		return self.codigo

	def agregar_creditos (self, cred):
		self.n_creditos = cred
	
	def obtener_creditos (self):
		return self.n_creditos

	#funcion para presentar los datos
	def presentarD(self):
		cadena = ("%sciclo: %s\nn creditos:%s"%(super(EstudiantePresencial, self).presentaD(),self.obtener_ciclo(),self.obtener_creditos()))
		return cadena 




class EstDistancia(Estudiante):
	def __init__ (self):#funcion __init__ donde tenemos las variables a utilizar
		super(EstDistancia, self).__init__()  #utilizamos el super para ocupar las funciones de la clase Empleado
		self.modulo = ""  # inicializacion de variables 
		self.n_materias = 0
	
	def agregar_modulo (self, m):
		self.modulo = m
	
	def obtener_modulo (self):
		return self.modulo.upper()

	def agregar_nmaterias (self, mat):
		self.n_materias = mat
	
	def obtener_nmaterias (self):
		return self.n_materias

	#funcion para presentar los datos
	def presentarD(self):
		cadena = ("%smodulo: %s\nnúmero de materias: %d"%(super(EstDistancia, self).presentarD(),self.obtener_modulo(),self.obtener_nmaterias()))
		return cadena 


