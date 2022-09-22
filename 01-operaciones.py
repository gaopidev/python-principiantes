'''
Curso de python para principiantes:
Clase 01: opera dos numeros

Como ejecutar el script:
python3 01-operaciones.py numero1 numero2
'''
import sys

if __name__ == "__main__":
    # Obtener los dos numeros a operar 
    num1, num2 = sys.argv[1], sys.argv[2]
    # Convertir a numeros enteros
    num1 = int(num1)
    num2 = int(num2)

    # suma
    # caracteristica de python 3.6+ formateo de string f"{}"
    print(f"{num1} + {num2} = {num1 + num2}")
    # resta
    print(f"{num1} - {num2} = {num1 - num2}")
    # multiplicacion
    print(f"{num1} x {num2} = {num1 * num2}")
    # division
    print(f"{num1} / {num2} = {num1 / num2}")