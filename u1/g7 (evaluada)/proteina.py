from aminoacidos import dic

class Proteina():
    def __init__(self, nombre) -> None:
        self.__nombre = nombre
        self.__descripcion = None
        self.__secuencia = None

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre
    
    def set_descripcion(self, descripcion):
        if isinstance(descripcion, str):
            self.__descripcion = descripcion

    def get_descripcion(self):
        return self.__descripcion
    
    def set_secuencia(self, secuencia):
        for i in secuencia:
            if i not in dic.keys():
                print("Secuencia no válida")
                break
        self.__secuencia = secuencia

    def get_secuencia(self):
        return self.__secuencia
    
    def imprimir(self):
        print("#" * 50)
        print(f"\nNombre: {self.__nombre}")
        print(f"Descripción: \n{self.__descripcion}\n")
        print(f"Secuencia: \n{self.__secuencia}\n")

    def mostrar_secuencia(self):
        print(f"Secuencia:\n{self.__secuencia}\n")