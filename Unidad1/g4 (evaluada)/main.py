from secuenciador import Secuanciador as Sd

def main():
    lista, patron = menu()
    secuenciador = crear_secuencias(lista)
    imprimir_datos(secuenciador, patron)


def menu():
    while True:
        print("¿Cuantas veces va a secuenciar?")
        veces = input("")
        try:
            veces = int(veces)
            break
        except:
            print("Número no válido")

    lista = []
    for i in range(veces):
        while True:
            print(f"Escriba la cantidad aproximada de nucleotidos de la secuencia {i + 1}")
            cantidad = input("")
            try:
                cantidad = int(cantidad)
                break
            except:
                print("Número no válido")
        lista.append(cantidad)

    condicion = True
    while condicion:
        print("Introduzca el patrón a buscar")
        patron = input("").upper()
        condicion = False
        for i in patron:
            if i not in ["A", "C", "T", "G"]:
                condicion = True
                break

    return lista, patron


def imprimir_datos(secuenciador, patron):
    contador = 0
    for i in secuenciador.get_cadenas():
        if contador % 2:
            print("\nSecuencia Inversa:")
        else:
            print("\n", "#"*50)
            print("\nSecuencia:")
        print(f"{i.get_secuencia()}")
        print(f"\nLongitud: {i.get_longitud()}")

        dic = i.contar_nucleotidos()
        print("\nVeces que aparecen los nucleótidos:")
        print("A", dic.get("A"))
        print("T", dic.get("T"))
        print("C", dic.get("C"))
        print("G", dic.get("G"))

        print(f"\nPeso Molecular: {i.calcular_peso_molecular()}")
        lista = i.encontrar_patron(patron)
        print(f"\nPosiciones donde aparece el patron:\n{lista}\n")

        contador += 1


def crear_secuencias(longitud):
    secuenciador = Sd()
    for i in longitud:
        print(i)
        secuenciador.set_longitud(i)
        secuenciador.generar_cadena()
    return secuenciador

if __name__ == "__main__":
    main()
