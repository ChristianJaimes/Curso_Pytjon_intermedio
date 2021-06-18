def divisors(num):
    assert int(num) > 0, "Debes ingresar numeros positivos"
    divisors =[]
    for i in range(1,num + 1):
         if num % i == 0:
             divisors.append(i)
    return divisors
    

def run():
    num = input("Ingresa un numero: " )
    assert num.replace("-","").isnumeric(),"Debes ingresar un valor numerico"
    print(divisors(int(num)))
    ValueError
    SyntaxError
    print("termino el programa")

if __name__ == '__main__':
    run()
    