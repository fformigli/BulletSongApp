from model import *
from view import *


class ClienteController:
    def __init__(self):
        self.view = View()

    def agregar(self):
        cliente = self.view.view_agregar_cliente()
        print(cliente)
        #self.model.guardarPersona(cliente)
