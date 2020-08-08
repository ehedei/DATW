from reader import *

"""
Procedimiento que añade una línea al final del documento.
Parámetros:
path: ruta del archivo
"""
def append_line(path):
    try:
        text = input('Introduzca el texto que debe ser añadido: ')
        file = open(path, 'a', encoding='utf8')
        file.write('\n' + text)
        file.close()

        show_file(path)

    except IOError:
        print('No ha sido posible añadir la línea al archivo')


"""
Procedimiento que sustituye una línea de un texto.
Parámentros:
path: ruta del archivo
option: línea a sustituir 
"""
def substitute_line(path, option):
    try:
        file = open(path, 'r', encoding='utf8')
        lines = file.readlines()
        amount = len(lines)
        if option <= 0 or option >= amount:
            print('La línea elegida no es válida. Está fuera del rango')
            file.close()
        else:
            text = input('Introduzca el texto de la línea que va a ser reemplazada: ')
            lines[option - 1] = text + '\n'
            file = open(path, 'w', encoding='utf8')
            file.writelines(lines)
            file.close()
            print('Resultado:')
            show_file(path)
    except IOError:
        print('No ha sido posible sustituir la línea.')


"""
Procedimiento que gestiona la carga y la modificación de un archivo de texto
"""
def modificate_story():
    path = input('Introduzca la ruta de su cuento: ')
    show_file(path)
    optionString = input('¿Qué línea desea modificar? (0 para añadir al final): ')
    try:
        option = int(optionString)
        if option == 0:
            append_line(path)
        else:
            substitute_line(path, option)
    except ValueError:
        print('Error: El valor insertado no es un número.')