from tkinter import ttk
from tkinter import *
from model import *
from controller import *



class Aplication:
	def __init__(self):
		Main(self)


class Main:
	"""Interfaz Principal"""
	def __init__(self, main):
		self.main = main
		self.root = Tk()
		self.root.title("BulletSongApp")
		self.root.geometry("800x400+100+100")

		# menubar
		self.menubar = Menu(self.root)

		# menu headers
		self.menugeneral = Menu(self.menubar,tearoff=0)
		self.menurrhh = Menu(self.menubar,tearoff=0)

		# sub menu
		self.submenu_clientes = Menu(self.menugeneral, tearoff=0)

		# menu commands
		# self.menugeneral.add_command(label="Productos")
		# self.menugeneral.add_command(label="Inventario")

		# self.menurrhh.add_command(label="Empleados")
		self.menurrhh.add_command(label="Salarios", command=self.view_salarios_general)

		self.submenu_clientes.add_command(label="Añadir Clientes", command=self.add_clientes)
		self.submenu_clientes.add_command(label="Ver Clientes", command=lambda:(ClienteController()).view_all(self.root))

		# add menu headers to menu bar and submenes
		self.menugeneral.add_cascade(label="Clientes", menu=self.submenu_clientes)
		self.menubar.add_cascade(label="Gestión", menu=self.menugeneral)
		self.menubar.add_cascade(label="RRHH", menu=self.menurrhh)

		self.menubar.add_command(label="Salir", command=self.root.destroy)

		# self.status = ttk.Label(text="BulletSongApp-0.1").place(relx=0.0, rely=1.0, anchor='sw')

		# add menu bar to window
		self.root.config(menu=self.menubar)
		self.root.mainloop()

	def view_salarios_general(self):
		empleado_controller = EmpleadoController()
		empleado_bonificado_controller = EmpleadoBonificadoController()
		empleado_vendedor_controller = EmpleadoVendedorController()

		empleado_controller.view_salarios(self.root)
		empleado_bonificado_controller.view_salarios(self.root)
		empleado_vendedor_controller.view_salarios(self.root)


	def add_clientes(self):
		cliente_controller = ClienteController()
		cliente_controller.add(self.root)



# sample Login


# class Login:
# 	""" login form"""
# 	def __init__(self, main):
# 		self.main = main
# 		self.root = Tk()
# 		self.root.title("Login")
# 		self.root.geometry("800x600")

# 		self.frame = ttk.Frame(self.root, padding="10 10 5 5")

# 		self.lusername = ttk.Label(self.frame, text="Usuario:")
# 		self.lusername.grid(row=1, column=0, sticky=E)

# 		self.eusername = ttk.Entry(self.frame)
# 		self.eusername.grid(row=1, column=1)
# 		self.eusername.focus()

# 		self.lpassword = ttk.Label(self.frame, text="Contraseña:")
# 		self.lpassword.grid(row=2, column=0)

# 		self.epassword = ttk.Entry(self.frame, show="*")
# 		self.epassword.grid(row=2, column=1, pady=10)

# 		self.root.bind("<Return>", (lambda event:self.authenticate(self)))

# 		self.blogin = ttk.Button(self.frame, text="Entrar", command=(lambda:self.authenticate(self)))
# 		selfself.eruc.get().blogin.grid(row=4, columnspan=2)

# 		self.bcancel = ttk.Button(self.frame, text="Cancelar", command=(lambda:self.root.destroy()))
# 		self.bcancel.grid(row=4, column=3)

# 		self.frame.pack()
# 		self.root.mainloop()

if __name__ == '__main__':
	Aplication()