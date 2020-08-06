"""
Función que valida la longitud mínima de un texto
"""
def validate_min_length(name):
    valid = True
    if len(name) < 6:
        print('El nombre de usuario debe contener al menos 6 caracteres')
        valid = False

    return valid


"""
Función que valida la longitud máxima de un texto
"""
def validate_max_length(name):
    valid = True
    if len(name) > 12:
        print('El nombre de usuario no puede contener más de 12 caracteres')
        valid = False

    return valid


"""
Función que valida que un nombre tiene sólo carácteres alfanuméricos
"""
def validate_alphanumeric(name):
    valid = True
    if not name.isalnum():
        print('El nombre de usuario puede contener solo letras y números')
        valid = False

    return valid


"""
Función que valida un nombre
"""
def validate_name(name):
    valid = True
    if not validate_min_length(name):
        valid = False

    if not validate_max_length(name):
        valid = False

    if not validate_alphanumeric(name):
        valid = False

    return valid