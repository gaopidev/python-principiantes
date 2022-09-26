'''
Curso de python para principiantes
Clase 08: tabla de conversion de temperaturas Celsius - Fahrenheit.
El usuario ingresa temperatura Celsius inicial, el numero de 
conversiones a realizar y cuantos grados Celsius entre cada conversion 

Como ejecutar el script:
python3 08-temperatura.py temp_inicial num_registros diferencia
'''
import argparse

if __name__ == "__main__":

    # Descripcion acerca del uso del scripts, se muestra con el flag -h o --help
    parser = argparse.ArgumentParser(description="Conversion de unidades Celsius-Fahrenheit")
    # Añadimos los argumentos que se requieren para usar el script
    # flag, nombre_argumento, nombre_para_usar_como_variable, valor_por_defecto, tipo_de_dato, descripcion
    parser.add_argument('-i', '--inicio', dest='inicio', default=0, type=float, help='Temperatura inicial en Celsius')
    parser.add_argument('-n', '--numero', dest='numero', default=10, type=int, help='Numero de conversiones a realizar')
    parser.add_argument('-p', '--paso', dest='paso', default=10, type=float, help='Diferencia entre conversiones')
    # variable que contendra el valor de los argumentos
    args = parser.parse_args()
    
    temp_c = args.inicio
    num_co = args.numero
    paso   = args.paso

    # Repetir segun el numero indicado en num_co
    for n in range(0, num_co):
        # fahrenheit = (celsius * (9/5)) + 32
        fah = (temp_c * 1.8) + 32
        print(f"{temp_c}º C\t{fah:.2f}º F")
        # incrementamos el valor de celsius segun el argumento que paso el usuario
        temp_c += paso
