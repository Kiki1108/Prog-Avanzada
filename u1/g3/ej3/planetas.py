class Planeta():
    def __init__(self) -> None:
        self.__nombre = None
        self.__masa = None
        self.__densidad = None
        self.__diametro = None
        self.__orbita_media = None
        self.__id = None

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre
    
    def set_masa(self, masa):
        try:
            self.__masa = float(masa)
        except:
            print("Masa no válida")
    
    def get_masa(self):
        return self.__masa
    
    def set_densidad(self, densidad):
        try:
            self.__densidad = float(densidad)
        except:
            print("Densidad no válida")

    def get_densidad(self):
        return self.__densidad
    
    def set_diametro(self, diametro):
        try:
            self.__diametro = float(diametro)
        except:
            print("Diámetro no válido")

    def get_diametro(self):
        return self.__diametro
    
    def set_orbita_media(self, orbita):
        try:
            self.__orbita_media = float(orbita)
        except:
            print("orbita no válida")
    
    def get_orbita_medio(self):
        return self.__orbita_media
    
    def set_id(self, id):
        self.__id = id
            
    def get_id(self):
        return self.__id
        
    def imprimir_planeta(self):
        print(f"        Planeta: {self.get_nombre()}")
        print(f"            Id:{self.get_id()}")
        print(f"            Masa: {self.get_masa()} Masas Terrestres")
        print(f"            Densidad:{self.get_densidad()} g/cm3")
        print(f"            Diametro:{self.get_diametro()} km")
        print(f"            Orbita media:{self.get_orbita_medio()} UA")

