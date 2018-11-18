from view import *
from model import *


class ClienteController:
    """Controlador para clientes"""

    def __init__(self):
        self.view = ClienteView
        self.cliente = Cliente

    def add(self):
        cliente = self.view.view_add()
        self.cliente.save(cliente)

    def view_all(self):
        clientes = self.cliente.list_all()
        self.view.view_all(clientes)

    def search_all(self):
        target = self.view.view_get_dato()
        result = self.cliente.search_all(target)
        self.view.view_all(result)


class EmpleadoController:
    """Controlador para empleados"""

    def __init__(self):
        self.view = EmpleadoView
        self.empleado = Empleado

    def add(self):
        empleado = self.view.view_add()
        self.empleado.save(empleado)

    def view_all(self):
        empleados = self.empleado.list_all()
        self.view.view_all(empleados)

    def view_salarios(self):
        empleados = self.empleado.list_all()
        self.view.view_salario(empleados)


class EmpleadoBonificadoController:
    """Controlador para empleados bonificados"""

    def __init__(self):
        self.view = EmpleadoBonificadoView
        self.empleado_bonificacion = EmpleadoBonificado

    def add(self):
        empleado = self.view.view_add()
        self.empleado_bonificacion.save(empleado)

    def view_all(self):
        empleados = self.empleado_bonificacion.list_all()
        self.view.view_all(empleados)

    def view_salarios(self):
        empleados = self.empleado_bonificacion.list_all()
        self.view.view_salario(empleados)
