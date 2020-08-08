from reader_writer import *
from reader import *
from story_modificator import *


"""
Procedimiento que imprime el menú de la aplicación por pantalla.
"""
def print_menu():
    print('-----------------------------------------')
    print('Menú:')
    print('1. Entrada/salida del archivo números.')
    print('2. Leer un archivo de texto plano.')
    print('3. Alterar un cuento.')
    print('Cualquier otro valor para finalizar')


"""
Procedimiento que imprime el menú de la aplicación por pantalla.
"""
def run_menu():
    runMenu = True

    while runMenu:
        print_menu()
        opcion = input('Seleccione una opción: ')
        if opcion == '1':
            handle_file()

        elif opcion == '2':
            get_file()

        elif opcion == '3':
            modificate_story()

        else:
            print('Ha seleccionado abandonar la aplicación. ¡Hasta pronto!')
            runMenu = False
