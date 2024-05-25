from datetime import date
from typing import List

class Tesis:
    def __init__(self, nombre_autor: List[str], institucion_academica: str, fecha_investigacion: date, fecha_presentacion: date, campo_estudio: str, estado: str, numero_paginas: int):
        self.nombre_autor = nombre_autor
        self.institucion_academica = institucion_academica
        self.fecha_investigacion = fecha_investigacion
        self.fecha_presentacion = fecha_presentacion
        self.campo_estudio = campo_estudio
        self.estado = estado
        self.numero_paginas = numero_paginas

    def registrar_tesis(self):
        pass  # Implementar lógica

    def buscar_tesis(self):
        pass  # Implementar lógica

    def modificar_tesis(self):
        pass  # Implementar lógica

    def eliminar_tesis(self):
        pass  # Implementar lógica

    def realizar_prestamo_tesis(self):
        pass  # Implementar lógica

    def devolver_tesis(self):
        pass  # Implementar lógica

    def generar_multa(self):
        pass  # Implementar lógica

    def levantar_multa(self):
        pass  # Implementar lógica