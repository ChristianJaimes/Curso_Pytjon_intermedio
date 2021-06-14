def run():
    """Explicacion:
    Definir una lista con los numeros comprendidos entren 1 y 99999
    que son multiplos de 4 y as su vez tambien son multiplos de 6 y 9
    """
    num_list =[i for i in range (1,100000)if (i%4 == 0 and i%6 == 0 and i%9 ==0)]
    print(num_list)

if __name__ == '__main__':
    run()
    