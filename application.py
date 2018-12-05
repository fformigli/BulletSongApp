#!/usr/bin/python
# fformigli 2018

from model import Cliente, EmpleadoBonificado, InstrumentoCuerda
from controller import ClienteController, EmpleadoController, EmpleadoBonificadoController, EmpleadoVendedorController, InstrumentoCuerdaController
from gui import Main


class Application:
    """Aplicacion para gestion de una tienda musical"""

    def __init__(self):
        self.menu()

    @staticmethod
    def menu():
        """Menu para uso de la aplicacion"""

        index = -1
        while index != "0":
            print("Menu:\n")

            options = ["Ver Clientes", "Agregar Cliente", "Buscar en Clientes", "Agregar Empleado",
                       "Agregar Empleado con Bonificacion", "Agregar Vendedor", "Calcular Salarios", "Agregar Instrumento de Cuerdas", "Ver todos los productos"]

            c = 0
            for option in options:
                c += 1
                print(str(c) + ".- " + option)

            print("0.- Salir")

            index = input("Introduzca el numero de operacion que quiere realizar:\n")
            cliente_controller = ClienteController()
            empleado_controller = EmpleadoController()
            empleado_bonificado_controller = EmpleadoBonificadoController()
            empleado_vendedor_controller = EmpleadoVendedorController()
            instrumento_cuerda_controller = InstrumentoCuerdaController()

            if index == "1":
                cliente_controller.view_all()
            elif index == "2":
                cliente_controller.add()
            elif index == "3":
                cliente_controller.search_all()

            elif index == "4":
                empleado_controller.add()
            elif index == "5":
                empleado_bonificado_controller.add()
            elif index == "6":
                empleado_vendedor_controller.add()
            elif index == "7":
                empleado_controller.view_salarios()
                empleado_bonificado_controller.view_salarios()
                empleado_vendedor_controller.view_salarios()
            elif index == "8":
                instrumento_cuerda_controller.add()
            elif index == "9":
                instrumento_cuerda_controller.view_all()

    @staticmethod
    def cargar_listas():
        cliente = Cliente("1043894-7", 1, "Edilda", "Formigli", "1043894", "CI", "021212121", "1965/05/29")
        cliente.save(cliente)

        empleado_bonificacion = EmpleadoBonificado(250000, "24/08/2010", 3000000, 25, "Fernando", "Formigli",
                                                   "5088536", "CI", "0983265381", "1995/01/01")
        empleado_bonificacion.save(empleado_bonificacion)

        instrumento_cuerda = InstrumentoCuerda(6, 1, "Fender", 6, "Guitarra Electica", "ideal para jazz",
                                               "Stratocaster")


if __name__ == '__main__':
    Application()
