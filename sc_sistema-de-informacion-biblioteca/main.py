from utils.helpers import *

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")
        if opcion == '1':
            gestionar_tesis()
            system_pause()
        elif opcion == '2':
            gestionar_articulos()
            system_pause()
        elif opcion == '3':
            gestionar_libros()
            system_pause()
        elif opcion == '4':
            gestionar_categorias()
            system_pause()
        elif opcion == '5':
            gestionar_autores()
            system_pause()
        elif opcion == '6':
            gestionar_lectores()
            system_pause()
        elif opcion == '7':
            gestionar_prestamos()
            system_pause()
        elif opcion == '8':
            gestionar_multas()
            system_pause()
        elif opcion == '0':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()