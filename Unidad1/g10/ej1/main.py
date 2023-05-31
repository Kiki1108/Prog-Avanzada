from circulo import Circulo
from rectangulo import Rectangulo


def main():
    cir = Circulo(10)
    cir.calcular_area()
    cir.calcular_perimetro()

    rec = Rectangulo(base=10, altura=20)
    rec.calcular_area()
    rec.calcular_perimetro()


if __name__ == "__main__":
    main()
