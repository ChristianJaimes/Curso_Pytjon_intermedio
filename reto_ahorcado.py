import os
import random
def main():
    """           Reto del Ahorcado
    Reglas para el desarrollo:
     * Incorportar comprehensions,
       manejo de errores y manejo de archivos.
     * Utilizar el archivo data.txt para leerlo
       y obtener las palabras  

             Ayudas
     * Funcion enumerate
     * metodo get de los diccionarios
     * Sentencia 
         os.system("cls") -> en windows
         os.system("clear") -> en Unix
    """
    pass
def run():
      os.system("cls")
      palabraOriginal = getPalabraOriginal()
      palabraOculta = ocultarPalabra(palabraOriginal)
      print(palabraOculta)
      print(getPalabraclave(palabraOriginal))
      letra = input("ingresa una letra")
      for i in range(0,len(palabraOculta)):
            
            if letra == palabraOriginal[i]:
                  palabraOculta[i] = letra
      print(palabraOculta)
      palabraOculta.replace()                  

def ocultarPalabra(palabraOriginal):
      """Muestra _ en lugar de las letras de la palabra
      """
      palabraOculta = "_ "*len(palabraOriginal)
      return palabraOculta[:-1]
      

def getPalabraclave(palabraOriginal):
      """Tratamiento de la palabra original de forma que quede
      E S P A C I A D A la palabra clave y sea facil de comparar
      """
      palabraClave = ""
      tam = len(palabraOriginal)
      for i in range(0,tam):
                  palabraClave += palabraOriginal[i]
                  palabraClave += " "             
      return palabraClave[:-1]
            
      

def getPalabraOriginal():
      
      """ Retorna una palabra aleatoria contenida dentro del archivo data.txt
      ARGS : null
      RETURN: 
          String:
                Palabra extraida del archivo data.txt
      """
      all_Words = []
      with open ("./data.txt","r",encoding="utf-8") as file:
        for line in file:
              all_Words.append(line.replace("\n",""))
      palabraClave = all_Words[random.randint(0,len(all_Words))]
      return palabraClave
      
                         

if __name__ == '__main__':
    run()
    