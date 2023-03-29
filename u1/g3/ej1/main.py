from perro import Perro


def main():
    p1 = Perro()
    p2 = Perro()

    print("Elija el nombre del perro (1)")
    while not p1.get_nombre():
        p1.set_nombre(input())

    print("Elija el nombre del perro (2)")
    while not p2.get_nombre():
        p2.set_nombre(input())

    menu(p1, p2)


def menu(p1, p2):
    termino = False

    while not termino:
        perro = None
        while perro != 1 and perro != 2 and perro != 0:
            print("\nElija el perro:")
            print(f"(1) {p1.get_nombre()}")
            print(f"(2) {p2.get_nombre()}")
            print("(0) Salir de la experiencia")
            try:
                perro = int(input())
            except:
                print("Intentelo denuevo")
                continue
        
        if perro == 0:
            break 

        accion = None

        while accion != 1 and accion != 2 and accion != 3 and accion != 4 and accion != 5 and accion != 6:
            print("\nEscriba la acción que quierra realizar")
            print("(1) Tomar agua")
            print("(2) Escribir hace cuantas horas tomó agua")
            print("(3) Ver hace cuanto tomó agua")
            print("(4) Pasear")
            print("(5) Dejar de pasear")
            print("(6) Ver si está paseando")
            try:
                accion = int(input())
            except:
                print("Intentelo denuevo")
                continue
        
        if perro == 1:
            acciones(p1, accion)
        else:
            acciones(p2, accion)
        

def acciones(perro, accion):
    match accion:
        case 1:
            perro.tomar_agua()
        case 2:
            perro.set_hora_toma_agua()
        case 3:
            print(f"Tomó agua hace {perro. get_hora_toma_agua()} Horas")
        case 4:
            perro.pasear()
        case 5:
            perro.dejar_pasear()
        case 6:
            perro.ver_paseo()


if __name__ == "__main__":
    main()
