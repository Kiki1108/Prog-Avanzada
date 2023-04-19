from Bio.PDB import PDBParser, PDBList

import pathlib

def main():
     # Solo en modo local
    PATH_DIR = pathlib.Path(__file__).parent.absolute()
    #filename = PATH_DIR + '/pdb_folder/7k2h.pdb'
    #parser = PDBParser(QUIET=True)

    #parser = PDBParser(PERMISSIVE = True, QUIET = True) 
    # data = parser.get_structure("2fat","pdb2fat.ent")
    # pdbl = PDBList() 
    # pdbl.retrieve_pdb_file('2FAT', pdir = '.', file_format = 'pdb')
    dir = pathlib.Path("pdb_folder")
    lista = searching_all_files(dir)
    parser = PDBParser(PERMISSIVE = True, QUIET = True)
    print(lista)
    # quit()
    lista2 = []

    for i in lista:
        booleano = False
        nombre = ""
        for x in str(i):
            
            for j in str(x):
                if j == "/":
                    booleano = True
                if booleano:
                    nombre = nombre + j
        parser = PDBParser(PERMISSIVE = True, QUIET = True)         
        data = parser.get_structure(nombre, i)
        print(type(data))
        print(data.get_models())
        for model in data.get_models():
            for chain in model:
                print(chain)
                for res in chain:
                    for atom in res:
                        print(type(atom))
                        print(atom.get_name())
                    break
                break
            break

        print(type(data.header))
        print(data.header.keys())

        nombre = data.header.get("name")
        print(nombre)

        models = data.get_models()

        models = list(models)

        for i in models:
            seq = []
        for x in i.get_residues():
            if x.get_resname() != "HOH":
                seq.append(x.get_resname())

        seq
        lista2.append(data)
        # print(id(data))
    
    print(lista2)
    # print(id(lista2[0]))
    # print(id(lista2[1]))

def searching_all_files(directory: pathlib.Path):   
    file_list = [] # A list for storing files existing in directories

    for x in directory.iterdir():
        print(str(x))
        if x.is_file():
            booleano = False
            nombre = ""
            for i in str(x):
                if i == "/":
                   booleano = True
                if booleano:
                    nombre = nombre + i
            if "pdb" in nombre:
               file_list.append(x)

        else:

           file_list.append(searching_all_files(directory/x))

    return file_list

if __name__ == "__main__":
    main()