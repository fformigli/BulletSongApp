from interface import *
import pickle


class TiendaMusical:
    def __init__(self):
        self.nombre = "BulletSong"


class Persona(metaclass=ABCMeta):
    """Clase abstracta datos basicos de personas"""

    def __init__(self, id_persona, nombre, apellido, nro_documento, tipo_documento, nro_telefono, fecha_nacimiento):
        self.id_persona = id_persona
        self.nombre = nombre
        self.apellido = apellido
        self.nro_documento = nro_documento
        self.tipo_documento = tipo_documento
        self.nro_telefono = nro_telefono
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return "COD: " + self.id_persona + " (" + self.nro_documento + ") " + self.nombre.upper() + " " + self.apellido.upper()


class Cliente(Persona):
    """Clase que representa a los Clientes de la tienda. Hereda Persona"""

    @staticmethod
    def save(cliente):

        print(cliente)
        result = []
        try:
            archivo = open('pickle/cliente.pickle', 'rb')
            result = pickle.load(archivo)
            archivo.close()
            file = open('pickle/cliente.pickle', 'wb')
            result.append(cliente)
            pickle.dump(result, file)
            file.close()

        except IOError:
            # TODO: propagar correctamente
            file = open('pickle/cliente.pickle', 'wb')
            result.append(cliente)
            pickle.dump(result, file)
            file.close()
        return True

    @staticmethod
    def search_all(target):
        result = []
        lista_clientes = Cliente.list_all()
        if lista_clientes:
            for cliente in lista_clientes:
                if target.lower() in cliente.__str__().lower():
                    result.append(cliente)

        return result

    @staticmethod
    def list_all():
        result = []
        try:
            file = open('pickle/cliente.pickle', 'rb')
            result = pickle.load(file)
            file.close()
            return result
        except IOError:
            # TODO: propagar correctamente
            return result

    def __init__(self, ruc, *args):
        super().__init__(*args)
        self.ruc = ruc

    def __str__(self):
        return "Cliente: " + super().__str__() + " RUC: " + self.ruc


class Empleado(Persona):
    """Clase para empleados. Solo cobran salario fijo. Hereda de Persona"""

    def __init__(self, fecha_contrato, salario, *args):
        super().__init__(*args)
        self.fecha_contrato = fecha_contrato
        self.salario = salario

    def calculo_salario(self):
        return "Asalariado\t" + str(int(self.salario))

    def salario(self):
        return self.salario

    @staticmethod
    def save(empleado):
        result = []
        try:
            archivo = open('pickle/empleado.pickle', 'rb')
            result = pickle.load(archivo)
            archivo.close()
            file = open('pickle/empleado.pickle', 'wb')
            result.append(empleado)
            pickle.dump(result, file)
            file.close()
        except IOError:
            # TODO: propagar correctamente
            file = open('pickle/empleado.pickle', 'wb')
            result.append(empleado)
            pickle.dump(result, file)
            file.close()
        return

    @staticmethod
    def list_all():
        result = []
        try:
            file = open('pickle/empleado.pickle', 'rb')
            result = pickle.load(file)
            file.close()
            return result
        except IOError:
            # TODO: propagar correctamente
            return result

    def __str__(self):
        return super().__str__() + " Contratado el: " + self.fecha_contrato + "  Salario: " + str(self.salario)


class EmpleadoVendedor(Empleado):
    """Clase para vendedores. Los vendedores cobran una comision por venta ademas de su salario. Hereda de Empleado"""

    def __init__(self, comision, *args):
        super().__init__(*args)
        self.comision = comision

    def calculo_salario(self):
        return "Vendedor\t\t" + str(int(int(super().salario()) + int(super().salario()) * int(self.comision) / 100))

    @staticmethod
    def list_all():
        result = []
        try:
            file = open('pickle/empleado_vendedor.pickle', 'rb')
            result = pickle.load(file)
            file.close()
            return result
        except IOError:
            # TODO: propagar correctamente
            return result

    @staticmethod
    def save(empleado):
        result = []
        try:
            archivo = open('pickle/empleado_vendedor.pickle', 'rb')
            result = pickle.load(archivo)
            archivo.close()
            file = open('pickle/empleado_vendedor.pickle', 'wb')
            result.append(empleado)
            pickle.dump(result, file)
            file.close()
        except IOError:
            # TODO: propagar correctamente
            file = open('pickle/empleado_vendedor.pickle', 'wb')
            result.append(empleado)
            pickle.dump(result, file)
            file.close()
        return

    def __str__(self):
        return super().__str__() + " Comision: " + self.comision


