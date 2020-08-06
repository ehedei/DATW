try:
    teclado = input('Introduzca un número positivo por teclado: ')
    numero = int(teclado)

    if numero <= 0:
        print('El número insertado no es positivo.')
    else:
        cantidadCifras = 0;
        while numero >= 1:
            numero = numero / 10
            cantidadCifras += 1
        print("El número de cifras es ", cantidadCifras)

except ValueError:
    print('La cadena introducida no es un número')