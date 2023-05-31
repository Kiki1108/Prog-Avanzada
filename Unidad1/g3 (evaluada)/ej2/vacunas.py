class Vacuna():
    def __init__(self) -> None:
        self.__nombre = None
        self.__lab = None
        self.__efectos_secundarios = []

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            print("Nombre no válido")
    
    def get_nombre(self):
        return self.__nombre
    
    def set_lab(self, lab):
        if isinstance(lab, str):
            self.__lab = lab
        else:
            print("Nombre del laboratorio no válido")
    
    def get_lab(self):
        return self.__lab
    
    def add_efectos_secundarios(self, efecto_secundario):
        if isinstance(efecto_secundario, str):
            self.__efectos_secundarios.append(efecto_secundario)
        else:
            print("Efecto secundario no válido")

    def get_efectos_secundarios(self):
        print("\nEfectos Secunadarios:")
        for a in range(len(self.__efectos_secundarios)):
            print(f"({a+1}) {self.__efectos_secundarios[a]}")
    