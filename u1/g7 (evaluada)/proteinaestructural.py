from proteina import Proteina

class ProteinaEstructural(Proteina):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
        self.__tipo = None

    def set_tipo(self, tipo):
        if tipo.lower() == "fibrosa":
            self.__tipo = "Fibrosa"
        elif tipo.lower() == "globular":
            self.__tipo = "Globular"
        else:
            print("Proteina no válida")

    def get_tipo(self):
        return self.__tipo()
    
    def imprimir(self):
        print("#" * 50)
        print(f"\nNombre: {self.get_nombre()}")
        print(f"Descripción: \n{self.get_descripcion()}\n")
        print(f"Secuencia: \n{self.get_secuencia()}\n")
        print(f"Tipo: {self.__tipo}\n")
    
    def mostrar_tipo(self):
        print(f"Nombre: {self.get_nombre()}\nTipo: {self.__tipo}")