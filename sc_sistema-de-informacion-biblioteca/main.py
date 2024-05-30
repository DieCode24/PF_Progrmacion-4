from utils.helpers import SistemaBiblioteca as sb
from managers.libro_manager import LibroManager
from managers.articulo_cientifico_manager import ArticuloCientificoManager
from managers.tesis_manager import TesisManager
from managers.autor_manager import AutorManager
from managers.lector_manager import LectorManager

from datetime import date

def main():
    libro_manager = LibroManager()
    articulo_manager = ArticuloCientificoManager()
    Autor = AutorManager()
    Tesis = TesisManager()
    lector_manager = LectorManager()
    biblioteca = sb()

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
            sb.mostrar_menu_bibliotecario(biblioteca, Autor, libro_manager, articulo_manager, Tesis, lector_manager)
            return False
        
        elif rol == "administrador":
            sb.mostrar_menu_administrador(biblioteca, Autor, libro_manager, articulo_manager, Tesis, lector_manager)
            return False


if __name__ == "__main__":
    main()