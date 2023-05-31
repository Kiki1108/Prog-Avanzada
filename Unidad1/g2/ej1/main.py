from empleados import Empleado as Ep
from departamento import Departamento as Dp


def crear_diccionario():
    nombres_departamentos = ["aa", "bb", "cc"]
    dic = {}

    for i in nombres_departamentos:
        nuevo = Dp(i)
        dic[i] = nuevo

    return dic


def main():
    emp1 = Ep("E0001", "Alejandro")
    emp1.calcular_salario(10000, 90)

    dic = crear_diccionario()

    emp1.asignar_departamento(dic["bb"])

    print(dic[1])

    emp1.imprimir_datos()


if __name__ == "__main__":
    main()
