def main():
    palindrome = lambda string: string == string[::-1]
    print(f'usando funciones: {palindrome("ana")}')
    print(f'usando funciones: {palindromeFunction("ana")}')

def palindromeFunction(string):
   return string == string[::-1]

if __name__ == '__main__':
    main()
    