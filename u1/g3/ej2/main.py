from vacunas import Vacuna

def main():
    vacunas = []

    termino = False
    while not termino:
        print("\nElija la acción")
        print("(1) Agregar vacuna")
        print("(2) Agregar efecto secundario")
        print("(3) Ver vacunas")
        print("(4) Ver efectos secundarios")
        print("(0) Salir de la experiencia")

        try:
            accion = int(input())
            if accion < 0 or accion > 4:
                print("\nAcción no válida\n")
                continue
        except:
            print("\nAcción no válida\n")
            continue

        match accion:
            case 0:
                break
            case 1:
                v = Vacuna()
                while not v.get_nombre(): 
                    print("\nEscriba el nombre de la vacuna")
                    nombre = input()
                    v.set_nombre(nombre)
                while not v.get_lab():
                    print("\nEscriba el nombre del laboratorio")
                    laboratorio = input()
                    v.set_lab(laboratorio)
                vacunas.append(v)
            case 2:
                print("\nElija la vacuna:")
                ver_vacunas(vacunas)
                try:
                    eleccion = int(input())
                    if eleccion -1 < 0 or eleccion -1 > len(vacunas):
                        print("\nAcción no válida\n")
                        continue
                except:
                    print("\nAcción no válida\n")
                    continue
                print("\nEscriba el efecto secundario")
                efecto_secundario = input()
                vacunas[eleccion-1].add_efectos_secundarios(efecto_secundario)
            case 3:
                ver_vacunas(vacunas)
            case 4:
                print("\nElija la vacuna:")
                ver_vacunas(vacunas)
                try:
                    eleccion = int(input())
                    if eleccion -1 < 0 or eleccion -1 > len(vacunas):
                        print("\nAcción no válida\n")
                        continue
                except:
                    print("\nAcción no válida\n")
                    continue
                vacunas[eleccion-1].get_efectos_secundarios()

   
def ver_vacunas(vacunas):
    contador = 1
    for a in range(len(vacunas)):
        print(f"({contador}) {vacunas[a].get_nombre()}, laboratorio: {vacunas[a].get_lab()} ")
        contador = contador + 1


if __name__ == "__main__":
    main()
