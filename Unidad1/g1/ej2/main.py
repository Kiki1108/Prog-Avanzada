

class Tarjeta():
    def __init__(self):
        self.titular = input("Escriba el nombre del titular de la tarjeta\n")

        validar_saldo = False
        while not validar_saldo:
            saldo = input("Escriba el saldo de la tarjeta\n")
            try: 
                saldo = float(saldo)
                validar_saldo = True
            except:
                saldo = 0
                print("Saldo inválido")

        self.saldo = saldo

    def compra(self):
        validar_monto = False
        while not validar_monto:
            monto = input("Escriba el monto de la compra\n")
            try: 
                monto = float(monto)
                validar_monto = True
            except:
                monto = 0
                print("Monto no válido, no se realizó la compra, intente denuevo")
        if self.saldo >= monto:
            self.saldo = self.saldo - monto
        else:
            print("Monto insuficiente, no se realizó la compra, cargue más dinero e intentelo denuevo más tarde")

def main():
    t = Tarjeta()
    t.compra()

    print(f"\nTitular: {t.titular}")
    print(f"Saldo disponible: {t.saldo}")

if __name__ == "__main__":
    main()
