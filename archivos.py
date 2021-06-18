def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding= "utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print (numbers)

def write():
    #names = ["Facundo","Migel","Pepe","Christian","Rocío"]
    names = ["Sara","Maria"]
    with open("./archivos/names.txt","a", encoding = "utf-8") as f :#a-> añadir w -> sobreescribir
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    read()
    write()


if __name__ == '__main__':
    run()
    