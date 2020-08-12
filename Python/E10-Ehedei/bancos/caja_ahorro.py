from cuenta import *

"""
Clase de cuenta de ahorro
"""
class CajaAhorro(Cuenta):
    def __init__(self, titular='Jane Doe', saldo=1.0):
        Cuenta.__init__(self, titular, saldo)

    """
    Método que muestra los datos de la cuenta
    """
    def mostrar_datos(self):
        print('Tipo de cuenta: Cuenta de ahorro')
        Cuenta.mostrar_datos(self)