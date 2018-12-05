from model import *
from view import EmpleadoView, ClienteView, EmpleadoBonificadoView, EmpleadoVendedorView, InstrumentoCuerdaView, \
    msg_guardado


class ClienteController:
    """Controlador para clientes"""

    def __init__(self):
        self.view = ClienteView
        self.cliente = Cliente

    def add(self, frame):
        self.view.view_add(frame)

    def view_all(self, frame):
        self.view.view_all(frame, filter(None, self.cliente.list_all()))

    def search_all(self, frame):
        self.view.view_all(frame, self.cliente.search_all(self.view.view_get_dato()))

class EmpleadoController:
    """Controlador para empleados"""

    def __init__(self):
        self.view = EmpleadoView
        self.empleado = Empleado

    def add(self):
        self.empleado.save(self.view.view_add())

    def view_all(self):
        return self.empleado.list_all()

    def view_salarios_completo(self, frame, lista):
        self.view.view_salarios_completo(frame, lista)


class EmpleadoBonificadoController:
    """Controlador para empleados bonificados"""

    def __init__(self):
        self.view = EmpleadoBonificadoView
        self.empleado_bonificacion = EmpleadoBonificado

    def add(self):
        self.empleado_bonificacion.save(self.view.view_add())

    def view_all(self):
        return self.empleado_bonificacion.list_all()

    def view_salarios(self):
        return self.empleado_bonificacion.list_all()


class EmpleadoVendedorController:
    """Controlador para Vendedores. Cobran salario base mas un porcentaje de comision"""

    def __init__(self):
        self.view = EmpleadoVendedorView
        self.empleado_vendedor = EmpleadoVendedor

    def add(self):
        self.empleado_vendedor.save(self.view.view_add())

    def view_all(self):
        return self.empleado_vendedor.list_all()

    def view_salarios(self):
        return self.empleado_vendedor.list_all()


class InstrumentoCuerdaController:
    """Controlador para los instrumentos de cuerda"""

    def __init__(self):
        self.view = InstrumentoCuerdaView
        self.instrumento_cuerda = InstrumentoCuerda

    def add(self):
        self.instrumento_cuerda.save(self.view.view_add())

    def view_all(self):
        self.view.view_all(self.instrumento_cuerda.list_all())
