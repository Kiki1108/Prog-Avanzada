class Asignatura():
    def __init__(self) -> None:
        self.nombre = None
        self.carrera = None

    def asociar_carrera(self, carrera):
        self.carrera = carrera