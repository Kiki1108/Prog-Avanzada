from proteina import Proteina

class ProteinaEnzimatica(Proteina):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
        self.__subtrato = None

    def set_subtrato(self, subtrato):
        if isinstance(subtrato, str):
            self.__subtrato = subtrato.capitalize()
        else:
            print("Proteina no válida")

    def get_subtrato(self):
        return self.__subtrato()

    def imprimir(self):
        print("#" * 50)
        print(f"\nNombre: {self.get_nombre()}")
        print(f"Descripción: \n{self.get_descripcion()}\n")
        print(f"Secuencia: \n{self.get_secuencia()}\n")
        print(f"subtrato: {self.__subtrato}\n")

    def mostrar_subtrato(self):
        print(f"Nombre: {self.get_nombre()}\nSubtrato: {self.__subtrato}")

