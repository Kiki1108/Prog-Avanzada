from planetas import Planeta

class Sistema_Planetario():
    def __init__(self) -> None:
        self.__nombre = None
        self.__sol = None
        self.__planetas = []

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre
    
    def set_sol(self, sol):
        self.__sol = sol
    
    def get_sol(self):
        return self.__sol
    
    def set_planeta(self, planeta):
        if isinstance(planeta, Planeta):
            for a in range(len(self.__planetas)):
                if self.__planetas[a].get_id() == planeta.get_id() and planeta.get_id() != None:
                    print("Id del planeta ya se encuentra en el sistema planetario")
                    return
            self.__planetas.append(planeta)
        else:
            print("planeta inválido")
            
    def get_planetas(self):
        return self.__planetas
    
    def set_planeta_id(self, id, p):
        for a in range(len(self.__planetas)):
            if self.__planetas[a].get_id() == id and self.__planetas[a] != self.__planetas[p]:
                self.__planetas[p].set_id(None)
                print("Id Repetida en el sistema")
                break
            else:
                self.__planetas[p].set_id(id)
    
    def imprimir(self):
        print(self.get_nombre())
        print(f"    Estrella: {self.get_sol()}")
        for a in self.get_planetas():
            a.imprimir_planeta()
