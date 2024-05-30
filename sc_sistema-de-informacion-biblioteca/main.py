from utils.helpers import SistemaBiblioteca as sb
from managers.libro_manager import LibroManager
from managers.articulo_cientifico_manager import ArticuloCientificoManager
from managers.tesis_manager import TesisManager
from managers.autor_manager import AutorManager

def main():
    biblioteca = sb()
    libro_manager = LibroManager()
    articulo_manager = ArticuloCientificoManager()
    autor_manager = AutorManager()
    Tesis = TesisManager()
    sb.limpiar_consola(biblioteca)

    roles_validos = ["lector", "bibliotecario", "administrador"]
    rol = None

    while rol not in roles_validos:
        rol = input("¿Es usted un lector, bibliotecario o administrador? ").lower()
        if rol not in roles_validos:
            print("Rol no reconocido. Intente de nuevo.")

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
            sb.mostrar_menu_bibliotecario(biblioteca, autor_manager, libro_manager, articulo_manager, Tesis)
        elif rol == "administrador":
            sb.mostrar_menu_administrador(biblioteca, autor_manager, libro_manager, articulo_manager, Tesis)


if __name__ == "__main__":
    main()