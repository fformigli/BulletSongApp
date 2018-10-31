from classes import *

class Model:
	def guardarCliente(self, cliente):
		result = []
		try:
			archivo = open('persona.pickle', 'rb')
			result = pickle.load(archivo)
			archivo.close()
			archivoNuevo = open('persona.pickle','wb')
			result.append(persona)
			pickle.dump(result, archivoNuevo)
			archivoNuevo.close()
		except IOError:
			archivoNuevo = open('persona.pickle','wb')
			result.append(persona)
			pickle.dump(result, archivoNuevo)
			archivoNuevo.close()
		return