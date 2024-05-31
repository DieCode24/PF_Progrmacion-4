from datetime import datetime, timedelta
from utils.validators import validar_input
from clases.prestamo import Prestamo
from utils.idgenerator import id_generator

class Multa:
    def __init__(self, id_prestamo, valor_multa):
        self.id_multa = id_generator()
        self.id_prestamo = id_prestamo
        self.dias_retraso = 0
        self.fecha_finalizacion = None
        self.estado = "activa"
        self.valor_multa = valor_multa # Valor en pesos colombianos por día de retraso


    def __str__(self):
        return f"ID: {self.id_multa}\nID Préstamo: {self.id_prestamo}\nDías de retraso: {self.dias_retraso}\nFecha de finalización: {self.fecha_finalizacion}\nEstado: {self.estado}\nValor de la multa: {self.calcular_valor_multa()}"
    
    def idmulta(self):
        return self.id_multa
    
    def idprestamo(self):
        return self.id_prestamo
    
    def diasretraso(self):
        return self.dias_retraso
    
    def fechafinalizacion(self):
        return self.fecha_finalizacion
    
    def estado(self):
        return self.estado
    
    
    def generar_multa(self, fecha_prestamo, fecha_entrega):
        
        #juan manuel me pasa la fecha de prestamo y yo le pido la fecha de devolucion+
        
        fecha_devolucion = validar_input("Ingrese la fecha de devolución (dd/mm/aaaa): ")
        
        
        if fecha_devolucion > fecha_entrega:
            self.dias_retraso = (fecha_devolucion - fecha_entrega).days
            self.fecha_finalizacion = fecha_devolucion + timedelta(days=self.dias_retraso)
        else:
            self.dias_retraso = 0
            self.estado = "inactiva"

    def levantar_multa(self):
        if self.estado == "activa":
            self.estado = "inactiva"
            print(f"La multa con ID {self.id_multa} ha sido levantada.")
        else:
            print(f"La multa con ID {self.id_multa} ya está inactiva.")

    def calcular_dias_retraso(self, fecha_actual):
        if self.estado == "activa":
            fecha_entrega = datetime.strptime(self.fecha_finalizacion, "%Y-%m-%d") - timedelta(days=self.dias_retraso)
            dias_transcurridos = (fecha_actual - fecha_entrega).days
            if dias_transcurridos > self.dias_retraso:
                self.dias_retraso = dias_transcurridos
            return self.dias_retraso
        else:
            return 0

    def calcular_valor_multa(self):
        return self.dias_retraso * self.valor_multa