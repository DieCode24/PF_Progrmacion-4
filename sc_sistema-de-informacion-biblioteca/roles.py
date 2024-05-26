class Biblioteca:
    def __init__(self):
        pass
    
    def mostrar_menu_lector(self):
        print("\nMenú de Lector:")
        print("1. Buscar libros")
        print("2. Realizar préstamo de libro")
        print("3. Devolver libro")
        print("4. Consultar préstamos")
        print("5. Salir")

    def mostrar_menu_bibliotecario(self):
        print("\nMenú de Bibliotecario:")
        print("1. Registrar nuevo libro")
        print("2. Buscar libros")
        print("3. Modificar libro")
        print("4. Inhabilitar libro")
        print("5. Registrar nuevo lector")
        print("6. Modificar lector")
        print("7. Buscar lectores")
        print("8. Salir")

    def mostrar_menu_administrador(self):
        print("\nMenú de Administrador:")
        print("1. Gestionar categorías")
        print("2. Gestionar copias de libros")
        print("3. Gestionar autores")
        print("4. Gestionar multas")
        print("5. Salir")
    
    def ejecutar(self):
        rol = input("¿Es usted un lector, bibliotecario o administrador? ").lower()
        
        if rol == "administrador":
            clave = input("Ingrese la clave de administrador: ")
            if clave != "clave_admin":
                print("Clave incorrecta. Acceso denegado.")
                return
        
        while True:
            if rol == "lector":
                self.mostrar_menu_lector()
            elif rol == "bibliotecario":
                self.mostrar_menu_bibliotecario()
            elif rol == "administrador":
                self.mostrar_menu_administrador()
            else:
                print("Rol no reconocido. Intente de nuevo.")
                break
            
            opcion = input("Seleccione una opción: ")
            if opcion == "5" and rol in ["lector", "administrador"]:
                break
            elif opcion == "8" and rol == "bibliotecario":
                break
            else:
                print(f"Opción {opcion} seleccionada. (Funcionalidad no implementada en este ejemplo)")
    
if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.ejecutar()
