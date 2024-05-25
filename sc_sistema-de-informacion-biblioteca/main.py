# Importamos la clase SistemaBiblioteca del módulo helpers en el paquete utils, y lo asocio a la palabra reservada propia sb.
from utils.helpers import SistemaBiblioteca as sb

def main():
    """
    Función principal que ejecuta el menú principal en un bucle continuo hasta que el usuario decida salir.
    """    
    while True:
        # Se insantica la bibliote a utilizar.
        biblioteca = sb()
        
        sb.limpiar_consola(biblioteca)
        sb.mostrar_menu(biblioteca)
        
        opcion = input("\n\n> Ingrese una opción => ")
        
        if opcion == '1':
            sb.gestionar_tesis(biblioteca)
            sb.pausar_sistema(biblioteca)
        elif opcion == '2':
            sb.gestionar_articulos(biblioteca)
            sb.pausar_sistema(biblioteca)
        elif opcion == '3':
            sb.gestionar_libros(biblioteca)
            sb.pausar_sistema(biblioteca)
        elif opcion == '4':
            sb.gestionar_categorias(biblioteca)
            sb.pausar_sistema(biblioteca)
        elif opcion == '5':
            sb.gestionar_autores(biblioteca)
            sb.pausar_sistema(biblioteca)
        elif opcion == '6':
            sb.gestionar_lectores(biblioteca)
            sb.pausar_sistema(biblioteca)
        elif opcion == '7':
            sb.gestionar_prestamos(biblioteca)
            sb.pausar_sistema(biblioteca)
        elif opcion == '8':
            sb.gestionar_multas(biblioteca)
            sb.pausar_sistema(biblioteca)
        elif opcion == '0':
            print("\n\n> Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()