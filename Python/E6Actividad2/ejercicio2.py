teclado = input('Inserte un año (positivo) con el teclado: ')
numero = int(teclado)
if numero <= 0:
    print('El año introducido no es positivo.')
elif numero % 400 == 0 or (numero % 100 != 0 and numero % 4 == 0):
    print('El año es bisiesto.')
else:
    print('El año no es bisiesto.')