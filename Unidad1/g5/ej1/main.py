from perro import Perro
from gato import Gato


def main():
    toby = Perro("Toby")
    toby.set_genero("M")
    toby.set_edad(1)

    print(f"\nNombre: {toby.get_nombre()}")
    print(f"Genero: {toby.get_genero()}")
    print(f"Edad: {toby.get_edad()}")
    toby.ladrar()

    michi = Gato("Michi")
    michi.set_genero("H")
    michi.set_edad(2)

    print(f"\nNombre: {michi.get_nombre()}")
    print(f"Genero: {michi.get_genero()}")
    print(f"Edad: {michi.get_edad()}")
    michi.maullar()


if __name__ == "__main__":
    main()