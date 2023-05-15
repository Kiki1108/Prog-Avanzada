class Animal():
    def __init__(self, nombre) -> None:
        self.__nombre = nombre
        self.__edad = None
        self.__genero = None

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            print("nombre no válido")

    def get_nombre(self):
        return self.__nombre
    
    def set_edad(self, edad):
        if isinstance(edad, int):
            self.__edad = edad
        else:
            print("edad no válida")
    
    def get_edad(self):
        return self.__edad
    
    def set_genero(self, genero):
        if genero == "M" or genero == "H":
            self.__genero = genero
        else:
            print("genero no valido")

    def get_genero(self):
        return self.__genero
