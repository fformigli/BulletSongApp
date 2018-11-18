from model import Cliente


class ClienteView:
	"""View para los diferentes modelos de BulletSongApp"""

	@staticmethod
	def view_add():
		"""metodo para agregar clientes"""

		print("Introduzca los datos del nuevo cliente")
		ruc = input("Introduzca el RUC del cliente:\n")
		idpersona = input("Introduzca el codigo de cliente:\n")
		nombre = input("Introduzca el nombre:\n")
		apellido = input("Introduzca el apellido:\n")
		cedula = input("Introduzca la cedula:\n")
		tipodoc = input("Introduzca el tipo documento:\n")
		nrotelefono = input("Introduzca el nro de telefono:\n")
		fecnac = input("Introduzca la fecha de nacimiento:\n")

		return Cliente(ruc, idpersona, nombre, apellido, cedula, tipodoc, nrotelefono, fecnac)

	@staticmethod
	def view_clientes(lista_clientes):
		"""metodo para ver todos los clientes"""
		if lista_clientes:
			for cliente in lista_clientes:
				print(cliente)

	@staticmethod
	def view_search_all():
		"""Solicita paramtro para buscar clientes por cualquier parametro"""
		return input("Introduzca el dato a buscar entre los clientes:\n")
