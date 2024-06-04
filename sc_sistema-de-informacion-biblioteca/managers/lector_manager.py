from typing import List, Optional
from clases.lector import Lector
from clases.estado import Estado
from utils.helpers import limpiar_consola, pausar_sistema
from utils.validators import validar_input

class LectorManager:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def registrar_lector(self):
        """
        Registra un nuevo lector en el sistema.
        """
        nombre = validar_input("Ingrese el nombre del lector: ", str).title()
        telefono = validar_input("Ingrese el número de teléfono del lector: ", int)
        direccion = validar_input("Ingrese la dirección del lector: ", str).title()
        estado = Estado.NORMAL

        lector = Lector(nombre, telefono, direccion, estado)
        self.data_manager.lectores.append(lector)
        print(f"Lector {nombre} registrado exitosamente.")
        limpiar_consola()

    def buscar_lector(self, id: int) -> Optional[Lector]:
        """
        Busca un lector por su ID.

        :param id: ID del lector a buscar.
        :return: El objeto Lector si se encuentra, de lo contrario None.
        """
        for lector in self.data_manager.lectores:
            if lector.id == id:
                return lector
        return None

    def modificar_lector(self):
        """
        Modifica la información de un lector existente.
        """
        lectores = self.data_manager.lectores
        if not lectores:
            print("No hay lectores registrados.")
            return

        print("Seleccione el lector que desea modificar:")
        for i, lector in enumerate(lectores, start=1):
            print(f"{i}. {lector.nombre}")

        opcion = validar_input("Ingrese el número del lector: ", int)
        if opcion < 1 or opcion > len(lectores):
            print("Opción inválida.")
            return

        lector = lectores[opcion - 1]
        print(f"Información actual del lector {lector.nombre}:")
        print(f"ID: {lector.id}, Nombre: {lector.nombre}, Teléfono: {lector.telefono}, Dirección: {lector.direccion}, Estado: {lector.estado}")

        nuevo_nombre = validar_input(f"Ingrese el nuevo nombre (actual: {lector.nombre}): ", str) or lector.nombre
        nuevo_telefono = validar_input(f"Ingrese el nuevo número de teléfono (actual: {lector.telefono}): ", int) or lector.telefono
        nueva_direccion = validar_input(f"Ingrese la nueva dirección (actual: {lector.direccion}): ", str) or lector.direccion

        lector.actualizar_informacion(nuevo_nombre, nuevo_telefono, nueva_direccion)
        print("Lector modificado exitosamente.")
        
    def actualizar_informacion(self, id: int, nuevo_nombre: str, nuevo_telefono: int, nueva_direccion: str):
        """
        Actualiza la información de un lector existente.

        :param id: ID del lector a actualizar.
        :param nuevo_nombre: Nuevo nombre del lector.
        :param nuevo_telefono: Nuevo número de teléfono del lector.
        :param nueva_direccion: Nueva dirección del lector.
        :raise ValueError: Si el lector no se encuentra.
        """
        lector = self.buscar_lector(id)
        if lector:
            lector.actualizar_informacion(nuevo_nombre, nuevo_telefono, nueva_direccion)
            print(f"Información del lector {lector.nombre} actualizada exitosamente.")
        else:
            raise ValueError("Lector no encontrado")

    def habilitar_lector(self, id: int):
        """
        Habilita a un lector.

        :param id: ID del lector a habilitar.
        :raise ValueError: Si el lector no se encuentra.
        """
        lector = self.buscar_lector(id)
        if lector:
            lector.rehabilitar()
            print(f"\nLector {lector.nombre} habilitado exitosamente.")
        else:
            raise ValueError("Lector no encontrado")

    def inhabilitar_lector(self, id: int):
        """
        Inhabilita a un lector.

        :param id: ID del lector a inhabilitar.
        :raise ValueError: Si el lector no se encuentra.
        """
        lector = self.buscar_lector(id)
        if lector:
            lector.suspender()
            print(f"\nLector {lector.nombre} inhabilitado exitosamente.")
        else:
            raise ValueError("Lector no encontrado")

    def listar_lectores(self):
        """
        Lista todos los lectores registrados en el sistema.
        """
        if not self.data_manager.lectores:
            input("\n> No hay lectores registrados.")
            return
        for lector in self.data_manager.lectores:
            print(f"\nID: {lector.get_id()}, Nombre: {lector.get_nombre()}, Teléfono: {lector.get_telefono()}, Dirección: {lector.get_direccion()}, Estado: {lector.get_estado()}")
        pausar_sistema()

    def seleccionar_lector(self):
        while True:
            if not self.data_manager.lectores:
                limpiar_consola()
                print("\n> No hay lectores registrados.")
                self.registrar_lector()
                pausar_sistema()

            limpiar_consola()
            print("> Seleccione un lector:")
            print("Lectores:")
            for i, lector in enumerate(self.data_manager.lectores):
                print(f"{i + 1}. {lector.nombre} ({lector.id})")

            try:
                seleccion = input("Lector: ")
                seleccion = int(seleccion)
                if 1 <= seleccion <= len(self.data_manager.lectores):
                    lector_seleccionado = self.data_manager.lectores[seleccion - 1]
                    pausar_sistema()
                    limpiar_consola()
                    return lector_seleccionado
                else:
                    print("Opción inválida. Por favor, intente de nuevo.")

            except ValueError:
                print("Opción inválida. Por favor, intente de nuevo.")