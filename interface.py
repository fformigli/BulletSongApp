from abc import ABCMeta, abstractmethod

class Alquilable(metaclass=ABCMeta):
	'''Interface para productos alquilables'''
	@abstractmethod
	def alquilar(self):
		pass

class Vendible(metaclass=ABCMeta):
	'''Interfaz para productos que se pueden vender'''
	@abstractmethod
	def vender(self):
		pass