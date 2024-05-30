from clases.tesis import Tesis
from clases.estado import Estado
from utils.validators import validar_input
from managers.autor_manager import AutorManager

class TesisManager:
    def __init__(self):
        self.tesis = [ 
            Tesis(["juan", "pedro"], "utp", "2020-01-04", "2024-01-01", "Ciencia", Estado.DISPONIBLE, 100),
            Tesis(["maria", "luis"], "utp", "2020-01-04", "2024-01-01", "Matematicas", Estado.DISPONIBLE, 200),
            Tesis(["juan", "mateo"], "utp", "2020-01-04", "2024-01-01", "Ciencia", Estado.DISPONIBLE, 100),
            ]
        autor = AutorManager()
    
    def agregar_tesis(self):
        institucion = validar_input("Ingrese la institución de la tesis: ", str).capitalize()
        f_investigacion = validar_input("Ingrese la fecha de investigación de la tesis (YYYY-MM-DD): ", str)
        f_presentacion = validar_input("Ingrese la fecha de presentación de la tesis (YYYY-MM-DD): ", str)
        campo_estudio = validar_input("Ingrese el campo de estudio de la tesis: ", str)
        estado = Estado.DISPONIBLE
        paginas = validar_input("Ingrese el número de páginas de la tesis: ", int)
        
        
        autores = validar_input("Ingrese los autores de la tesis (separados por coma): ", list, separator=",")

        tesis = Tesis(autores, institucion, f_investigacion, f_presentacion, campo_estudio, estado, paginas)
        self.tesis.append(tesis)
        
        
        
    def listar_tesis(self):
        print("LISTA DE TESIS\n")
        counter = 1;
        for tesis in self.tesis:
            print(counter, " Campo: ", tesis.get_CampoEstudio(), "\n" + 
                "   Autores: ", tesis.get_Autores(),"\n" + 
                "   Páginas: ", tesis.get_Paginas(),"\n" + 
                "   Fecha publicacion: ", tesis.get_Fpresentacion(),"\n\n")
            counter += 1
            
    def buscar_tesis(self): 
        print("Como desea buscar la tesis?")
        print("1. Autor")
        print("2. Campo de estudio")
        
        op = validar_input("\n> Ingrese una opción => ", int)
        
        if op == '1':
            self.buscar_por_autor()
            
        elif op == '2':
            self.buscar_por_campo()
        
    def buscar_por_autor(self):
        autor = validar_input("Ingrese el autor: ", str).capitalize()
        for tesis in self.tesis:
            if autor in tesis.get_Autores().capitalize():
                print(" Campo: ", tesis.get_CampoEstudio(), "\n" + 
                    "   Autores: ", tesis.get_Autores(),"\n" + 
                    "   Páginas: ", tesis.get_Paginas(),"\n" + 
                    "   Fecha publicación: ", tesis.get_Fpresentacion(),"\n\n")

                    
    def buscar_por_campo(self):
        campo = validar_input("Ingrese el campo de estudio: ", str).capitalize()
        for tesis in self.tesis:
            if campo in tesis.get_CampoEstudio().capitalize():
                print(" Campo: ", tesis.get_CampoEstudio(), "\n" + 
                    "   Autores: ", tesis.get_Autores(),"\n" + 
                    "   Páginas: ", tesis.get_Paginas(),"\n" + 
                    "   Fecha publicación: ", tesis.get_Fpresentacion(),"\n\n")
                
                
    def eliminar_tesis(self):
        self.listar_tesis()
        if not self.tesis:
            print("No hay tesis registradas")
            return
        
        opcion = validar_input(f"Ingrese el número de la tesis que desea eliminar: ", int)

        tesis_a_eliminar = self.tesis[opcion - 1]
        self.tesis.remove(tesis_a_eliminar) 
        print("Tesis eliminada correctamente.")
            
        
    def modificar_tesis(self):
        self.listar_tesis()
        if not self.tesis:
            print("No hay tesis registradas")
            return
        
        opcion = validar_input(f"Ingrese el número de la tesis que desea modificar: ", int)
    

        T_modificar = self.tesis[opcion - 1]
        
        print("Datos actuales de la tesis\n")
        print(" Campo: ", T_modificar.get_CampoEstudio(), "\n" + 
                "   Autores: ", T_modificar.get_Autores(),"\n" + 
                "   Páginas: ", T_modificar.get_Paginas(),"\n" + 
                "   Fecha investigacion: ", T_modificar.get_Finvestigacion(),"\n" +
                "   Fecha publicacion: ", T_modificar.get_Fpresentacion(),"\n" +
                "   Institucion: ", T_modificar.get_Institucion(),"\n\n")
        
        print("Datos nuevos de la tesis\n")

        autores = validar_input("Ingrese los autores de la tesis (separados por coma): ", list, separator=",")
        institucion = validar_input("Ingrese la institución de la tesis: ", str).capitalize()
        f_investigacion = validar_input("Ingrese la fecha de investigación de la tesis (YYYY-MM-DD): ", str)
        f_presentacion = validar_input("Ingrese la fecha de presentación de la tesis (YYYY-MM-DD): ", str)
        campo_estudio = validar_input("Ingrese el campo de estudio de la tesis: ", str)
        estado = Estado.DISPONIBLE
        paginas = validar_input("Ingrese el número de páginas de la tesis: ", int)
        
        T_modificar.set_Autores(autores)
        T_modificar.set_Institucion(institucion)
        T_modificar.set_Finvestigacion(f_investigacion)
        T_modificar.set_Fpresentacion(f_presentacion)
        T_modificar.set_CampoEstudio(campo_estudio)
        T_modificar.set_Estado(estado)
        T_modificar.set_Paginas(paginas)
        
        print("Tesis modificada correctamente.")
        
    

    