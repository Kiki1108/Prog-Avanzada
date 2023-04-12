from proteina import Proteina
from aminoacidos import dic

class ProteinaMutante(Proteina):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
        self.__mutacion = None
        self.__rango = []

    def set_mutacion(self, secuencia):
        for i in secuencia:
            if i.upper() not in dic.keys():
                print("Secuencia no válida")
                break
        self.__mutacion = secuencia.upper()

    def get_mutacion(self):
        return self.__mutacion
    
    def mostrar_mutacion(self):
        print(f"Nombre: {self.get_nombre()}")
        print("Mutación:")
        print(self.__rango[0])
        print(self.__mutacion)
        print(self.__rango[1], "\n")

    def set_rango(self, rango1, rango2):
        if isinstance(rango1, int) and isinstance(rango2, int):
            self.__rango.append(rango1)
            self.__rango.append(rango2)
        else:
            print("Rangos no válidos")

    def get_rango(self):
        return self.__rango

    def imprimir(self):
        print("#" * 50)
        print(f"\nNombre: {self.get_nombre()}")
        print(f"Descripción: \n{self.get_descripcion()}\n")
        print(f"Secuencia: \n{self.get_secuencia()}\n")
        print("Mutación:")
        print(self.__rango[0])
        print(self.__mutacion)
        print(self.__rango[1], "\n")

    
