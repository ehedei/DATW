from alumno import *


"""
Función que solicita un nombre al usuario y lo devuelve
"""
def insertar_nombre():
    nombre = input("Inserte el nombre del alumno (entre 1 y 20 caractéres): ")
    return nombre


"""
Función que solicita una nota al usuario y la devuelve
"""
def insertar_nota():
    nota = int(input("Inserte la nota del alumno (número entero entre 0 y 10): "))
    return nota



"""
Procedimiento que gestiona el cambio de nombre del alumno por el usuario
"""
def cambiar_nombre(alumno):
    while True:
        try:
            alumno.set_nombre(insertar_nombre())
            break
        except Exception as e:
            print(e)


"""
Procedimiento que gestiona el cambio de nota del alumno por el usuario
"""
def cambiar_nota(alumno):
    while True:
        try:
            alumno.set_nota(insertar_nota())
            break
        except Exception as e:
            print(e)


"""
Procedimiento que muestra el menú
"""
def mostrar_menu():
    print('-----------------------')
    print('Menú:')
    print('1. Alterar el nombre del Alumno')
    print('2. Alterar la nota del Alumno')
    print('3. Consultar los datos del Alumno')
    print('4. Ver la nota del Alumno')
    print('5. Ver el nombre del alumno')
    print('Cualquier otro valor para salir')


"""
Procedimiento que maneja las interacciones del usuario con el menú del programa
"""
def usar_menu(alumno):
    mostrar = True

    while mostrar:
        mostrar_menu()
        opcion = input('¿Qué desea hacer? Inserte la opción deseada: ')
        if opcion == '1':
            cambiar_nombre(alumno)
        elif opcion == '2':
            cambiar_nota(alumno)
        elif opcion == '3':
            alumno.imprimir_datos()
        elif opcion == '4':
            alumno.imprimir_nota()
        elif opcion == '5':
            alumno.imprimir_nombre()
        else:
            print('Ha elegido salir de la aplicación. ¡Hasta la vista!')
            mostrar = False
