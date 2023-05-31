class Empleado():
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.salario = None
        self.dp = None

    def calcular_salario(self, salario, horas):
        if horas > 50:
            horas_extras = horas - 50
            dinero_horas_extras = (horas_extras * (salario / 50))
            self.salario = salario + dinero_horas_extras
        else:
            self.salario = salario


    def asignar_departamento(self, departamento):
        self.dp = departamento


    def imprimir_datos(self):
        print(f"{self.nombre}, {self.id}, {self.salario}, {self.dp.nombre}")