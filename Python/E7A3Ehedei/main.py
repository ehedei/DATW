from name_validator import *


name = input('Introduzca un nombre a continuación, para que pueda ser validado: ')
if validate_name(name):
    print('El nombre está validado')
