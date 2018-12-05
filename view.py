from tkinter import *
from tkinter import ttk, messagebox

from model import *


def clear_frame(frame):
    for w in frame.winfo_children():
        w.destroy()


class PersonaView(metaclass=ABCMeta):
    """view utilizable por cualquiera de los hijos que heredan"""

    @staticmethod
    def view_get_dato():
        """Solicita parametro para buscar personas por cualquier parametro"""
        return input("Introduzca el dato a buscar entre la informacion:\n")

    @staticmethod
    def view_get_codigo():
        """Solicita Codigo de Persona"""
        return input("Introduzca el codigo del registro:\n")

    @staticmethod
    def view_all(frame, lista):
        """ver todos los elementos de la lista"""

        clear_frame(frame)

        Label(frame, text='Cod', relief=RIDGE, anchor="w", width=5, bg='dark grey').grid(row=0, column=0, sticky=W)
        Label(frame, text='Nombre', relief=RIDGE, anchor="w", width=40, bg='dark grey').grid(row=0, column=1, sticky=W)
        Label(frame, text='RUC', relief=RIDGE, anchor="w", width=10, bg='dark grey').grid(row=0, column=2, sticky=W)
        Label(frame, text='Nro. Telefono', relief=RIDGE, anchor="w", width=10, bg='dark grey').grid(row=0, column=3,
                                                                                                    sticky=W)
        Label(frame, text='Fec. Nac.', relief=RIDGE, anchor="w", width=10, bg='dark grey').grid(row=0, column=4,
                                                                                                sticky=W)
        Label(frame, text='Tipo Documento', relief=RIDGE, anchor="w", width=20, bg='dark grey').grid(row=0, column=5,
                                                                                                     sticky=W)
        Label(frame, text='Nro. Documento', relief=RIDGE, anchor="w", width=20, bg='dark grey').grid(row=0, column=6,
                                                                                                     sticky=W)

        if lista:
            cc = 0
            for persona in lista:
                cc += 1
                Label(frame, text='%s' % persona.id_persona, relief=RIDGE, anchor="w", width=5).grid(row=cc, column=0,
                                                                                                     sticky=W)
                Label(frame, text='%s, %s' % (persona.apellido, persona.nombre), relief=RIDGE, anchor="w",
                      width=40).grid(row=cc, column=1, sticky=W)
                Label(frame, text='%s' % persona.ruc, relief=RIDGE, anchor="w", width=10).grid(row=cc, column=2,
                                                                                               sticky=W)
                Label(frame, text='%s' % persona.nro_telefono, relief=RIDGE, anchor="w", width=10).grid(row=cc,
                                                                                                        column=3,
                                                                                                        sticky=W)
                Label(frame, text='%s' % persona.fecha_nacimiento, relief=RIDGE, anchor="w", width=10).grid(row=cc,
                                                                                                            column=4,
                                                                                                            sticky=W)
                Label(frame, text='%s' % persona.tipo_documento, relief=RIDGE, anchor="w", width=20).grid(row=cc,
                                                                                                          column=5,
                                                                                                          sticky=W)
                Label(frame, text='%s' % persona.nro_documento, relief=RIDGE, anchor="w", width=20).grid(row=cc,
                                                                                                         column=6,
                                                                                                         sticky=W)

        frame.pack()


def create_cliente(frame, eruc, eid_persona, enombre, eapellido, enrodocumento, combobox, enrotelefono,
                   efecnacimiento):
    """crea el cliente a partir de lo cargado en el formulario"""
    print("adding cliente")
    Cliente.save(
        Cliente(eruc.get(), eid_persona.get(), enombre.get(), eapellido.get(), enrodocumento.get(), combobox.get(),
                enrotelefono.get(), efecnacimiento.get()))

    msg_guardado(frame)


def msg_guardado(frame):
    clear_frame(frame)
    messagebox.showinfo(message="Agregado Exitosamente!!")


