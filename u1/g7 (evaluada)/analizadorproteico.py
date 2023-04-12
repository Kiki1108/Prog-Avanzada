from proteina import Proteina

class AnalizadorProteico():
    def __init__(self) -> None:
        self.__proteinas = []

    def add_proteina(self, proteina):
        if isinstance(proteina, Proteina):
            self.__proteinas.append(proteina)

    def mostrar_porcentaje_hidrofobos(self):
        for i in self.__proteinas:
            tamano = len(i.get_secuencia())
            contador = 0
            for j in i.get_secuencia():
                if j in ["A", "V", "I", "L", "F", "M"]:
                    contador += 1
            
            print(i.get_nombre())
            print(f"% de aminoácidos hidrofobico: {int((contador/tamano)*100)}%")

    def mostrar_peso_molecular(self):
        pass



