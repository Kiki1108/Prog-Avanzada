class SecuanciaADN():
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
        for a in self.__secuencia:
            match a:
                case "A": inverso = "T" + inverso
                case "T": inverso = "A" + inverso
                case "C": inverso = "G" + inverso
                case "G": inverso = "C" + inverso
        return inverso
    

    def contar_nucleotidos(self):
        a = 0
        t = 0
        c = 0
        g = 0
        for i in self.__secuencia:
            match i:
                case "A": a += 1
                case "T": t += 1
                case "C": c += 1
                case "G": g += 1
        dic = {"A": a, "T": t, "C": c, "G": g}
        return dic
    

    def encontrar_patron(self, patron):
        cadena = self.__secuencia
        lista = []
        while cadena.find(patron) != -1 :
            lista.append(cadena.find(patron) + 1)
            cadena = cadena.replace(patron, patron.lower(), 1)
        print(cadena)
        return lista


    def calcular_peso_molecular(self):
        dic = self.contar_nucleotidos()
        a = dic.get("A")
        t = dic.get("T")
        c = dic.get("C")
        g = dic.get("G")
        peso = a * 313.21 + t * 304.2 + c * 289.18 + g * 329.21
        return peso
        

