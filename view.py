from abc import ABCMeta

from model import Cliente, Empleado, EmpleadoBonificado


class PersonaView(metaclass=ABCMeta):
    """view utilizable por cualquiera de los hijos que heredan"""

    @staticmethod
    def view_get_dato():
        """Solicita parametro para buscar personas por cualquier parametro"""
        return input("Introduzca el dato a buscar entre la informacion:\n")

    @staticmethod
    def view_get_codigo():
        """Solicita Codigo de Persona"""
        return input("Introduzca el codigo del registro que desea eliminar:\n")

    @staticmethod
    def view_all(list):
        """ver todos los elementos de la lista"""
        if list:
            for persona in list:
                print(persona)


class ClienteView(PersonaView):
    """View para los clientes de BulletSongApp"""

    @staticmethod
    def view_add():
        """metodo para agregar clientes"""

        print("Introduzca los datos del nuevo cliente")
        ruc = input("Introduzca el RUC del cliente:\n")
        id_persona = input("Introduzca el codigo de cliente:\n")
        nombre = input("Introduzca el nombre:\n")
        apellido = input("Introduzca el apellido:\n")
        cedula = input("Introduzca la cedula:\n")
        tipo_documento = input("Introduzca el tipo documento:\n")
        nro_telefono = input("Introduzca el nro de telefono:\n")
        fecha_nacimiento = input("Introduzca la fecha de nacimiento:\n")

        return Cliente(ruc, id_persona, nombre, apellido, cedula, tipo_documento, nro_telefono, fecha_nacimiento)


class EmpleadoView(PersonaView):
    """View para empleados de BulletSongApp"""

    @staticmethod
    def view_salario(lista):
        """metodo para imprimir salario uniforme"""

        if lista:
            for empleado in lista:
                print(
                    empleado.id_persona + "\t" + empleado.apellido + ", " + empleado.nombre + "\t" + str(empleado.calculo_salario()))

    @staticmethod
    def view_add():
        """metodo para agregar empleados"""

        id_persona = input("Introduzca el codigo de Empleado:\n")
        nombre = input("Introduzca el nombre:\n")
        apellido = input("Introduzca el apellido:\n")
        cedula = input("Introduzca la cedula:\n")
        tipo_documento = input("Introduzca el tipo documento:\n")
        nro_telefono = input("Introduzca el nro de telefono:\n")
        fecha_nacimiento = input("Introduzca la fecha de nacimiento:\n")
        fecha_contrato = input("Introduzca la fecha de contrato:\n")
        salario = input("Introduzca el salario base:\n")

        return Empleado(fecha_contrato, salario, id_persona, nombre, apellido, cedula, tipo_documento, nro_telefono,
                        fecha_nacimiento)


class EmpleadoBonificadoView(PersonaView):
    """View para empleados bonificados de BulletSongApp"""

    @staticmethod
    def view_salario(lista):
        """metodo para imprimir salario uniforme"""

        if lista:
            for empleado in lista:
                print(
                    empleado.id_persona + "\t" + empleado.apellido + ", " + empleado.nombre + "\t" + str(empleado.calculo_salario()))

    @staticmethod
    def view_add():
        """metodo para agregar empleados bonificados"""

        id_persona = input("Introduzca el codigo de Empleado:\n")
        nombre = input("Introduzca el nombre:\n")
        apellido = input("Introduzca el apellido:\n")
        cedula = input("Introduzca la cedula:\n")
        tipo_documento = input("Introduzca el tipo documento:\n")
        nro_telefono = input("Introduzca el nro de telefono:\n")
        fecha_nacimiento = input("Introduzca la fecha de nacimiento:\n")

        fecha_contrato = input("Introduzca la fecha de contrato:\n")
        salario = input("Introduzca el salario base:\n")
        bonificacion = input("Introduzca el monto de bonificacion:\n")

        return EmpleadoBonificado(bonificacion, fecha_contrato, salario, id_persona, nombre, apellido, cedula,
                                  tipo_documento, nro_telefono,
                                  fecha_nacimiento)
