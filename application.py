#Application : clase principal

from model import Cliente,EmpleadoBonificacion,InstrumentoCuerda

class Application:
	'''Aplicacion para gestion de una tienda musical'''
	
	@staticmethod
	def main():
		print("testing")
		cliente = Cliente("1043894-7",1,"Edilda","Formigli","1043894", "CI", "021212121", "1965/05/29")
		print(cliente)

		empleadoBonificacion = EmpleadoBonificacion(250000,"24/08/2010",3000000,25,"Fernando","Formigli","5088536","CI","0983265381","1995/01/01")
		print(empleadoBonificacion)
		print("El salario de este empleado es: "+str(empleadoBonificacion.calculo_salario()))

		instrumentoCuerda = InstrumentoCuerda(6,1,"Fender",6,"Guitarra Electica","ideal para jazz","Stratocaster")
		print(instrumentoCuerda)

		print(instrumentoCuerda.alquilar())



if __name__ == '__main__':
     Application.main()