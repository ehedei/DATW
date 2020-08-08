"""
Función que recibe un array y devuelve un string formateado, con los elementos separados por guiones
"""
def array_to_string(arrayNumbers):
    return '-'.join(map(str, arrayNumbers))


"""
Función que lee un archivo y devuelve un array de enteros
"""
def read_file():
    file = open('../resources/numeros.txt', 'rt')
    line = file.readline()
    file.close()
    strings = line.split('-')
    numbers = list(map(int, strings))

    return numbers


"""
Función que recibe un array de enteros y los guarda en un archivo: 
1ª Linea: suma de elementos
2ª Linea: elementos ordenados
3ª Linea: elementos ordenados de forma descendente
"""
def write_file(numbers):
    amount = sum(numbers)
    ascNumbers = sorted(numbers)
    descNumbers = sorted(numbers, reverse=True)

    writableFile = open('../resources/resultados.txt', 'wt')
    writableFile.write(str(amount) + '\n')
    writableFile.write(array_to_string(ascNumbers) + '\n')
    writableFile.write(array_to_string(descNumbers))

    writableFile.close()


"""
Procedimiento que maneja un archivo de texto
"""
def handle_file():
    try:
        numbers = read_file()
        write_file(numbers)
        print('Proceso finalizado correctamente.')
    except IOError:
        print('Ha ocurrido un error en el proceso de entrada/salida de datos')

