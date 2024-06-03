from utils.helpers import pausar_sistema, limpiar_consola, print_brand_sistema, separador_en_consola

def show_copy_menu(self):
    libro_manager = self.container.libro_manager
    autor_manager = self.container.autor_manager
    copy_manager = self.container.copy_manager
    while True:
        limpiar_consola()
        print_brand_sistema()
        separador_en_consola()

        print("[-- Menu | Gestión de Copias --]")

        print("\n[1] Listar copias")
        print("[2] Buscar copia")
        print("[3] Habilitar copia")
        print("[4] Inhabilitar copia")
        print("[0] Volver al menú principal")
        choice = input("\n\n> Seleccione una opción => ")
        
        if choice == "1":
            copy_manager.listar_copias()
            pausar_sistema()
            limpiar_consola()
        
        elif choice == "2":
            query = input("Buscar copia por ID: ")
            copy_manager.buscar_copia(query)
            pausar_sistema()
            limpiar_consola()
            
        elif choice == "3":
            id = input("Ingrese el ID de la copia que desea habilitar: ")
            copy_manager.habilitar_copia(id)
            pausar_sistema()
            limpiar_consola()
        
        elif choice == "4":
            id = input("Ingrese el ID de la copia que desea inhabilitar: ")
            copy_manager.inhabilitar_copia(id)
            pausar_sistema()
            limpiar_consola()

        elif choice == "0":
            return False

        else:
            print("\n> Opción inválida. Por favor, intente de nuevo.")
            pausar_sistema()