class ClienteView(PersonaView):
    """View para los clientes de BulletSongApp"""

    @staticmethod
    def view_add(frame):
        """metodo para agregar clientes"""

        clear_frame(frame)

        (ttk.Label(frame, text="Agregar Clientes")).grid(row=0, column=1, columnspan=2, pady=10)

        (ttk.Label(frame, text="ID Persona", anchor="w", width=20)).grid(row=2, column=1)
        eid_persona = ttk.Entry(frame)
        eid_persona.grid(row=2, column=2)

        (ttk.Label(frame, text="Nombre", anchor="w", width=20)).grid(row=3, column=1)
        enombre = ttk.Entry(frame)
        enombre.grid(row=3, column=2)

        (ttk.Label(frame, text="Apellido", anchor="w", width=20)).grid(row=4, column=1)
        eapellido = ttk.Entry(frame)
        eapellido.grid(row=4, column=2)

        (ttk.Label(frame, text="RUC", anchor="w", width=20)).grid(row=5, column=1)
        eruc = ttk.Entry(frame)
        eruc.grid(row=5, column=2)

        (ttk.Label(frame, text="Tipo de Documento", anchor="w", width=20)).grid(row=6, column=1)
        combobox = ttk.Combobox(frame, state='readonly')
        combobox['values'] = ["Cedula de Identidad Paraguaya", "Pasaporte", "Otro"]
        combobox.grid(row=6, column=2)

        (ttk.Label(frame, text="Nro. Documento", anchor="w", width=20)).grid(row=7, column=1)
        enrodocumento = ttk.Entry(frame)
        enrodocumento.grid(row=7, column=2)

        (ttk.Label(frame, text="Nro. de Telefono", anchor="w", width=20)).grid(row=8, column=1)
        enrotelefono = ttk.Entry(frame)
        enrotelefono.grid(row=8, column=2)

        (ttk.Label(frame, text="Fecha de Nacimiento", anchor="w", width=20)).grid(row=9, column=1)
        efecnacimiento = ttk.Entry(frame)
        efecnacimiento.grid(row=9, column=2)

        # frame.bind("<Return>", (lambda event: create_cliente()))

        Button(frame, text="Guardar", command=lambda: create_cliente(frame,eruc, eid_persona, enombre,
                                                                     eapellido, enrodocumento, combobox,
                                                                     enrotelefono, efecnacimiento)).grid(row=10,
                                                                                                         column=1,
                                                                                                         pady=20)

        Button(frame, text="Cancelar", command=lambda: clear_frame(frame)).grid(row=10, column=2, pady=20)

        frame.pack()


class EmpleadoView(PersonaView):
    """View para empleados de BulletSongApp"""

    @staticmethod
    def view_salario(frame, lista):
        """metodo para imprimir salario uniforme"""

        clear_frame(frame)

        Label(frame, text='Cod', relief=RIDGE, anchor="w", width=20, bg='dark grey').grid(row=0, column=0, sticky=W)
        Label(frame, text='Nombre', relief=RIDGE, anchor="w", width=40, bg='dark grey').grid(row=0, column=1, sticky=W)
        Label(frame, text="Salario por Categoria", relief=RIDGE, anchor="w", width=40, bg='dark grey').grid(row=0,
                                                                                                            column=2,
                                                                                                            sticky=W)

        if lista:
            cc = 0
            for empleado in lista:
                cc += 1
                Label(frame, text='%s' % empleado.id_persona, relief=RIDGE, anchor="w", width=20).grid(row=cc,
                                                                                                       column=0,
                                                                                                       sticky=W)
                Label(frame, text='%s, %s' % (empleado.apellido, empleado.nombre), relief=RIDGE, anchor="w",
                      width=40).grid(row=cc, column=1, sticky=W)
                Label(frame, text='%s' % (str(empleado.calculo_salario())), relief=RIDGE, anchor="w", width=40).grid(
                    row=cc, column=2, sticky=W)
        frame.pack()

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


class EmpleadoBonificadoView(EmpleadoView):
    """View para empleados bonificados de BulletSongApp"""

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


class EmpleadoVendedorView(EmpleadoView):
    """View para empleados con comision de BulletSongApp"""

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
        comision = input("Introduzca el porcentaje de comisión:\n")

        return EmpleadoVendedor(comision, fecha_contrato, salario, id_persona, nombre, apellido, cedula,
                                tipo_documento, nro_telefono,
                                fecha_nacimiento)


class ProductoView:
    """View para productos"""

    # TODO: metodo view_vender()
    @staticmethod
    def view_all(lista):
        """metodo para imprimir productos"""
        print("-----------------------------------------")
        if lista:
            for producto in lista:
                print(str(producto.id_producto) + "\t" + str(producto.categoria) + "\t" + str(
                    producto.marca) + "\t" + str(producto.nombre) + "\t" + str(producto.stock) + "\t" + str(
                    producto.precio_venta))


class InstrumentoView(ProductoView):
    """View para Instrumentos"""
    # TODO: metodo view_alquilar()


class InstrumentoCuerdaView(InstrumentoView):
    """ View para gestion de datos de instrumentos de cuerda"""

    @staticmethod
    def view_add():
        """ Metodo para agregar instrumentos de cuerda"""

        id_producto = input("Introduzca el codigo del producto:\n")
        marca = input("Introduzca la marca:\n")
        stock = input("Introduzca la cantidad existente:\n")
        categoria = input("Introduzca la categoria:\n")
        descripcion = input("Introduzca la descripcion:\n")
        nombre = input("Introduzca el nombre:\n")
        precio_venta = input("Introduzca el precio de venta:\n")
        precio_alquiler = input("Introduzca el precio de alquiler:\n")
        plazo_alquiler = input("Introduzca el plazo sin multa de alquiler:\n")
        multa = input("Introduzca la multa para plazo vencido:\n")
        cantidad_cuerdas = input("Introduzca la cantidad de cuerdas:\n")

        return InstrumentoCuerda(cantidad_cuerdas, id_producto, marca, stock, categoria, descripcion, nombre,
                                 precio_venta, precio_alquiler, plazo_alquiler, multa)
