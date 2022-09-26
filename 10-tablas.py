'''
Curso de python para principiantes
Clase 10: crear archivos de texto con las tablas de multiplicar

Como ejecutar el script:
python3 10-tablas numero_de_la_tabla
'''
import sys

if __name__ == "__main__":
    # Obtenemos el numero con el cual haremos las tablas de multiplicar
    num = int(sys.argv[1])
    # Abrimos el archivo en modo de escritura (por eso el parametro 'w',)
    # Al nombre del archivo le agregamos el numero de la tabla
    # Si el archivo ya existe, se sobreescribe
    archivo = open(f'tabla-del-{num}.txt', 'w')
    # Ciclo para hacer las tablas del 1 al 10
    for n in range(1, 11):
        # Escribimos linea por linea el archivo
        archivo.write(f"{num} x {n} = {num * n}\n")
    # Siempre cerrar el archivo
    archivo.close()

    #Nota: lo mejor sería manejar los archivos con with