from utils.helpers import pausar_sistema, limpiar_consola

def show_prestamo_menu(self):
    limpiar_consola()
    prestamo_manager = self.container.prestamo_manager
    libro_manager = self.container.libro_manager
    lector_manager = self.container.lector_manager
    tesis_manager = self.container.tesis_manager
    articulo_manager = self.container.articulo_manager
    copia_manager = self.container.copy_manager
    
    while True:
        print("# Gestión de Préstamos")
        print("---------------------------------------------------")
        print("Seleccione una opción:\n")
        print("> [1] Realizar Préstamo")
        print("> [2] Devolver Libro")
        print("> [3] Listar Préstamos")
        print("> [4] Buscar Préstamo")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            
            lector = lector_manager() 
            libro = libro_manager()
            prestamo_manager.realizar_prestamo(lector, libro)
        elif opcion == "2":
            prestamo_manager.devolver_libro()
        elif opcion == "3":
            prestamo_manager.listar_prestamos()
        elif opcion == "4":
            prestamo_manager.buscar_prestamo()
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
            
            
            
        