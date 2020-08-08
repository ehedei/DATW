"""
Procedimiento que muestra el contenido de un archivo
"""
def show_file(path):
    try:
        file = open(path, 'r', encoding='utf8')
        count = 1;
        while True:
            line = file.readline()
            if len(line) == 0:
                break;
            else:
                print('Linea ' + str(count) + ': ' + line)
                count += 1
        file.close()
    except IOError:
        print('Ha surgido un error en la lectura del archivo.')


def get_file():
    path = input('Introduzca la ruta de su archivo: ')
    show_file(path)