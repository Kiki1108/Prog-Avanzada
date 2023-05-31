class SecuenciaADN():
    def __init__(self) -> None:
        self.__secuencia = None


    def set_secuencia(self, secuencia):
        if isinstance(secuencia, str):
            self.__secuencia = secuencia
            #AAAAAAA
        else:
            print("La secuencia no es válida")


    def get_secuencia(self):
        return self.__secuencia


    def get_longitud(self):
        return len(self.__secuencia)


    def get_inverso(self):
        inverso = ""
        for nucleotido in self.__secuencia:
            match nucleotido:
                case "A": inverso = "T" + inverso
                case "T": inverso = "A" + inverso
                case "C": inverso = "G" + inverso
                case "G": inverso = "C" + inverso
        return inverso


    def contar_nucleotidos(self):
        contador = [0, 0, 0, 0]
        for i in self.__secuencia:
            match i:
                case "A": contador[0] += 1
                case "T": contador[1] += 1
                case "C": contador[2] += 1
                case "G": contador[3] += 1
        dic = {"A": contador[0], "T": contador[1], "C": contador[2], "G": contador[3]}
        return dic


    def encontrar_patron(self, patron):
        cadena = self.__secuencia
        lista = []
        while cadena.find(patron) != -1 :
            lista.append(cadena.find(patron) + 1)
            cadena = cadena.replace(patron, patron.lower(), 1)
        return lista


    def calcular_peso_molecular(self):
        dic = self.contar_nucleotidos()
        peso = dic.get("A") *313.21 +dic.get("T") *304.2 +dic.get("C") *289.18 +dic.get("G") *329.21
        return peso

