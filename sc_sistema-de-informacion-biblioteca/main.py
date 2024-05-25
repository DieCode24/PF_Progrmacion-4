# Importamos la clase SistemaBiblioteca del módulo helpers en el paquete utils.
from utils.helpers import SistemaBiblioteca as sb

def main():
    """
    Función principal que ejecuta el menú principal en un bucle continuo hasta que el usuario decida salir.
    """
    while True:
        biblioteca_1 = sb()
        sb.limpiar_consola(biblioteca_1)
        sb.mostrar_menu(biblioteca_1)
        
        opcion = input("\n\n> Ingrese una opción => ")
        
        if opcion == '1':
            sb.gestionar_tesis(biblioteca_1)
            sb.pausar_sistema(biblioteca_1)
        elif opcion == '2':
            sb.gestionar_articulos(biblioteca_1)
            sb.pausar_sistema(biblioteca_1)
        elif opcion == '3':
            sb.gestionar_libros(biblioteca_1)
            sb.pausar_sistema(biblioteca_1)
        elif opcion == '4':
            sb.gestionar_categorias(biblioteca_1)
            sb.pausar_sistema(biblioteca_1)
        elif opcion == '5':
            sb.gestionar_autores(biblioteca_1)
            sb.pausar_sistema(biblioteca_1)
        elif opcion == '6':
            sb.gestionar_lectores(biblioteca_1)
            sb.pausar_sistema(biblioteca_1)
        elif opcion == '7':
            sb.gestionar_prestamos(biblioteca_1)
            sb.pausar_sistema(biblioteca_1)
        elif opcion == '8':
            sb.gestionar_multas(biblioteca_1)
            sb.pausar_sistema(biblioteca_1)
        elif opcion == '0':
            print("\n\n> Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()