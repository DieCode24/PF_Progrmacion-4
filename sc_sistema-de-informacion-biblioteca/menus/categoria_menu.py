from utils.helpers import limpiar_consola, pausar_sistema, print_brand_sistema, separador_en_consola
from managers.data_manager import DataManager

def show_categoria_menu(self):
    categoria_manager = self.container.categoria_manager
    self.data_manager = DataManager

    while True:
        limpiar_consola()
        print_brand_sistema()
        separador_en_consola()

        print("[-- Menu | Gestión de Categorías --]")

        print("\n[1] Crear Categoría")
        print("[2] Buscar Categoría")
        print("[3] Modificar Categoría")
        print("[4] Eliminar Categoría")
        print("[5] Listar Categorías")
        print("[0] Volver al menú principal")
        opcion = input("\n\n> Ingrese una opción => ")

        if opcion == "1":
            limpiar_consola()
            nombre = input("Ingrese el nombre de la categoría: ")
            categoria_id = int(input("Ingrese el ID de la categoría: "))
            descripcion = input("Ingrese la descripción de la categoría: ")
            categoria_manager.crear_categoria(nombre, categoria_id, descripcion)
            print("Categoría creada exitosamente.")
            pausar_sistema()

        elif opcion == "2":
            limpiar_consola()
            categoria_id = int(input("Ingrese el ID de la categoría a buscar: "))
            categoria = categoria_manager.buscar_categoria_por_id(categoria_id)
            if categoria:
                print(categoria)
            else:
                print("Categoría no encontrada.")
            pausar_sistema()

        elif opcion == "3":
            limpiar_consola()
            categoria_id = int(input("Ingrese el ID de la categoría a modificar: "))
            nuevo_nombre = input("Ingrese el nuevo nombre de la categoría (dejar en blanco para no cambiar): ")
            nueva_descripcion = input("Ingrese la nueva descripción de la categoría (dejar en blanco para no cambiar): ")
            try:
                categoria_manager.modificar_categoria(categoria_id, nuevo_nombre, nueva_descripcion)
                print("Categoría modificada exitosamente.")
            except ValueError as e:
                print(e)
            pausar_sistema()

        elif opcion == "4":
            limpiar_consola()
            categoria_id = int(input("Ingrese el ID de la categoría a eliminar: "))
            try:
                categoria_manager.eliminar_categoria(categoria_id)
                print("Categoría eliminada exitosamente.")
            except ValueError as e:
                print(e)
            pausar_sistema()

        elif opcion == "5":
            limpiar_consola()
            categorias = categoria_manager.listar_categorias()
            pausar_sistema()
        
        elif opcion == "0":
            return False

        else:
            print("\n> Opción no válida, intente de nuevo.")
            pausar_sistema()