class EmpleadoBonificado(Empleado):
    """Clase para empleados con bonificacion (por ejemplo por exposicion a riesgos). Hereda de Empleado"""

    def __init__(self, bonificacion, *args):
        super().__init__(*args)
        self.bonificacion = bonificacion

    def calculo_salario(self):
        return "Bonificado\t" + str(int(super().salario()) + int(self.bonificacion))

    @staticmethod
    def list_all():
        result = []
        try:
            file = open('pickle/empleado_bonificado.pickle', 'rb')
            result = pickle.load(file)
            file.close()
            return result
        except IOError:
            # TODO: propagar correctamente
            return result

    @staticmethod
    def save(empleado):
        result = []
        try:
            archivo = open('pickle/empleado_bonificado.pickle', 'rb')
            result = pickle.load(archivo)
            archivo.close()
            file = open('pickle/empleado_bonificado.pickle', 'wb')
            result.append(empleado)
            pickle.dump(result, file)
            file.close()
        except IOError:
            # TODO: propagar correctamente
            file = open('pickle/empleado_bonificado.pickle', 'wb')
            result.append(empleado)
            pickle.dump(result, file)
            file.close()
        return

    def __str__(self):
        return super().__str__() + " Bonificacion: " + str(self.bonificacion)


class Producto(Vendible, metaclass=ABCMeta):
    """Clase abstracta para productos"""

    def vender(self):
        pass

    def __init__(self, id_producto, marca, stock, categoria, descripcion, nombre, precio_venta):
        super().__init__(precio_venta)
        self.id_producto = id_producto
        self.marca = marca
        self.stock = stock
        self.categoria = categoria
        self.descripcion = descripcion
        self.nombre = nombre

    def __str__(self):
        return self.categoria + " " + self.marca + " " + self.nombre + "\n\t" + self.descripcion


class Accesorio(Producto):
    """Clase para Accesorio. productos que solo se pueden vender. Hereda de Producto"""

    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return "Accesorio: " + super().__str__()

    def vender(self):
        pass


class Repuesto(Producto):
    """Clase para Repuesto. productos que solo se pueden vender. Hereda de Producto"""

    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return "Repuesto: " + super().__str__()

    def vender(self):
        pass


class Instrumento(Alquilable, Producto, metaclass=ABCMeta):
    """Clase Abstracta para Instrumentos. Hereda de Producto"""

    def __init__(self, id_producto, marca, stock, categoria, descripcion, nombre, precio_venta, precio_alquiler,
                 plazo_alquiler, multa):
        Alquilable.__init__(self, precio_alquiler, plazo_alquiler, multa)
        Producto.__init__(self, id_producto, marca, stock, categoria, descripcion, nombre, precio_venta)

    def alquilar(self):
        return 10000 + super().multa

    def vender(self):
        return "vendido"


class InstrumentoCuerda(Instrumento):
    """Clase para InstrumentoCuerda. Tipos de Instrumentos. Hereda de Instrumento"""

    def __init__(self, cantidad_cuerdas, id_producto, marca, stock, categoria, descripcion, nombre, precio_venta,
                 precio_alquiler, plazo_alquiler, multa):
        super().__init__(id_producto, marca, stock, categoria, descripcion, nombre, precio_venta, precio_alquiler,
                         plazo_alquiler, multa)
        self.cantidad_cuerdas = cantidad_cuerdas

    @staticmethod
    def list_all():
        result = []
        try:
            file = open('pickle/instrumento_cuerda.pickle', 'rb')
            result = pickle.load(file)
            file.close()
            return result
        except IOError:
            # TODO: propagar correctamente
            return result

    @staticmethod
    def save(instrumento_cuerda):
        result = []
        try:
            archivo = open('pickle/instrumento_cuerda.pickle', 'rb')
            result = pickle.load(archivo)
            archivo.close()
            file = open('pickle/instrumento_cuerda.pickle', 'wb')
            result.append(instrumento_cuerda)
            pickle.dump(result, file)
            file.close()
        except IOError:
            # TODO: propagar correctamente
            file = open('pickle/instrumento_cuerda.pickle', 'wb')
            result.append(instrumento_cuerda)
            pickle.dump(result, file)
            file.close()
        return

    def __str__(self):
        return "Instrumento de Cuerda: " + super().__str__()


class InstrumentoViento(Instrumento):
    """Clase para InstrumentoViento. Tipos de Instrumentos. Hereda de Instrumento"""

    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return "Instrumento de Viento: " + super().__str__()


class InstrumentoPercusion(Instrumento):
    """Clase para InstrumentoPercusion. Tipos de Instrumentos. Hereda de Instrumento"""

    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return "Instrumento de Percusion: " + super().__str__()


class InstrumentoElectronico(Instrumento):
    """Clase para InstrumentoElectronico. Tipos de Instrumentos. Hereda de Instrumento"""

    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return "Instrumento de Electronico: " + super().__str__()
