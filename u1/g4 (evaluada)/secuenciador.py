import random
from secuenciaADN import SecuenciaADN as Adn

class Secuanciador():
    def __init__(self) -> None:
        self.__long = None
        self.__cadena = []


    def set_longitud(self, long):
        try:
            self.__long = int(long)
        except:
            print("longitud no válida")


    def get_longitud(self):
        return self.__long


    def generar_cadena(self):
        long = random.randint(int(self.__long - self.__long/10), int(self.__long + self.__long/10))
        cadena = ""
        for _i in range(long):
            nucleotido = random.randint(0, 3)
            match nucleotido:
                case 0: cadena = cadena + "A"
                case 1: cadena = cadena + "T"
                case 2: cadena = cadena + "C"
                case 3: cadena = cadena + "G"
        secuencia = Adn()
        secuencia.set_secuencia(cadena)
        self.__cadena.append(secuencia)

        inversa = Adn()
        inversa.set_secuencia(secuencia.get_inverso())
        self.__cadena.append(inversa)


    def get_cadenas(self):
        return self.__cadena
