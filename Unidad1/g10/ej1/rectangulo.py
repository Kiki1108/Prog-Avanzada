
from figura import Figura

class Rectangulo(Figura):
    def __init__(self, base, altura) -> None:
        self.__base = base
        self.__altura = altura

    def calcular_area(self):
        area = self.__base * self.__altura
        print(f"Área: {area} u2")

    def calcular_perimetro(self):
        perimetro = 2 * self.__base + 2 * self.__altura
        print(f"Perímetro: {perimetro} u")