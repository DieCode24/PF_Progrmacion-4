from utils.helpers import pausar_sistema, limpiar_consola

def show_autor_menu(self):
    limpiar_consola()
    autor_manager = self.container.autor_manager
    tesis_manager = self.container.tesis_manager
    libro_manager = self.container.libro_manager
    articulo_manager = self.container.articulo_manager
    while True:
        print("# Gestión de Autores")
        print("---------------------------------------------------")
        print("Seleccione una opción:\n")
        print("> [1] Registrar Autor")
        print("> [2] Listas de Autores")
        print("> [3] Modificar Autor")
        print("> [4] Inhabiliar Autor")
        print("> [5] Habilitar Autor")
        print("> [6] Datos de prueba (Mock data)")
        print("> [0] Voler al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            limpiar_consola()
            autor_manager.registrar_autor()
            pausar_sistema()
            
        elif opcion == "2":
            limpiar_consola()
            autor_manager.listas_d_autores()
            pausar_sistema()
            limpiar_consola()
            
            
        elif opcion == "3":
            limpiar_consola()
            autor_manager.modificar_autor()
            pausar_sistema()
            limpiar_consola()
            
        elif opcion == "4":
            limpiar_consola()
            autor_manager.inhabilitar_autor()
            pausar_sistema()
            limpiar_consola()
            
        elif opcion == "5":
            limpiar_consola()
            autor_manager.habilitar_autor()
            pausar_sistema()
            limpiar_consola()
            
        elif opcion == '6':
            autor_manager.mock()
            pausar_sistema()
            limpiar_consola()
            
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
