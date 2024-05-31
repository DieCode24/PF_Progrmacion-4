from datetime import datetime, timedelta

class Multa:
    def __init__(self, id_multa, id_prestamo):
        self.id_multa = id_multa
        self.id_prestamo = id_prestamo
        self.dias_retraso = 0
        self.fecha_finalizacion = None
        self.estado = "activa"
        self.valor_multa = 3000  # Valor en pesos colombianos por día de retraso

    def generar_multa(self):
        # Solicitar al usuario la fecha de préstamo y devolución
        fecha_prestamo_str = input("Ingrese la fecha de préstamo (dd/mm/aaaa): ")
        fecha_devolucion_str = input("Ingrese la fecha de devolución (dd/mm/aaaa): ")

        # Convertir las cadenas de texto a objetos datetime
        fecha_prestamo = datetime.strptime(fecha_prestamo_str, "%d/%m/%Y")
        fecha_devolucion = datetime.strptime(fecha_devolucion_str, "%d/%m/%Y")

        # Calcular la fecha de entrega y los días de retraso
        fecha_entrega = fecha_prestamo + timedelta(days=3)
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