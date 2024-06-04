from datetime import date
from utils.idgenerator import id_generator
from clases.estado import Estado
from datetime import timedelta,  date


class Prestamo:
    def __init__(self,  id_lector: int, id_libro: str, fecha_prestamo: date, fecha_devolucion: date):
        self._id_prestamo = id_generator()
        self._id_lector = id_lector
        self._id_libro = id_libro
        self.dias_prestamo = 0 #la diferencia que hay entre la fecha de devolucion y la fecha de entrega
        
        self._fecha_prestamo = date.today() #fecha de cuando se hace el prestamo
        self._fecha_entrega = self.calcular_fecha_entrega(self, 3) #fecha de entrega mas 3 dias
        self._fecha_devolucion = fecha_devolucion  #fecha en cuando se devolvio
        
    def calcular_fecha_entrega(self, dias_prestamo) -> date:
        return self._fecha_prestamo + timedelta(days=dias_prestamo)
    
    
    
    def IdPrestamo(self):
        return self._id_prestamo
    
    def set_IdPrestamo(self, id_prestamo):
        self._id_prestamo = id_prestamo
        
    def IdLector(self):
        return self._id_lector
    
    def set_IdLector(self, id_lector):
        self._id_lector = id_lector
        
    def IdLibro(self):
        return self._id_libro
    
    def set_IdLibro(self, id_libro):
        self._id_libro = id_libro
        
    def FechaPrestamo(self):
        return self._fecha_prestamo
    
    def set_FechaPrestamo(self, fecha_prestamo):
        self._fecha_prestamo = fecha_prestamo
        
    def FechaDevolucion(self):
        return self._fecha_devolucion
    
    def set_FechaDevolucion(self, fecha_devolucion):
        self._fecha_devolucion = fecha_devolucion
        