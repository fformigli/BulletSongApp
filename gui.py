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
		self.root.configure(background='#0b121e')

		# menubar
		self.menubar = Menu(self.root)

		# menu headers
		self.menugeneral = Menu(self.menubar,tearoff=0)
		self.menurrhh = Menu(self.menubar,tearoff=0)

		# menu commands
		self.menugeneral.add_command(label="Clientes")
		self.menugeneral.add_command(label="Productos")
		self.menugeneral.add_command(label="Inventario")

		self.menurrhh.add_command(label="Empleados")
		self.menurrhh.add_command(label="Salarios", command=self.view_salarios_general)

		# add menu headers to menu bar
		self.menubar.add_cascade(label="Gestión", menu=self.menugeneral)
		self.menubar.add_cascade(label="RRHH", menu=self.menurrhh)
		self.menubar.add_command(label="Salir", command=self.root.destroy)

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
# 		self.blogin.grid(row=4, columnspan=2)

# 		self.bcancel = ttk.Button(self.frame, text="Cancelar", command=(lambda:self.root.destroy()))
# 		self.bcancel.grid(row=4, column=3)

# 		self.frame.pack()
# 		self.root.mainloop()

if __name__ == '__main__':
	Aplication()