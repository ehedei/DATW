try:
    numero = int(input('Introduzca un número positivo: '))
    if numero <= 0:
        print('El número no es positivo.')
    else:
        esPrimo = True
        if numero == 1:
            esPrimo = False
        else:
            for indice in range(2, numero - 1):
                if numero % indice == 0:
                    esPrimo = False
                    break

        if(esPrimo):
            print('El número es primo.')
        else:
            print('El número no es primo.')
except ValueError:
    print('La cadena introducida no es un número')