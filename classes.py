from abc import ABCMeta, abstractmethod

class TiendaMusical:
	def __init__(self,nombre):
		self.nombre = nombre

class Persona(metaclass=ABCMeta):
	'''Clase abstracta datos basicos de personas'''
	def __init__(self,idPersona, nombre, apellido, nroDocumento, tipoDocumento, nroTelefono, fechaNacimiento):
		self.idPersona = idPersona
		self.nombre = nombre
		self.apellido = apellido
		self.nroDocumento = nroDocumento
		self.tipoDocumento = tipoDocumento
		self.nroTelefono = nroTelefono
		self.fechaNacimiento = fechaNacimiento

	def __str__(self):
		return "("+self.nroDocumento+") "+ self.nombre +" "+self.apellido

class Cliente(Persona):
	'''Clase que representa a los Clientes de la tienda. Hereda Persona'''
	def __init__(self, ruc, *args):
		super().__init__(*args)
		self.ruc = ruc

	def __str__(self):
		return super().__str__() + " RUC: " + self.ruc

class Empleado(Persona):
	'''Clase para empleados. Solo cobran salario fijo. Hereda de Persona'''
	def __init__(self, fechaContrato, salario, *args):
		super().__init__(*args)
		self.fechaContrato = fechaContrato
		self.salario = salario
	def __str__():
		return super().__str__() + " Contratado el: " + self.fechaContrato

class EmpleadoVendedor(Empleado):
	'''Clase para vendedores. Los vendedores cobran una comision por venta ademas de su salario. Hereda de Empleado'''
	def __init__(self, comision, *args):
		super().__init__(*args)
		self.comision = comision
	def __str__(self):
		return super().__str__() + " Comision: " + self.comision

class EmpleadoBonificacion(Empleado):
	'''Clase para empleados con bonificacion (por ejemplo por exposicion a riesgos). Hereda de Empleado'''
	def __init__(self,bonificacion,*args):
		super().__init__(*args)
		self.bonificacion = bonificacion
	def __str__(self):
		return super().__str__() + " Bonificaion: " + self.bonificacion

class Producto(metaclass=ABCMeta):
	'''Clase abstracta para productos'''
	def __init__(self,idProducto,marca,stock,categoria,descripcion,nombre):
		self.idProducto = idProducto
		self.marca = marca
		self.stock = stock
		self.categoria = categoria
		self.descripcion = descripcion
		self.nombre = nombre
	def __str__(self):
		return self.categoria+" "+self.marca+" "+self.nombre+"\n"+descripcion

class Accesorio(Producto):
	'''Clase para Accesorio. productos que solo se pueden vender. Hereda de Producto'''
	def __init__(self, *args):
		super().__init__(*args)

	def __str__(self):
		return "Accesorio: "+super().__str__()

class Repuesto(Producto):
	'''Clase para Repuesto. productos que solo se pueden vender. Hereda de Producto'''
	def __init__(self, *args):
		super().__init__(*args)

	def __str__(self):
		return "Repuesto: "+super().__str__()

class Instrumento(Producto, metaclass=ABCMeta):
	'''Clase Abstracta para Instrumentos. Hereda de Producto'''
	def __init__(self, *args):
		super().__init__(*args)

class InstrumentoCuerda(Instrumento):
	'''Clase para InstrumentoCuerda. Tipos de Instrumentos. Hereda de Instrumento'''
	def __init__(self, cantidadCuerdas, *args):
		super().__init__(*args)
		self.cantidadCuerdas = cantidadCuerdas

	def __str__(self):
		return "Instrumento de Cuerda: "+ super().__str__()

class InstrumentoViento(Instrumento):
	'''Clase para InstrumentoViento. Tipos de Instrumentos. Hereda de Instrumento'''
	def __init__(self, *args):
		super().__init__(*args)

	def __str__(self):
		return "Instrumento de Viento: "+ super().__str__()

class InstrumentoPercusion(Instrumento):
	'''Clase para InstrumentoPercusion. Tipos de Instrumentos. Hereda de Instrumento'''
	def __init__(self, *args):
		super().__init__(*args)

	def __str__(self):
		return "Instrumento de Percusion: "+ super().__str__()

class InstrumentoElectronico(Instrumento):
	'''Clase para InstrumentoElectronico. Tipos de Instrumentos. Hereda de Instrumento'''
	def __init__(self, *args):
		super().__init__(*args)

	def __str__(self):
		return "Instrumento de Electronico: "+ super().__str__()
