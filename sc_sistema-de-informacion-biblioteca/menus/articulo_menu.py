from utils.helpers import pausar_sistema, limpiar_consola, print_brand_sistema, separador_en_consola

def show_articulo_menu(self):
    articulo_manager = self.container.articulo_manager
    while True:
        limpiar_consola()
        print_brand_sistema()
        separador_en_consola()

        print("[-- Menu | Gestión de Artículos Científicos --]")

        print("\n[1] Registrar Artículo")
        print("[2] Buscar Artículo")
        print("[3] Modificar Artículo")
        print("[4] Eliminar Artículo")
        print("[5] Listar Artículos")
        print("[0] Volver al menú principal")

        opcion = input("\n\n> Ingrese una opción => ")
        
        if opcion == '1':
            limpiar_consola()
            articulo_manager.registrar_articulo_desde_consola()
            pausar_sistema()

        elif opcion == '2':
            limpiar_consola()
            articulo_manager.buscar_articulo_desde_consola()
            pausar_sistema()

        elif opcion == '3':
            limpiar_consola()
            articulo_manager.modificar_articulo_desde_consola()
            pausar_sistema()

        elif opcion == '4':
            limpiar_consola()
            doi = input("Ingrese el DOI del artículo a eliminar: ")
            try:
                articulo_manager.eliminar_articulo(doi)
                print("Artículo eliminado exitosamente.")
            except ValueError as e:
                print(e)
            pausar_sistema()
         
        elif opcion == '5':
            limpiar_consola()
            articulo_manager.listar_articulos()
            pausar_sistema()
            limpiar_consola()

        elif opcion == '0':
            input("\n\n> Volviendo al menú principal...")
            
            return False  # Salir del bucle while y regresar al menú anterior

        else:
            print("\n> Opción no válida, intente de nuevo.")
            pausar_sistema()