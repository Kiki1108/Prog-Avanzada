from animal import Animal

class Gato(Animal):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)

    def maullar(self):
        print(f"El gato {self.get_nombre()} maulló")