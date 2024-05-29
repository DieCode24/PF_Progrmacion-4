from clases.tesis import Tesis
from clases.estado import Estado
from utils.validators import validar_input
from clases.autor import Autor

class TesisManager:
    def __init__(self):
        self.tesis = [ 
            Tesis(["juan", "pedro"], "utp", "2020-01-04", "2024-01-01", "Ciencia", Estado.DISPONIBLE, 100),
                      ]
    
    def agregar_tesis(self):
        autores = validar_input("Ingrese los autores de la tesis (separados por coma): ", list, separator=",")
        institucion = validar_input("Ingrese la institucion de la tesis: ", str)
        f_investigacion = validar_input("Ingrese la fecha de investigacion de la tesis (YYYY-MM-DD): ", str)
        f_presentacion = validar_input("Ingrese la fecha de presentacion de la tesis (YYYY-MM-DD): ", str)
        campo_estudio = validar_input("Ingrese el campo de estudio de la tesis: ", str)
        estado = Estado.DISPONIBLE
        paginas = validar_input("Ingrese el numero de paginas de la tesis: ", int)
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
        print("1. Por autor")
        print("2. Por campo de estudio")
        
        op = input("Ingrese la opcion: ")
        
        if op == '1':
            self.buscar_por_autor()
            
        elif op == '2':
            self.buscar_por_campo()
        
    def buscar_por_autor(self):
        autor = validar_input("Ingrese el autor: ", str).lower()
        for tesis in self.tesis:
            if autor in tesis.get_Autores():
                print(" Campo: ", tesis.get_CampoEstudio(), "\n" + 
                      "   Autores: ", tesis.get_Autores(),"\n" + 
                      "   Páginas: ", tesis.get_Paginas(),"\n" + 
                      "   Fecha publicacion: ", tesis.get_Fpresentacion(),"\n\n")

                    
    def buscar_por_campo(self):
        campo = validar_input("Ingrese el campo de estudio: ", str).lower()
        for tesis in self.tesis:
            if campo in tesis.get_CampoEstudio().lower():
                print(" Campo: ", tesis.get_CampoEstudio(), "\n" + 
                      "   Autores: ", tesis.get_Autores(),"\n" + 
                      "   Páginas: ", tesis.get_Paginas(),"\n" + 
                      "   Fecha publicacion: ", tesis.get_Fpresentacion(),"\n\n")
                
                
    def eliminar_tesis(self):
        self.listar_tesis()
        if not self.tesis:
            print("No hay tesis registradas")
            return
        
        num_tesis = len(self.tesis)
        opcion = validar_input(f"Ingrese el número de la tesis que desea eliminar (1-{num_tesis}): ", int)
    
        if opcion < 1 or opcion > num_tesis:
            print("Número de tesis no válido.")
            return

        tesis_a_eliminar = self.tesis[opcion - 1]

        confirmacion = input(f"¿Está seguro que desea eliminar la siguiente tesis?\n{tesis_a_eliminar}\n(s/n): ")
        if confirmacion.lower() == "s":
            del self.tesis[opcion - 1]
            print("Tesis eliminada correctamente.")
        else:
            print("Operación de eliminación cancelada.")
        
    

    