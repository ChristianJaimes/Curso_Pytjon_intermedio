def main():
  #  palindrome = lambda string: string == string[::-1]
   # print(f'usando funciones: {palindrome("ana")}')
    try:
     print(f'usando funciones: {palindromeFunction("")}')
    except TypeError:
        print("Solo se pueden ingresar strings")

def palindromeFunction(string):
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacia")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

if __name__ == '__main__':
    main()
    