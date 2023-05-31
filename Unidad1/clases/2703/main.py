from estudiantes import Estudiante
from carrera import Carrera
from asignaturas import Asignatura


def main():
    c1 = Carrera()
    c1.nombre = "Bioinformática"
    print(c1.nombre)

    calculo1 = Asignatura()
    calculo1.nombre = "Cálculo I"
    calculo1.asociar_carrera(c1)

    a1 = Estudiante()
    a1.nombre = "Cristian"
    a1.incribie_asignatura(calculo1)
    a1.asociar_carrera(c1)

    print(a1.carrera.nombre)
    print(a1.asignaturas_cursando[0].carrera.nombre)

if __name__ == "__main__":
    main()
