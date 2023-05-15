from abc import abstractclassmethod
from abc import ABCMeta

class Figura(metaclass=ABCMeta):

    @abstractclassmethod
    def calcular_area():
        pass

    @abstractclassmethod
    def calcular_perimetro():
        pass