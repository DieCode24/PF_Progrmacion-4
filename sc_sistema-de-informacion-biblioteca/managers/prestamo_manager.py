from clases.prestamo import Prestamo
from utils.idgenerator import id_generator
from datetime import date
from utils.validators import validar_input

class PrestamoManager:
    def __init__(self):
        self.prestamos = []
        
        
    def registrar_prestamo(self):
        id_prestamo = id_generator()
        id_lector = validar_input("Ingrese el id del lector: ", int)
        