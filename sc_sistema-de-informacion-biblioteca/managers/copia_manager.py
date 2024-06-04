from managers.data_manager import DataManager
from clases.libro import Estado
from clases.copia import Copia
from utils.idgenerator import id_generator
from utils.helpers import limpiar_consola, pausar_sistema
class CopiaManager():

    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager
        
    def registrar_copias(self, isbn, estado, numero_copias):
        for i in range(numero_copias):
            id = id_generator()
            copia = Copia(isbn, id, estado)
            self.data_manager.copies.append(copia)
        return copia
    
    def eliminar_copia(self, isbn, id):
        copia = self.buscar_copia(isbn, id)
        if copia:
            self.data_manager.copies.remove(copia)
            return copia
        return None
    
    def buscar_copia(self, id):
        if not self.data_manager.copies:
            print("No hay copias registradas.")
            return
        for copia in self.data_manager.copies:
            if copia.id == id:
                return copia
            else:
                print("No se encontró la copia.")
                return None
    
    def listar_copias(self):
        if not self.data_manager.copies:
            print("No hay copias registradas.")
            return
        for copia in self.data_manager.copies:
            print(f"ID: {copia.id}")
            print(f"ISBN: {copia.isbn}")
            print(f"Estado: {copia.estado}")
            print()
            
    def modificar_estado_copia(self, id, estado):
        copia = self.buscar_copia(id)
        if copia:
            copia.estado = estado
            return copia
        return None
    
    def habilitar_copia(self, id):
        if not self.data_manager.copies:
            print("No hay copias registradas.")
            return
        copia = self.buscar_copia(id)
        if copia:
            copia.estado = Estado.DISPONIBLE
            return copia
    
    def inhabilitar_copia(self, id):
        if not self.data_manager.copies:
            print("No hay copias registradas.")
            return
        copia = self.buscar_copia(id)
        if copia:
            copia.estado = Estado.INHABILITADO
            return copia
        return None
    
    def seleccionar_copia(self):
        while True:
            if not self.data_manager.copies:
                limpiar_consola()
                print("No hay copias registradas.")
                pausar_sistema()
                return None

            limpiar_consola()
            print(">. Seleccione una copia:")
            print("Copias:")
            for i, copia in enumerate(self.data_manager.copies):
                print(f"{i + 1}. ID: {copia.id}, ISBN: {copia.isbn}, Estado: {copia.estado}")

            try:
                seleccion = input("Copia: ")
                seleccion = int(seleccion)
                if 1 <= seleccion <= len(self.data_manager.copies):
                    copia_seleccionada = self.data_manager.copies[seleccion - 1]
                    pausar_sistema()
                    limpiar_consola()
                    return copia_seleccionada
                else:
                    print("Opción inválida. Por favor, intente de nuevo.")

            except ValueError:
                print("Opción inválida. Por favor, intente de nuevo.")