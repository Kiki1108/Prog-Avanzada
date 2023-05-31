from proteina import Proteina

class SecuenciaProteina():
    def __init__(self) -> None:
        self.__proteinas = []

    def add_proteina(self, proteina):
        if isinstance(proteina, Proteina):
            self.__proteinas.append(proteina)

    def mostrar_secuencias(self):
        for i in self.__proteinas:
            print(f"Nombre: {i.get_nombre()}")
            i.mostrar_secuencia()
