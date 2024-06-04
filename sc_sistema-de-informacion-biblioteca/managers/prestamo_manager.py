from datetime import date
from typing import List, Optional
from clases.prestamo import Prestamo
from datetime import timedelta
from utils.validators import validar_input
from utils.idgenerator import id_generator
from managers.data_manager import DataManager

class PrestamoManager:
    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager

    def registrar_prestamo(self, lectores, libros):
        lectores.listar_lectores()
        id_lector= validar_input("Ingrese el ID del lector: ", int)
        lector = lectores.buscar_lector(id_lector)
        libros.listado_libros()
        id_libro = validar_input("Ingrese el ISBN del libro: ", str)
        libro = libros.buscar_libro(id_libro)
        id_lector = lectores.get_IdLector()
        id_libro = libros.get_IdLibro()
        fecha_prestamo = date.today()
        fecha_devolucion = self.calcular_fecha_entrega(fecha_prestamo)
        nuevo_prestamo = Prestamo(id_lector, id_libro, fecha_prestamo, fecha_devolucion)
        self.prestamos.append(nuevo_prestamo)

    def consultar_prestamo(self, id_prestamo: int):
        for prestamo in self.prestamos:
            if prestamo.get_IdPrestamo() == id_prestamo:
                return prestamo
        return None

    def calcular_fecha_entrega(self, fecha_prestamo: date, dias_prestamo: int = 3) -> date:
        return fecha_prestamo + timedelta(days=dias_prestamo)
        