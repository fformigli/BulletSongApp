#!/usr/bin/python
# fformigli 2018
from tkinter import Tk, Menu, ttk

from controller import *


class Application:
    """Aplicacion para gestion de una tienda musical"""
    def __init__(self):
        Main()


class Main:
    """Interfaz Principal"""

    def __init__(self):
        self.root = Tk()
        self.root.title("BulletSongApp")
        self.root.geometry("900x400+100+100")

        self.frame = ttk.Frame(self.root, padding="10 10 5 5")

        # menubar
        self.menubar = Menu(self.root)

        # menu headers
        self.menugeneral = Menu(self.menubar, tearoff=0)
        self.menurrhh = Menu(self.menubar, tearoff=0)

        # sub menu
        self.submenu_clientes = Menu(self.menugeneral, tearoff=0)

        # menu commands
        # self.menugeneral.add_command(label="Productos")
        # self.menugeneral.add_command(label="Inventario")

        # self.menurrhh.add_command(label="Empleados")
        self.menurrhh.add_command(label="Salarios", command=self.view_salarios_general)

        self.submenu_clientes.add_command(label="Añadir Clientes", command=self.add_clientes)
        self.submenu_clientes.add_command(label="Ver Clientes",
                                          command=lambda: (ClienteController()).view_all(self.frame))

        # add menu headers to menu bar and submenes
        self.menugeneral.add_cascade(label="Clientes", menu=self.submenu_clientes)
        self.menubar.add_cascade(label="Gestión", menu=self.menugeneral)
        self.menubar.add_cascade(label="RRHH", menu=self.menurrhh)

        self.menubar.add_command(label="Salir", command=self.root.destroy)

        # add menu bar to window
        self.root.config(menu=self.menubar)
        self.root.mainloop()

    def view_salarios_general(self):
        empleado_controller = EmpleadoController()
        empleado_bonificado_controller = EmpleadoBonificadoController()
        empleado_vendedor_controller = EmpleadoVendedorController()

        empleado_controller.view_salarios(self.frame)
        empleado_bonificado_controller.view_salarios(self.frame)
        empleado_vendedor_controller.view_salarios(self.frame)

    def add_clientes(self):
        cliente_controller = ClienteController()
        cliente_controller.add(self.frame)


if __name__ == '__main__':
    Application()
