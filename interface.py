from abc import ABCMeta, abstractmethod


class Alquilable(metaclass=ABCMeta):
    """Interface para productos alquilables"""

    def __init__(self, precio_alquiler):
        self.multa = 10000
        self.precio_alquiler = precio_alquiler

    @abstractmethod
    def alquilar(self):
        pass


class Vendible(metaclass=ABCMeta):
    """Interfaz para productos que se pueden vender"""

    def __init__(self, precio_venta):
        self.precio_venta = precio_venta

    @abstractmethod
    def vender(self):
        pass
