from view import *
from model import *


class ClienteController:
    """Controlador para clientes"""
    def __init__(self):
        self.view = ClienteView()
        self.cliente = Cliente

    def add(self):
        cliente = self.view.view_add()
        self.cliente.save(cliente)

    def view_all(self):
        lista_clientes = self.cliente.list_all()
        self.view.view_clientes(lista_clientes)
        return lista_clientes

    def delete(self):
        # TODO: eliminar clientes
        # cliente = self.view.search
        pass

    def search_all(self):
        target = self.view.view_search_all()
        result = self.cliente.search_all(target)
        self.view.view_clientes(result)
        return result
