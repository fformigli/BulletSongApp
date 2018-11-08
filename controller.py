from view import *
from model import *


class ClienteController:
    def __init__(self):
        self.view = View()
        self.cliente = Cliente

    def add(self):
        cliente = self.view.view_add_cliente()
        self.cliente.save(cliente)

    def view_all(self):
        lista_clientes = self.cliente.view_all()
        self.view.view_all_clientes(lista_clientes)
        return lista_clientes
