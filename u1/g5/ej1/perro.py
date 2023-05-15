from animal import Animal

class Perro(Animal):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
    
    def ladrar(self):
        print(f"El perro {self.get_nombre()} ladró")