'''
Curso de python para principiantes
Clase 05: factorial de un numero

Como ejecutar el script:
python3 05-factorial.py
'''
import sys

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        # Recursividad
        return num * factorial(num - 1)

if __name__ == "__main__":

    # Pedir el numero al usuario
    num = int(input("Numero para calcular el factorial: "))
    print("El factorial de", num, "es", factorial(num))
