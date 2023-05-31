from figura import Figura
import math

class Circulo(Figura):
    def __init__(self, radio) -> None:
        self.__radio = radio

    def calcular_area(self):
        area = (self.__radio * math.pi * self.__radio)
        print(f"área = {area} u2")

    def calcular_perimetro(self):
        perimetro = (2 * self.__radio * math.pi)
        print(f"Perímetro = {perimetro} u")