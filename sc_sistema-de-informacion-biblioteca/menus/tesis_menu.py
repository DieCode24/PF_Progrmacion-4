from utils.helpers import pausar_sistema, limpiar_consola, print_brand_sistema, separador_en_consola

def show_tesis_menu(self):
    limpiar_consola()
    autor_manager = self.container.autor_manager
    tesis_manager = self.container.tesis_manager
    
    while True:
        limpiar_consola()
        print_brand_sistema()
        separador_en_consola()
        
        print("[-- Menu | Gestión de Tesis --]")
        
        print("\n[1] Registrar Tesis")
        print("[2] Listar Tesis")
        print("[3] Buscar Tesis")
        print("[4] Modificar Tesis")
        print("[5] Eliminar Tesis")
        print("[6] Datos de prueba (Mock data)")
        print("[0] Voler al menú principal")
        opcion = input("\n\n> Seleccione una opción => ")
        if opcion == "1":
            limpiar_consola()
            autores = autor_manager.seleccionar_autores()
            tesis_manager.agregar_tesis(autores)
            pausar_sistema()
            limpiar_consola()
            
        elif opcion == "2":
            limpiar_consola()
            tesis_manager.listado_tesis()
            pausar_sistema()
            limpiar_consola()
            
        elif opcion == "3":
            limpiar_consola()
            tesis_manager.buscar_tesis()
            pausar_sistema()
            limpiar_consola()
            
        elif opcion == "4":
            limpiar_consola()
            autores = autor_manager
            tesis_manager.modificar_tesis(autores)
            pausar_sistema()
            limpiar_consola()
            
        elif opcion == "5":
            limpiar_consola()
            tesis_manager.eliminar_tesis()
            pausar_sistema()
            limpiar_consola()
        elif opcion == '6':
            tesis_manager.mock()
            pausar_sistema()
            limpiar_consola()
            
        elif opcion == "0":
            return False
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
