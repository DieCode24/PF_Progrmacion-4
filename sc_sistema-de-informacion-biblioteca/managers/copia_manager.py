from managers.data_manager import DataManager
from clases.libro import Estado
from clases.copia import Copia
from utils.idgenerator import id_generator
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