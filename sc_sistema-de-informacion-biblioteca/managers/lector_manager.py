from typing import List, Optional
from clases.lector import Lector
from clases.estado import Estado
from utils.helpers import limpiar_consola, pausar_sistema
from managers.data_manager import DataManager

class LectorManager:
    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager

    def registrar_lector(self, nombre: str, id: int, telefono: str, direccion: str, estado: str = Estado.NORMAL):
        """
        Registra un nuevo lector en el sistema.

        :param nombre: Nombre del lector.
        :param id: ID del lector.
        :param telefono: Número de teléfono del lector.
        :param direccion: Dirección del lector.
        :param estado: Estado del lector (opcional, por defecto es 'Normal').
        :return: El objeto Lector recién creado.
        """
        lector = Lector(nombre, id, telefono, direccion, estado)
        self.data_manager.lectores.append(lector)
        return lector

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

    def modificar_lector(self, id: int, **kwargs):
        """
        Modifica la información de un lector existente.

        :param id: ID del lector a modificar.
        :param kwargs: Diccionario de atributos a actualizar.
        :return: El objeto Lector modificado.
        :raise ValueError: Si el lector no se encuentra.
        """
        lector = self.buscar_lector(id)
        if lector:
            lector.actualizar_informacion(**kwargs)
            return lector
        else:
            raise ValueError("Lector no encontrado")

    def habilitar_lector(self, id: int):
        """
        Habilita a un lector.

        :param id: ID del lector a habilitar.
        :raise ValueError: Si el lector no se encuentra.
        """
        lector = self.buscar_lector(self, id)
        if lector:
            lector.rehabilitar()
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
        else:
            raise ValueError("Lector no encontrado")

    def listar_lectores(self) -> List[Lector]:
        """
        Lista todos los lectores registrados en el sistema.

        :return: Lista de objetos Lector.
        """
        return self.lectores

    def registrar_lector_desde_consola(self):
        """
        Registra un nuevo lector desde la consola, solicitando datos al usuario.
        """
        nombre = input("Ingrese el nombre del lector: ")
        id = int(input("Ingrese el ID del lector: "))
        telefono = input("Ingrese el número de teléfono del lector: ")
        direccion = input("Ingrese la dirección del lector: ")
        estado = Estado.NORMAL

        lector = self.registrar_lector(nombre, id, telefono, direccion, estado)
        input(f"Lector registrado: {lector}")
        

    def buscar_lector_desde_consola(self):
        """
        Busca un lector desde la consola, solicitando el ID al usuario.
        """
        id_lector = int(input("Ingrese el ID del lector a buscar: "))
        lectores_encontrados = self.buscar_lector(id_lector)

        if lectores_encontrados:
            print(lectores_encontrados)
            input("")
            
        else:
            print("No se encontró ningún lector con ese ID.")

    def modificar_lector_desde_consola(self):
        """
        Modifica un lector desde la consola, solicitando el ID y los nuevos datos al usuario.
        """
        id_lector = int(input("Ingrese el ID del lector a modificar: "))
        lector_a_modificar = self.buscar_lector( id_lector)

        if lector_a_modificar:
            nuevo_nombre = input("Ingrese el nuevo nombre del lector (dejar en blanco para no cambiar): ")
            nuevo_telefono = input("Ingrese el nuevo número de teléfono del lector (dejar en blanco para no cambiar): ")
            nueva_direccion = input("Ingrese la nueva dirección del lector (dejar en blanco para no cambiar): ")

            kwargs = {}
            if nuevo_nombre:
                kwargs['nombre'] = nuevo_nombre
            if nuevo_telefono:
                kwargs['telefono'] = nuevo_telefono
            if nueva_direccion:
                kwargs['direccion'] = nueva_direccion

            lector_modificado = self.modificar_lector( id_lector, **kwargs)
            print("Lector modificado exitosamente.")
        else:
            print("No se encontró ningún lector con ese ID.")
            
            
    def seleccionar_lector(self):
        while True:
            if not self.data_manager.lectores:
                limpiar_consola()
                print("No hay lectores registrados.")
                self.registrar_lector_desde_consola()
                pausar_sistema()

            limpiar_consola()
            print(">. Seleccione un lector:")
            print("0. Registrar un nuevo lector")
            print("Lectores:")
            for i, lector in enumerate(self.data_manager.lectores):
                print(f"{i + 1}. {lector.nombre} ({lector.id})")

            try:
                seleccion = input("Lector: ")
                seleccion = int(seleccion)
                if seleccion == 0:
                    self.registrar_lector_desde_consola()
                elif 1 <= seleccion <= len(self.data_manager.lectores):
                    lector_seleccionado = self.data_manager.lectores[seleccion - 1]
                    pausar_sistema()
                    limpiar_consola()
                    return lector_seleccionado
                else:
                    print("Opción inválida. Por favor, intente de nuevo.")

            except ValueError:
                print("Opción inválida. Por favor, intente de nuevo.")