#from model import Model
#from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def agregar_persona(self):
        persona = self.view.vistaAgregarPersona()
        self.model.guardarPersona(persona)
