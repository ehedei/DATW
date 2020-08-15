from camioneta import *
from motocicleta import *
import pickle

def definir_datos_iniciales():
    """
    Función que crea una lista inicial de vehículos con los que trabajar
    :return: Lista de vehículos
    """
    vehiculos = []
    vehiculos.append(Coche())
    vehiculos.append(Camioneta())
    vehiculos.append(Bicicleta())
    vehiculos.append(Motocicleta())
    return vehiculos


def leer_datos():
    """
    Función que lee los vehículos guardados en un archivo y los devuelve en forma de lista
    :return: Listado de vehículos
    """
    file = open('../resources/data', 'rb')
    vehiculos = pickle.load(file)
    file.close()
    return vehiculos


def guardar_datos(vehiculos):
    """
    Procecimiento que guarda los datos del programa
    :param vehiculos:  Diccionario con las listas de cada tipo de vehículo
    """
    try:
        file = open('../resources/data', 'wb')
        pickle.dump(vehiculos, file, pickle.HIGHEST_PROTOCOL)
        file.close()
    except IOError:
        print('No se han podido salvar los datos')


def catalogar(vehiculos, ruedas=-1):
    """
    Muestra los vehículos de una lista
    :param vehiculos: listado de vehiculos
    :param ruedas: Opcional. Número de ruedas que tiene los vehículos que se desean mostrar
    """
    if ruedas != -1:
        vehiculos = list(filter(lambda v: v.get_ruedas() == ruedas, vehiculos))
        print(f'\nSe ha encontrado {len(vehiculos)} vehículos con {ruedas} ruedas.\n')

    for vehiculo in vehiculos:
        print('---------------------')
        print(f'Índice del vehículo: {vehiculos.index(vehiculo) + 1}')
        print(vehiculo, '\n')

    print('---------------------')


def mostrar_vehiculos(data):
    """
    Procedimiento que permite al usuario elegir qué forma desea de ver los vehiculos de la lista
    :param data: lista de vehículos
    :return:
    """
    print('---------------------')
    print('¿Qué tipo de vehículos desea ver?')
    print('1. Coches')
    print('2. Camionetas')
    print('3. Bicicletas')
    print('4. Motocicletas')
    print('5. Todos')
    print('6. Según el número de ruedas')
    print('Cualquier otra cosa para volver')
    opcion = input('Inserte su opción: ')
    if opcion == '1':
        mostrar_segun_tipo(data, 'Coche')
    elif opcion == '2':
        mostrar_segun_tipo(data, 'Camioneta')
    elif opcion == '3':
        mostrar_segun_tipo(data, 'Bicicleta')
    elif opcion == '4':
        mostrar_segun_tipo(data, 'Motocicleta')
    elif opcion == '5':
        print('Listado de todos los vehículos:')
        catalogar(data)
    elif opcion == '6':
        mostrar_segun_ruedas(data)


def mostrar_segun_ruedas(data):
    """
    Procedimiento que permite mostrar los vehículos de la lista con un número determinado de ruedas
    :param data: listado de vehiculos
    """
    try:
        print('---------------------')
        ruedas = int(input('Introduzca el número de ruedas: '))
        if ruedas < 1:
            print('No existen vehículos sin ruedas')
        else:
            print(f'Lista de Vehículos de {ruedas} ruedas')
            catalogar(data, ruedas)
    except ValueError:
        print('Se ha producido un error: Ha insertado datos numéricos de forma incorrecta. Operación cancelada')


def mostrar_segun_tipo(data, tipo):
    """
    Procecimiento que permite mostrar los vehículos de la lista según el tipo de vehículo
    :param data: Lista de vehículos
    :param tipo: String. Tipo de vehículo a mostrar
    """
    lista = list(filter(lambda v: type(v).__name__ == tipo, data))
    print(f'Lista de vehículos de tipo {tipo}:')
    catalogar(lista)


def crear_vehiculo(data, tipoVehiculo):
    """
    Procedimiento que permite crear y añadir un vehículo a la lista según los valores decididos por el usuario
    :param data: listado de vehículos
    :param tipoVehiculo: Tipo de vehículo
    """
    try:
        color = input('Inserte el color: ')
        ruedas = int(input('Inserte el número de ruedas: '))

        tipo = ''
        velocidad = 0
        cilindrada = 0
        carga = 0

        if tipoVehiculo != 'bicicleta':
            velocidad = int(input('Inserte la velocidad máxima en km/h (valor entero): '))
            cilindrada = int(input('Inserte la cilindrada en cc (valor entero): '))

        if tipoVehiculo == 'bicicleta' or tipoVehiculo == 'motocicleta':
            tipo = input('Inserte el tipo de vehículo (deportiva, urbana, etc): ')

        if tipoVehiculo == 'camioneta':
            carga = int(input('Inserte la carga máxima en kg (valor entero): '))

        vehiculo = None
        if tipoVehiculo == 'coche':
            vehiculo = Coche(velocidad, cilindrada, color, ruedas)
        elif tipoVehiculo == 'camioneta':
            vehiculo = Camioneta(carga, velocidad, cilindrada, color, ruedas)
        elif tipoVehiculo == 'bicicleta':
            vehiculo = Bicicleta(tipo, color, ruedas)
        else:
            vehiculo = Motocicleta(velocidad, cilindrada, tipo, color, ruedas)

        data.append(vehiculo)

        print("Vehículo insertado correctamente.")

    except ValueError:
        print('Se ha producido un error: Ha insertado datos numéricos de forma incorrecta. Operación cancelada')


