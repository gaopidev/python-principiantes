'''
Curso de python para principiantes
Clase 02: palindromos

Como ejecutar el script:
python3 02-palindromos.py palabra
'''
import sys

if __name__ == "__main__":
    # Obtenemos la palabra que vamos a revisar
    palabra = sys.argv[1]
    # Quitamos los espacios en blanco
    pal_se = palabra.strip().replace(" ", "")
    # Obtenemos el reverso de la palabra
    rev = pal_se[::-1]

    if pal_se == rev:
        print("Es palindromo")
    else:
        print("No es palindromo")
