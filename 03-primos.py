'''
Curso de python para principiantes
Clase 03: numeros primos

Como ejecutar el script:
python3 03-primos.py
'''
# def palabra reservada para definir funciones
# def nombre_de_la_funcion(argumentos):
def es_primo(num):
    # 1 no es primo, se descarta
    if num < 2:
        return False
    # Recorremos mediante for el rango de numeros del 2
    # hasta num/2 +1 (+1 porque range no es inclusivo en el limite)
    for n in range(2, int(num/2) + 1):
        # revisamos si el residuo de dividir num/n es igual a 0
        if num % n == 0:
            return False
    # Al no encontrar un divisor entero dentro del rango, entonces num es primo
    return True


if __name__ == "__main__":

    # Pedimos al usuario el numero a revisar
    # num = int(input("Escribe un numero para saber si es primo: "))
    inp = input("Escribe un numero para saber si es primo: ")
    num = int(inp)

    # invocamos la funcion con su nombre y parametros
    # nombre_de_la_funcion(parametros)
    # es_primo() retorna True o False
    if es_primo(num): # True
        print("Es primo")
    else: # False
        print("No es primo")
