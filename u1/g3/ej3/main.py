import random
from soles import Sol 
from sistema_planetario import Sistema_Planetario as Sp
from planetas import Planeta
from nombres import name_planetas, name_soles


def main():
    numero_sistemas = random.randint(2,5)
    array = []
    for a in range(numero_sistemas):
        array.append(crear_sistema())

    imprimir_sistemas(array)


def crear_sistema():
    index_nombre = random.randint(0,19)
    sistema = Sp()
    sistema.set_nombre("Sistema " + name_soles[index_nombre])
    sistema.set_sol(name_soles[index_nombre])
    numero_planetas = random.randint(1, 5)

    for a in range(numero_planetas):
        sistema.set_planeta(crear_planetas())

    for b in range(numero_planetas):
        id = random.randint(0,1000)
        sistema.set_planeta_id(id, b)
    
    return sistema


def crear_planetas():
    index_nombre = random.randint(0, 53)
    planeta = Planeta()
    planeta.set_nombre(name_planetas[index_nombre])
    planeta.set_masa(random.randint(1, 30000)/100)
    planeta.set_densidad(random.randint(10, 1000)/100)
    planeta.set_diametro(random.randint(400000, 20000000)/100)
    planeta.set_orbita_media(random.randint(30, 4000)/100)
    return planeta


def imprimir_sistemas(array):
    for sistema in array:
        sistema.imprimir()



if __name__ == "__main__":
    main()
