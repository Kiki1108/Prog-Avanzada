import random
from secuenciaADN import SecuanciaADN as Adn

class Secuanciador():
    def __init__(self) -> None:
        self.__longitud = None
        self.__cadena = []


    def set_longitud(self, longitud):
        try:
            self.__longitud = int(longitud)
        except:
            print("longitud no válida")
    

    def get_longitud(self):
        return self.__longitud
    
    
    def generar_cadena(self): 
        longitud = random.randint(int(self.__longitud - self.__longitud/10), int(self.__longitud + self.__longitud/10))
        cadena = ""
        for b in range(longitud):
            nucleotido = random.randint(0, 3)
            match nucleotido:
                case 0: n = "A"
                case 1: n = "T"
                case 2: n = "G"
                case 3: n = "C"
            cadena = cadena + n
        secuencia = Adn()
        secuencia.set_secuencia(cadena)
        self.__cadena.append(secuencia)

        inversa = Adn()
        inversa.set_secuencia(secuencia.get_inverso())
        self.__cadena.append(inversa)
        
    
    def get_cadenas(self):
        return self.__cadena


