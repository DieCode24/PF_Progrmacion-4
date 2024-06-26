from datetime import date
from typing import List, Optional
from clases.prestamo import Prestamo, PrestamoBiblioteca
from datetime import timedelta
from utils.validators import validar_input
from utils.idgenerator import id_generator
from managers.data_manager import DataManager
from utils.helpers import pausar_sistema, limpiar_consola
import clases.estado as estados

class PrestamoManager:
    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager

    def registrar_prestamo(self, lectores, copia, tesis, articulo):
        while True:
            print("Seleccione el tipo de material a prestar")
            print("1. Libro")
            print("2. Tesis")
            print("3. Artículo")
            print("0. Salir")
            op = validar_input("\n> Ingrese una opción => ", int)
            
            if op == 1:
                self.registrar_prestamo_libro(lectores, copia)
            elif op == 2:
                self.registrar_prestamo_tesis(lectores, tesis)
            elif op == 3:
                self.registrar_prestamo_articulo(lectores, articulo)
            elif op == 0:
                return
            else:
                print("Opción no válida")
                return

    def registrar_prestamo_libro(self, lectores, copia):
        lector = lectores.seleccionar_lector()
        copy = copia.seleccionar_copia()
        if copy is None:
            print("La copia no existe")
            return
        if copy.estado() == "inhabilitado":
            print("La copia no está habilitada")
            return
        prestamo = Prestamo(lector.get_id(), copy.id())
        self.data_manager.prestamos.append(prestamo)
        print("Préstamo registrado exitosamente")
        pausar_sistema()
        
    def registrar_prestamo_tesis(self, lectores, tesis):
        lector = lectores.seleccionar_lector()
        tesis = tesis.seleccionar_tesis()
        if tesis is None:
            print("La tesis no existe")
            return
        
        if tesis.estado() == "PRESTADO" or tesis.estado() == "EN REPARACION" or tesis.estado() == "EN REVISION":
            print("La tesis no está disponible para préstamo")
            return
        prestamo = Prestamo(lector.get_id(), tesis.id())
        self.data_manager.prestamos.append(prestamo)
        estado = estados.Estado.PRESTADO
        tesis.set_Estado(estado)
        print("Préstamo registrado exitosamente")
        
    def registrar_prestamo_articulo(self, lectores, articulo):
        lector = lectores.seleccionar_lector()
        articulo = articulo.seleccionar_articulo()
        if articulo is None:
            print("El artículo no existe")
            return
        if articulo.estado() == "PRESTADO" or articulo.estado() == "EN REPARACION" or articulo.estado() == "EN REVISION":
            print("El artículo no está disponible para préstamo")
            return
        prestamo = Prestamo(lector.get_id(), articulo.id())
        self.data_manager.prestamos.append(prestamo)
        estado = estados.Estado.PRESTADO
        articulo.set_Estado(estado)
        print("Préstamo registrado exitosamente")
        
    def consultar_prestamo(self, id_prestamo: int):
        for prestamo in self.data_manager.prestamos:
            if prestamo.get_IdPrestamo() == id_prestamo:
                return prestamo
        return None
    

    def calcular_fecha_entrega(self, fecha_prestamo: date, dias_prestamo: int = 3) -> date:
        return fecha_prestamo + timedelta(days=dias_prestamo)
        