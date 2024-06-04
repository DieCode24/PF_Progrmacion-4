import threading
from dotenv import load_dotenv

from managers.libro_manager import LibroManager
from managers.articulo_cientifico_manager import ArticuloCientificoManager
from managers.tesis_manager import TesisManager
from managers.autor_manager import AutorManager
from managers.copia_manager import CopiaManager
from managers.lector_manager import LectorManager
from managers.data_manager import DataManager
from managers.prestamo_manager import PrestamoManager
from managers.categoria_manager import CategoriaManager
from menu import AdminMenu, LibrarianMenu, ReaderMenu
from utils.helpers import pausar_sistema, limpiar_consola, print_brand_sistema, separador_en_consola, validar_contraseña

load_dotenv()
class DependencyContainer:
    _instance = None
    _lock = threading.Lock()
    
    def __init__(self, data_manager):
        self.data_manager = data_manager
        self.libro_manager = LibroManager(data_manager)
        self.articulo_manager = ArticuloCientificoManager(data_manager)
        self.autor_manager = AutorManager(data_manager)
        self.tesis_manager = TesisManager(data_manager)
        self.lector_manager = LectorManager(data_manager)
        self.copy_manager = CopiaManager(data_manager)
        self.prestamo_manager = PrestamoManager(data_manager)
        self.lector_manager = LectorManager(data_manager)
        self.categoria_manager = CategoriaManager(data_manager)

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance
    
def main():
    data_manager = DataManager()
    container = DependencyContainer(data_manager)
    
    limpiar_consola()
    while True:
        limpiar_consola()
        print_brand_sistema()
        separador_en_consola()
        
        print("[--Login--]")
        print("\n[1] Administrador")
        print("[2] Bibliotecario")
        print("[3] Lector")
        print("[0] Salir")
        role = input("\n\n> Elige una opción => ")

        if role == "0":
            print("\n> Saliendo del sistema.")
            pausar_sistema()
            return False

        if role not in ["1", "2", "3"]:
            print("\n> Opción invalida. Por favor intentalo de nuevo.")
            pausar_sistema()
            continue

        if validar_contraseña(role):
            print("\n> Contraseña correcta. Acceso concedido.")
        else:
            input("\n> Contraseña incorrecta. Acceso denegado.")
            continue

        limpiar_consola()
        if role == "1":
            AdminMenu(container).show()
        elif role == "2":
            LibrarianMenu(container).show()
        elif role == "3":
            ReaderMenu(container).show()
        else:
            print("\n> Opción invalida. Por favor intentalo de nuevo.")

if __name__ == "__main__":
    main()