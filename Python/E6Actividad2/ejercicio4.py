try:
    base = float(input('Introduzca un número real (base): '))
    exponente = int(input('Introduzca un número entero (exponente): '))

    print('El resultado es: ', base ** exponente)

except ValueError:
    print('La cadena introducida no es un número')