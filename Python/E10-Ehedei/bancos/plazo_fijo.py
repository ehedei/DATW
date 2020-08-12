from cuenta import *

"""
Clase para cuenta de Plazo Fijo
"""
class PlazoFijo(Cuenta):
    def __init__(self, titular='Jane Doe', saldo=1.0, plazo=24, interes=7):
        Cuenta.__init__(self, titular, saldo)
        self.__plazo = plazo
        self.__interes = interes


    """
    Método que muestra los datos de la cuenta
    """
    def mostrar_datos(self):
        print('Tipo de cuenta: Plazo Fijo')
        Cuenta.mostrar_datos(self)
        print(f'Plazo de la cuenta: {str(self.__plazo)}')
        print(f'Interés de la cuenta: {str(self.__interes)}')


    """
    Método que devuelve el interés originado por la cuenta
    """
    def calcular_interes(self):
        return self.get_saldo() * self.__interes / 100


    """
    Setters y getters
    """
    def get_plazo(self):
        return self.__plazo


    def get_interes(self):
        return self.__plazo


    def set_interes(self, interes):
        self.__interes = interes


    def set_plazo(self, plazo):
        self.__plazo = plazo