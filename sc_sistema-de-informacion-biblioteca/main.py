import os
from dotenv import load_dotenv
from managers.libro_manager import LibroManager
from managers.articulo_cientifico_manager import ArticuloCientificoManager
from managers.tesis_manager import TesisManager
from managers.autor_manager import AutorManager
from managers.copia_manager import CopiaManager
from managers.lector_manager import LectorManager
from managers.data_manager import DataManager
from menu import AdminMenu, LibrarianMenu
from datetime import date
from utils.helpers import pausar_sistema, limpiar_consola, print_brand_sistema

load_dotenv()
class DependencyContainer:
    def __init__(self, data_manager):
        self.data_manager = data_manager
        self.libro_manager = LibroManager(data_manager)
        self.articulo_manager = ArticuloCientificoManager(data_manager)
        self.autor_manager = AutorManager(data_manager)
        self.tesis_manager = TesisManager(data_manager)
        self.lector_manager = LectorManager(data_manager)
        self.copy_manager = CopiaManager(data_manager)

def validar_contraseña(rol):
    if rol == "1":
        contraseña_correcta = os.getenv("ADMIN_PASSWORD")
    elif rol == "2":
        contraseña_correcta = os.getenv("LIBRARIAN_PASSWORD")
    elif rol == "3":
        contraseña_correcta = os.getenv("READER_PASSWORD")
    else:
        return False

    contraseña = input("Ingrese la contraseña: ")
    return contraseña == contraseña_correcta

def main():
    data_manager = DataManager()
    container = DependencyContainer(data_manager)
    
    limpiar_consola()
    while True:
        limpiar_consola()
        print_brand_sistema()
        print("\nLogin")
        print("1. Admin")
        print("2. Librarian")
        print("3. Reader")
        print("0. Exit")
        role = input("Choose your role: ")

        if role == "0":
            break

        if role not in ["1", "2", "3"]:
            print("Invalid choice. Please try again.")
            continue

        if not validar_contraseña(role):
            print("Contraseña incorrecta. Intente de nuevo.")
            pausar_sistema()
            continue

        limpiar_consola()
        if role == "1":
            AdminMenu(container).show()
        elif role == "2":
            LibrarianMenu(container).show()
        elif role == "3":
            pass
            # ReaderMenu(container).show()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()