from clases.prestamo import Prestamo
from utils.idgenerator import id_generator
from datetime import date
from datetime import datetime, timedelta
from typing import List, Optional
from utils.validators import validar_input

class PrestamoManager:
    def __init__(self):
        self.prestamos = []

    def registrar_prestamo(self, lector, libro):
        id_prestamo = id_generator()
        fecha_prestamo = date.today()
        fecha_devolucion = self.calcular_fecha_entrega(fecha_prestamo)
        nuevo_prestamo = Prestamo(id_prestamo, id_lector, id_libro, fecha_prestamo, fecha_devolucion)
        self.prestamos.append(nuevo_prestamo)
        return nuevo_prestamo

    def consultar_prestamo(self, id_prestamo: int) -> Optional[Prestamo]:
        for prestamo in self.prestamos:
            if prestamo.get_IdPrestamo() == id_prestamo:
                return prestamo
        return None

    def calcular_fecha_entrega(self, fecha_prestamo: date, dias_prestamo: int = 3) -> date:
        return fecha_prestamo + timedelta(days=dias_prestamo)
        