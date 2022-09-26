'''
Curso de python para principiantes
Clase 07: devolver la cantidad de digitos de un numero

Como ejecutar el script:
python3 07-digitos.py
'''
if __name__ == "__main__":
    # Entrada del usuario
    num = int(input("Escribe un numero: "))
    # Variable para modificar el valor de entrada
    n = num
    # Contador de digitos
    dig = 0

    while n > 0:
        dig = dig + 1
        # Al dividir entre 10 vamos descartando un digito
        n = n // 10
    
    print("El numero", num, "tiene", dig, "digitos")