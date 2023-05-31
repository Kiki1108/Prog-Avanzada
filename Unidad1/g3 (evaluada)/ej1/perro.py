class Perro():
    def __init__(self) -> None:
        self.__nombre = None
        self.__horas = None
        self.__paseo = False


    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else: 
            print("Nombre es no válido")
            self.__nombre = None


    def get_nombre(self):
        return self.__nombre
    

    def set_hora_toma_agua(self):
        print("Escriba hace cuanto tomó agua el perro")
        try:
            horas = int(input())
            if not self.__paseo:
                self.__horas = horas
                print(f"Horas establecida en {horas}")
            else:
                print("Está paseando no puede tomar agua")
        except:
            print("Hora no válida, Intentelo denuevo")


    def get_hora_toma_agua(self):
        return self.__horas
    

    def tomar_agua(self):
        if not self.__paseo:
            self.__horas = 0
            print("El perro tomó agua")
        else:
            print("Está paseando no puede tomar agua")


    def pasear(self):
        if self.__horas != None and self.__horas < 4:
            self.__paseo = True
            print("El perro está paseando")
        else:
            print("No puede pasear, se va a deshidratar")
            print(f"Lleva {self.get_hora_toma_agua()} horas sin tomar agua")


    def dejar_pasear(self):
        if self.__paseo == True:
            self.__paseo == False
        else:
            print("no está paseando")


    def ver_paseo(self):
        if self.__paseo:
            print("Está paseando")
        else:
            print("No está paseando")