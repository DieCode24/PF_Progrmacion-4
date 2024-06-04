from utils.helpers import pausar_sistema, limpiar_consola, print_brand_sistema, separador_en_consola

def show_prestamo_menu(self):
    limpiar_consola()
    prestamo_manager = self.container.prestamo_manager
    libro_manager = self.container.libro_manager
    lector_manager = self.container.lector_manager
    tesis_manager = self.container.tesis_manager
    articulo_manager = self.container.articulo_manager
    copia_manager = self.container.copy_manager

    while True:
        limpiar_consola()
        print_brand_sistema()
        separador_en_consola()

        print("[-- Menu | Gestión de Préstamos --]")

        print("\n[1] Realizar Préstamo")
        print("[2] Devolver Libro")
        print("[3] Listar Préstamos")
        print("[4] Buscar Préstamo")
        print("[0] Volver al menú principal")
        opcion = input("\n\n> Seleccione una opción => ")

        if opcion == "1":
            limpiar_consola()
            lector = lector_manager
            copia = copia_manager
            prestamo_manager.registrar_prestamo(lector, copia)
            pausar_sistema()

        elif opcion == "2":
            limpiar_consola()
            prestamo_manager.devolver_libro()
            pausar_sistema()

        elif opcion == "3":
            limpiar_consola()
            prestamo_manager.listar_prestamos()
            pausar_sistema()

        elif opcion == "4":
            limpiar_consola()
            prestamo_manager.buscar_prestamo()
            pausar_sistema()

        elif opcion == "0":
            return False

        else:
            print("\n> Opción inválida. Por favor, intente de nuevo.")
            pausar_sistema()