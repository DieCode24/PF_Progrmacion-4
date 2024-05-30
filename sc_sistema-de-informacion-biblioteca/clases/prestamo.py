from datetime import date
from typing import List


class Prestamo:
    def __init__(self, id_prestamo: int,  id_lector: int, id_libro: int, fecha_prestamo: date, fecha_devolucion: date):
        self._id_prestamo = id_prestamo
        self._id_lector = id_lector
        self._id_libro = id_libro
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion
        
    def get_IdPrestamo(self):
        return self._id_prestamo
    
    def set_IdPrestamo(self, id_prestamo):
        self._id_prestamo = id_prestamo
        
    def get_IdLector(self):
        return self._id_lector
    
    def set_IdLector(self, id_lector):
        self._id_lector = id_lector
        
    def get_IdLibro(self):
        return self._id_libro
    
    def set_IdLibro(self, id_libro):
        self._id_libro = id_libro
        
    def get_FechaPrestamo(self):
        return self._fecha_prestamo
    
    def set_FechaPrestamo(self, fecha_prestamo):
        self._fecha_prestamo = fecha_prestamo
        
    def get_FechaDevolucion(self):
        return self._fecha_devolucion
    
    def set_FechaDevolucion(self, fecha_devolucion):
        self._fecha_devolucion = fecha_devolucion
        