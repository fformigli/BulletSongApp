#main.py

from classes import *

class Application:
	'''Aplicacion para gestion de una tienda musical'''
	
	@staticmethod
	def main():
		cliente = Cliente("1043894-7",1,"Edilda","Formigli","1043894", "CI", "021212121", "1965/05/29")
		print("testing")
		print(cliente)

if __name__ == '__main__':
     Application.main()