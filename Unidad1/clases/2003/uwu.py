

class Mascota():
    def __init__(self, nombre = None):
        print("Entró al constructor")
        self.nombre = nombre #Constastes
        self.edad = 0 #Variables
        print("Edad 0:", self.edad)
        self.cambia_edad() # se pueden cambiar dentro de la construcción
        print("edad 1:", self.edad)

    def cambia_edad(self): # definimos el cambio para la variable dentro de la clase
        self.edad = self.edad + 1

        # tambien se pueden agregar variables, siendo siempre la primera self
        # def cambia_edad(self, incremento):
        #     self.edad = self.edad + incremento


def main():
    m = Mascota("salchicha") # m = Mascota(nombre = "Salchicha")

    print("tipo:", type(m)) # imprimir el tipo
    print("nombre", m.nombre) # imprimir el nombre

    m.cambia_edad() # ir al método definido en la clase
    print("edad 2:", m.edad) 

    m1 = Mascota("pato") # definir un nuevo objeto
    print("\nnombre:", m1.nombre)

    m2 = m1 # duplicamos??

    print("\nnombre:", m2.nombre) #tienen el mismo nombre

    print(id(m)) # comprobamos el id en memoria
    print(id(m1))
    print(id(m2))


if __name__ == "__main__":
    main()