from aminoacidos import dic
from proteina import Proteina
from proteinaestructural import ProteinaEstructural as Pes
from proteinaezimatica import ProteinaEnzimatica as Pen
from secuenciaproteina import SecuenciaProteina as Sp
from proteinamutante import ProteinaMutante as Pm
from analizadorproteico import AnalizadorProteico as Ap

import random

def main():
    p1 = Proteina(nombre="Proteina1")
    p2 = Pes(nombre="Proteina2")
    p3 = Pen(nombre="Proteina3")
    p4 = Pm(nombre="Proteina4")

    p1.set_descripcion("Blablabla")
    p2.set_descripcion("blableblu")
    p3.set_descripcion("bleblabloblu")
    p4.set_descripcion("bleblublu")

    p1.set_secuencia(hacer_secuencia(p1))
    p2.set_secuencia(hacer_secuencia(p2))
    p3.set_secuencia(hacer_secuencia(p3))
    p4.set_secuencia(hacer_secuencia(p4))

    p2.set_tipo("GLobUlar")
    p3.set_subtrato("aGUa")

    p2.mostrar_tipo()
    p3.mostrar_subtrato()
    p4.mostrar_mutacion()

    p1.imprimir()
    p2.imprimir()
    p3.imprimir()
    p4.imprimir()

    secuencia = Sp()
    secuencia.add_proteina(p1)
    secuencia.add_proteina(p2)
    secuencia.add_proteina(p3)
    secuencia.add_proteina(p4)

    secuencia.mostrar_secuencias()

    analizador = Ap()
    analizador.add_proteina(p1)
    analizador.add_proteina(p2)
    analizador.add_proteina(p3)
    analizador.add_proteina(p4)

    analizador.mostrar_porcentaje_hidrofobos()
    analizador.mostrar_peso_molecular()



def hacer_secuencia(proteina):
    if isinstance(proteina, Pm):
        tamano1 = random.randint(10, 400)
        tamano_mutacion = random.randint(10, 400)
        tamano2 = random.randint(10, 400)

        secuencia = "M"
        mutacion = ""
        aminoacidos = []
        for i in dic.keys():
            aminoacidos.append(i)
        for j in range(tamano1):
            secuencia = secuencia + aminoacidos[random.randint(0,19)]
        for k in range(tamano_mutacion):
            mutacion = mutacion + aminoacidos[random.randint(0,19)].lower()
        secuencia = secuencia + mutacion.upper()
        for j in range(tamano2):
            secuencia = secuencia + aminoacidos[random.randint(0,19)]
        
        proteina.set_mutacion(mutacion)
        proteina.set_rango(tamano1, (tamano1 + tamano_mutacion))

    else:
        tamano = random.randint(30, 1000)
        secuencia = "M"
        aminoacidos = []
        for i in dic.keys():
            aminoacidos.append(i)
        
        for j in range(tamano):
            secuencia = secuencia + aminoacidos[random.randint(0,19)]


    return secuencia



if __name__ == "__main__":
    main()