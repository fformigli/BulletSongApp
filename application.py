#!/usr/bin/python

from model import Cliente, EmpleadoBonificacion, InstrumentoCuerda
from controller import ClienteController
import tkinter


class Application:
    """Aplicacion para gestion de una tienda musical"""

    def __init__(self):
        self.main()

    @staticmethod
    def main():
        """Menu para uso de la aplicacion"""
        cliente_controller = ClienteController()
        cliente_controller.agregar()

    @staticmethod
    def test():
        """ejecucion para pruebas"""
        print("testing")
        cliente = Cliente("1043894-7", 1, "Edilda", "Formigli", "1043894", "CI", "021212121", "1965/05/29")
        print(cliente)

        empleado_bonificacion = EmpleadoBonificacion(250000, "24/08/2010", 3000000, 25, "Fernando", "Formigli",
                                                     "5088536", "CI", "0983265381", "1995/01/01")
        print(empleado_bonificacion)
        print("El salario de este empleado es: " + str(empleado_bonificacion.calculo_salario()))

        instrumento_cuerda = InstrumentoCuerda(6, 1, "Fender", 6, "Guitarra Electica", "ideal para jazz",
                                               "Stratocaster")
        print(instrumento_cuerda)

        print(instrumento_cuerda.alquilar())


class GApplication:
    """Interfaz grafica de la Aplicacion"""

    def __init__(self):
        self.main = tkinter.Tk()
        self.main.title("BulletSongApp")
        self.main.minsize(720, 300)

        label = tkinter.Label(self.main, text="testing some label in main window")
        label.pack()


if __name__ == '__main__':
    Application()
# gapp = GApplication()
# gapp.main.mainloop()
