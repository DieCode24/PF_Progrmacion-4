from utils.helpers import SistemaBiblioteca as sb
from managers.libro_manager import LibroManager
from managers.articulo_cientifico_manager import ArticuloCientificoManager
from managers.autor_manager import AutorManager

def main():
    biblioteca = sb()
    libro_manager = LibroManager()
    articulo_manager = ArticuloCientificoManager()
    Autor  = AutorManager()

    
    
    sb.limpiar_consola(biblioteca)
    
    rol = input("¿Es usted un lector, bibliotecario o administrador? ").lower()
        
    if rol == "administrador":
        clave = input("Ingrese la clave de administrador: ")
        if clave != "clave_admin":
            print("Clave incorrecta. Acceso denegado.")
            return
        
    while True:
        sb.limpiar_consola(biblioteca)
        
        if rol == "lector":
            sb.mostrar_menu_lector(biblioteca)
        elif rol == "bibliotecario":
            sb.mostrar_menu_bibliotecario(biblioteca, libro_manager, articulo_manager)
        elif rol == "administrador":
            sb.mostrar_menu_administrador(biblioteca, Autor, libro_manager, articulo_manager)
        else:
            print("Rol no reconocido. Intente de nuevo.")
            break

if __name__ == "__main__":
    main()