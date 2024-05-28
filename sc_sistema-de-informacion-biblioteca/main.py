# Importamos la clase SistemaBiblioteca del módulo helpers en el paquete utils, y lo asocio a la palabra reservada propia sb.
from utils.helpers import SistemaBiblioteca as sb

def main():
    """
    Función principal que ejecuta el menú principal en un bucle continuo hasta que el usuario decida salir.
    """
    # Se insantica la bibliote a utilizar.
    biblioteca = sb()
    
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
            sb.mostrar_menu_bibliotecario(biblioteca)
        elif rol == "administrador":
            sb.mostrar_menu_administrador(biblioteca)
        else:
            print("Rol no reconocido. Intente de nuevo.")
            break

if __name__ == "__main__":
    main()