def mostrar_creacion_vehiculo(data):
    """
    Procedimiento que permite decidir que tipo de vehículo se añadirá a la lista
    :param data: lista de vehículos
    """
    print('---------------------')
    print('¿Qué tipo de vehículo quiere añadir?')
    print('1. Coche')
    print('2. Camioneta')
    print('3. Bicicleta')
    print('4. Motocicleta')
    print('Cualquier otra cosa para volver')
    opcion = input('Inserte su opción: ')
    if opcion == '1':
        crear_vehiculo(data, 'coche')
    elif opcion == '2':
        crear_vehiculo(data, 'camioneta')
    elif opcion == '3':
        crear_vehiculo(data, 'bicicleta')
    elif opcion == '4':
        crear_vehiculo(data, 'motocicleta')


def mostrar_afectar_vehículo(data, operacion):
    """
    Procedimiento que permite seleccionar un vehiculo de la lista y aplicar sobre él la operacion pasada por parámetro
    :param data: Listado de vehiculos
    :param operacion: Operación que se desea ejecutar sobre el objeto
    """
    print('---------------------')
    print('Listado de vehículos: ')
    catalogar(data)
    try:
        index = int(input('Inserte el índice del vehículo: ')) - 1
        if index < 0 or index >= len(data):
            print('El valor insertado está fuera del rango.')
        else:
            if operacion == 'eliminar':
                data.pop(index)
            else:
                mostrar_modificar_vehiculo(data, index)
    except ValueError:
        print('Se ha producido un error: Ha insertado datos numéricos de forma incorrecta. Operación cancelada')


def mostrar_modificar_vehiculo(data, index):
    """
    Procedimiento que modifica un vehículo
    :param data: Listado de vehículos
    :param index: Indice del vehículo a modificar
    """
    vehiculo = data[index]
    clase = type(vehiculo).__name__
    try:
        print('---------------------')
        print(f'Color actual del vehículo: {vehiculo.get_color()}')
        color = input('Inserte el nuevo color (en blanco para omitir): ')
        if len(color) > 0:
            vehiculo.set_color(color)

        print(f'Número de ruedas actuales del vehículo: {vehiculo.get_ruedas()}')
        ruedas = input('Inserte el nuevo número de ruedas (en blanco para omitir): ')
        if len(ruedas) > 0:
            vehiculo.set_ruedas(int(ruedas))


        if clase != 'Bicicleta':
            print(f'Velocidad actual del vehículo: {vehiculo.get_velocidad()} km/h')
            velocidad = input('Inserte la velocidad máxima en km/h [valor entero] (en blanco para omitir): ')
            if len(velocidad) > 0:
                vehiculo.set_ruedas(int(ruedas))

            print(f'Cilindrada actual del vehículo: {vehiculo.get_cilindrada()} cc')
            cilindrada = input('Inserte la cilindrada en cc [valor entero] (en blanco para omitir): ')
            if len(cilindrada) > 0:
                vehiculo.set_cilindrada(int(cilindrada))

        if clase == 'Bicicleta' or clase == 'Motocicleta':
            print(f'Tipo actual del vehículo: {vehiculo.get_tipo()}')
            tipo = input('Inserte el tipo de vehículo (deportiva, urbana, etc) (en blanco para omitir): ')
            if len(tipo) > 0:
                vehiculo.set_tipo(tipo)

        if clase == 'Camioneta':
            print(f'Carga máxima actual del vehículo: {vehiculo.get_carga()} kg')
            carga = input('Inserte la carga máxima en kg (valor entero): (en blanco para omitir)')
            if len(carga) > 0:
                vehiculo.set_tipo(carga)

    except ValueError:
        print('Se ha producido un error: Ha insertado datos numéricos de forma incorrecta. Operación interrumpida')
    finally:
        print('Datos actuales del vehículo:')
        print(vehiculo)

def mostrar_menu():
    """
    Procedimiento que muestra el menú principal de la aplicación
    """
    print('-----------------------')
    print('Menú Principal:')
    print('¿Qué desea hacer?')
    print('1. Mostrar Vehículos')
    print('2. Crear Vehículo')
    print('3. Eliminar Vehículo')
    print('4. Modificar Vehículo')
    print('Cualquier otro valor para guardar y salir')


def usar_menu(data):
    """
    Procedimiento que permite al usuario gestionar el menú principal de la aplicación
    :param data: listado de vehículos
    """
    while True:
        mostrar_menu()
        opcion = input('¿Qué desea hacer? Inserte la opción deseada: ')
        if opcion == '1':
            mostrar_vehiculos(data)
        elif opcion == '2':
            mostrar_creacion_vehiculo(data)
        elif opcion == '3':
            mostrar_afectar_vehículo(data, 'eliminar')
        elif opcion == '4':
            mostrar_afectar_vehículo(data, 'modificar')
        else:
            guardar_datos(data)
            print('Ha elegido salir de la aplicación. ¡Hasta la vista!')
            break


try:
    datos = leer_datos()
except IOError:
    datos = definir_datos_iniciales()

usar_menu(datos)