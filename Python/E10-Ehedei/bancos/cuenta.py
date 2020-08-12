"""
Clase de cuenta bancaria
"""
class Cuenta(object):
    def __init__(self, titular='John Doe', saldo=0.0):
        self.__titular = titular
        self.__saldo = saldo


    """
    Muestra los datos de la cuenta
    """
    def mostrar_datos(self):
        print("Datos de la cuenta bancaria:")
        print(f'Titular de la cuenta: {self.__titular}')
        print(f'Saldo de la cuenta: {str(self.__saldo)}')


    """
    Getters y Setters
    """
    def get_titular(self):
        return self.__titular


    def get_saldo(self):
        return self.__saldo


    def set_saldo(self, saldo):
        self.__saldo = saldo


    def set_titular(self, titular):
        self.__titular = titular