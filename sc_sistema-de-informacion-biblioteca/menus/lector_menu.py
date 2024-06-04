from utils.helpers import limpiar_consola, pausar_sistema, print_brand_sistema, separador_en_consola

def show_lector_menu(self):
    lector_manager = self.container.lector_manager

    while True:
        limpiar_consola()
        print_brand_sistema()
        separador_en_consola()

        print("[-- Menu | Gestión de Lectores --]")

        print("\n[1] Registrar Lector")
        print("[2] Buscar Lector")
        print("[3] Modificar Lector")
        print("[4] Habilitar Lector")
        print("[5] Inhabilitar Lector")
        print("[6] Listar Lectores")
        print("[0] Volver al menú principal")
        opcion = input("\n\n> Ingrese una opción => ")

        if opcion == "1":
            limpiar_consola()
            lector_manager.registrar_lector()
            pausar_sistema()

        elif opcion == "2":
            limpiar_consola()
            lector_manager.listar_lectores()
            id_lector = int(input("Ingrese el ID del lector a buscar: "))
            lector_manager.buscar_lector(id_lector)
            pausar_sistema()

        elif opcion == "3":
            limpiar_consola()
            lector_manager.modificar_lector()
            pausar_sistema()

        elif opcion == "4":
            limpiar_consola()
            id_lector = int(input("Ingrese el ID del lector a habilitar: "))
            try:
                lector_manager.habilitar_lector(id_lector)
                print("Lector habilitado exitosamente.")
            except ValueError as e:
                print(e)
            pausar_sistema()

        elif opcion == "5":
            limpiar_consola()
            id_lector = int(input("Ingrese el ID del lector a inhabilitar: "))
            try:
                lector_manager.inhabilitar_lector(id_lector)
            except ValueError as e:
                print(e)
            pausar_sistema()

        elif opcion == "6":
            limpiar_consola()
            lectores = lector_manager.listar_lectores()

        elif opcion == "0":
            return False

        else:
            print("\n> Opción no válida, intente de nuevo.")
            pausar_sistema()