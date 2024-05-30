from utils.helpers import SistemaBiblioteca as sb
from managers.libro_manager import LibroManager
from managers.articulo_cientifico_manager import ArticuloCientificoManager
from managers.tesis_manager import TesisManager
from managers.autor_manager import AutorManager
from managers.lector_manager import LectorManager

from datetime import date

def main():
    biblioteca = sb()
    libro_manager = LibroManager()
    articulo_manager = ArticuloCientificoManager()
    autor_manager = AutorManager()
    tesis_manager = TesisManager()
    lector_manager = LectorManager()
    
    sb.limpiar_consola(biblioteca)
    sb.print_brand_sistema(biblioteca)

    roles_validos = ["lector", "bibliotecario", "administrador"]
    rol = None
    
    while rol not in roles_validos:
        rol = input("¿Es usted un lector, bibliotecario o administrador? ").lower()

        if rol not in roles_validos:
            print("Rol no reconocido. Intente de nuevo.")
            
    sb.verificar_acceso_administrador(biblioteca, rol)
    
    biblioteca.rol_actual = rol  # Asignar el rol actual
    
    while True:
        if rol == "lector":
            sb.mostrar_menu_lector(biblioteca)
            return False
        
        elif rol == "bibliotecario":
            sb.mostrar_menu_bibliotecario(biblioteca,libro_manager, autor_manager , articulo_manager, tesis_manager, lector_manager)
            return False
        
        elif rol == "administrador":
            sb.mostrar_menu_administrador(biblioteca, libro_manager, autor_manager, libro_manager, articulo_manager, tesis_manager, lector_manager)
            return False

if __name__ == "__main__":
    main()