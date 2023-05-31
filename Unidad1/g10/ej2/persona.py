from abc import abstractclassmethod
from abc import ABCMeta

class Persona(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @abstractclassmethod
    def mostrar_informacion():
        pass