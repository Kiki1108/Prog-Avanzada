
class Calculadora():
    def __init__(self):
        self.n1 = input("Escriba el primer número \n")
        print("\nEscriba alguna operación básica")
        print("(+) Suma             (-) Resta")
        print("(*) Multiplicación   (/) Divición")
        self.id = input()
        self.n2 = input("\nEscriba el segundo número \n")
        self.resultado = 0

    def suma(self):
        resultado = 0
        try:
            resultado = float(self.n1) + float(self.n2)
        except:
            print("No se ha realizado ninguna operación matemática")
        return resultado
    
    def resta(self):
        resultado = 0
        try:
            resultado = float(self.n1) - float(self.n2)
        except:
            print("No se ha realizado ninguna operación matemática")
        return resultado

    def multiplicacion(self):
        resultado = 0
        try:
            resultado = float(self.n1) * float(self.n2)
        except:
            print("No se ha realizado ninguna operación matemática")
        return resultado

    def divicion(self):
        resultado = 0
        try:
            resultado = float(self.n1) / float(self.n2)
        except:
            print("No se ha realizado ninguna operación matemática")
        return resultado
        
def main():
    c = Calculadora()
    match c.id:
        case "+":
            c.resultado = c.suma()
        case "-":
            c.resultado = c.resta()
        case "*":
            c.resultado = c.multiplicacion()
        case "/":
            c.resultado = c.divicion()
        case othe:
            print("No se ha realizado ninguna operación matemática")
    
    print(c.resultado)


if __name__ == "__main__":
    main()
