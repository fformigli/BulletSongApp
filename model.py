from interface import *


class TiendaMusical:
    def __init__(self):
        self.nombre = "BulletSong"


class Persona(metaclass=ABCMeta):
    """Clase abstracta datos basicos de personas"""

    def __init__(self, id_persona, nombre, apellido, nro_documento, tipo_documento, nro_telefono, fecha_nacimiento):
        self.idPersona = id_persona
        self.nombre = nombre
        self.apellido = apellido
        self.nroDocumento = nro_documento
        self.tipoDocumento = tipo_documento
        self.nroTelefono = nro_telefono
        self.fechaNacimiento = fecha_nacimiento

    def __str__(self):
        return "(" + self.nroDocumento + ") " + self.nombre + " " + self.apellido


class Cliente(Persona):
    """Clase que representa a los Clientes de la tienda. Hereda Persona"""

    def __init__(self, ruc, *args):
        super().__init__(*args)
        self.ruc = ruc

    def __str__(self):
        return "Cliente:" + super().__str__() + " RUC: " + self.ruc


class Empleado(Persona):
    """Clase para empleados. Solo cobran salario fijo. Hereda de Persona"""

    def __init__(self, fecha_contrato, salario, *args):
        super().__init__(*args)
        self.fechaContrato = fecha_contrato
        self.salario = salario

    def calculo_salario(self):
        return self.salario

    def __str__(self):
        return super().__str__() + " Contratado el: " + self.fechaContrato + "  Salario: " + str(self.salario)


class EmpleadoVendedor(Empleado):
    """Clase para vendedores. Los vendedores cobran una comision por venta ademas de su salario. Hereda de Empleado"""

    def __init__(self, comision, *args):
        super().__init__(*args)
        self.comision = comision

    def calculo_salario(self):
        return super().salario + super().salario * self.comision

    def __str__(self):
        return super().__str__() + " Comision: " + self.comision


class EmpleadoBonificacion(Empleado):
    """Clase para empleados con bonificacion (por ejemplo por exposicion a riesgos). Hereda de Empleado"""

    def __init__(self, bonificacion, *args):
        super().__init__(*args)
        self.bonificacion = bonificacion

    def calculo_salario(self):
        return super().calculo_salario() + self.bonificacion

    def __str__(self):
        return super().__str__() + " Bonificacion: " + str(self.bonificacion)


class Producto(metaclass=ABCMeta):
    """Clase abstracta para productos"""

    def __init__(self, id_producto, marca, stock, categoria, descripcion, nombre):
        self.idProducto = id_producto
        self.marca = marca
        self.stock = stock
        self.categoria = categoria
        self.descripcion = descripcion
        self.nombre = nombre

    def __str__(self):
        return self.categoria + " " + self.marca + " " + self.nombre + "\n\t" + self.descripcion


class Accesorio(Producto, Vendible):
    """Clase para Accesorio. productos que solo se pueden vender. Hereda de Producto"""

    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return "Accesorio: " + super().__str__()

    def vender(self):
        pass


class Repuesto(Producto, Vendible):
    """Clase para Repuesto. productos que solo se pueden vender. Hereda de Producto"""

    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return "Repuesto: " + super().__str__()

    def vender(self):
        pass


class Instrumento(Producto, Alquilable, Vendible, metaclass=ABCMeta):
    """Clase Abstracta para Instrumentos. Hereda de Producto"""

    def __init__(self, *args):
        super().__init__(*args)

    def alquilar(self):
        return 10000 + super().multa

    def vender(self):
        return "vendido"


class InstrumentoCuerda(Instrumento):
    """Clase para InstrumentoCuerda. Tipos de Instrumentos. Hereda de Instrumento"""

    def __init__(self, cantidad_cuerdas, *args):
        super().__init__(*args)
        self.cantidadCuerdas = cantidad_cuerdas

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
