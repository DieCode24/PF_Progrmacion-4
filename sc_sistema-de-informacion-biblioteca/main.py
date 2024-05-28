from utils.helpers import SistemaBiblioteca as sb
from managers.libro_manager import LibroManager
def main():
    biblioteca = sb()
    libroManager = LibroManager()
    
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
            sb.mostrar_menu_bibliotecario(biblioteca, libroManager)
        elif rol == "administrador":
            sb.mostrar_menu_administrador(biblioteca)
        else:
            print("Rol no reconocido. Intente de nuevo.")
            break

if __name__ == "__main__":
    main()