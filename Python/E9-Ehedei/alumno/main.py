from menu import *
from alumno import *

alumno = None

print('-----------------------------')
print('Inicio del programa Alumno:')

while True:
    nombre = insertar_nombre()
    nota = 0

    while True:
        try:
            nota = insertar_nota()
            break
        except ValueError:
            print('Debe insertar un valor entero para continuar.')

    try:
        alumno = Alumno(nombre, nota)
        break
    except Exception as e:
        print(e)


usar_menu(alumno)