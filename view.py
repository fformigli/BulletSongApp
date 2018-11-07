from model import Cliente

class View:
	"""View para los diferentes modelos de BulletSongApp"""
	def view_agregar_cliente(self):
		print("Introduzca los datos del nuevo cliente")
		ruc = input("Introduzca el RUC del cliente:\n")
		id = input("Introduzca el codigo de cliente:\n")
		nombre = input("Introduzca el nombre:\n")
		apellido = input("Introduzca el apellido:\n")
		cedula = input("Introduzca la cedula:\n")
		tipodoc = input("Introduzca el tipo documento:\n")
		nrotelefono = input("Introduzca el nro de telefono:\n")
		fecnac = input("Introduzca la fecha de nacimiento:\n")

		return Cliente(ruc,id,nombre,apellido,cedula,tipodoc,nrotelefono,fecnac)