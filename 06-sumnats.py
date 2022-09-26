'''
Curso de python para principiantes
Clase 06: Suma de los primeros n numeros naturales

Como ejecutar el script:
python3 06-sumnats.py
'''
if __name__ == "__main__":
    # Entrada del numero para calcular la suma
    num = int(input("Escribe el numero para calcular la suma: "))
    if num < 0:
        print("El numero debe ser mayor a 0")
        exit()
    else:
        sum = 0
        for n in range(1, num+1):
            sum += n
    print("La suma de los primeros", num, "numeros es", sum)