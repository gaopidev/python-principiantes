'''
Curso de python para principiantes
Clase 04: uso de listas

Como ejecutar el script:
python3 04-listas.py
'''
if __name__ == "__main__":
    # Encontrar el numero mas grande en una lista
    lista = [32, 12, 98, 1, 4, 128, 16, 14, 11, 256, 2]

    # En la variable may guardaremos el numero mas grande, en este caso la inicializamos con el 
    # primer elemento de la lista
    may = lista[0]
    # Recorremos la lista elemento por elemento
    for num in lista:
        if num > may:   # Si el elemento de la lista es mas grande que may, lo reemplazamos
            may = num

    # Este ejercicio se puede resolver con max()
    # may = max(lista)

    print("El numero mas grande de la lista es:", may)
