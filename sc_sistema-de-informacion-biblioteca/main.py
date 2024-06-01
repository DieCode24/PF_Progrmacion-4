from utils.helpers import SistemaBiblioteca as sb
from clases.base import Base
from datetime import date

def main():
    base = Base()
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
            sb.mostrar_menu_bibliotecario(biblioteca, base)
            return False
        
        elif rol == "administrador":
            sb.mostrar_menu_administrador(biblioteca, base)
            return False

if __name__ == "__main__":
    main()