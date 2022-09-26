'''
Curso de python para principiantes
Clase 09: devolver el numero n de la secuencia Fibonacci

Como ejecutar el script:
python3 09-fibonacci numero
'''
import sys

def fibonacci(num):
    if num <= 0:
        print("Valor incorrecto")
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

if __name__ == "__main__":
    # Obtenemos el numero desde los argumentos
    num = int(sys.argv[1])
    # Invocamos la funcion recursiva
    fib = fibonacci(num)
    # Imprimimos el numero obtenido en la funcion
    print(f"El {num}º numero de la secuencia Fibonacci es {fib}") 