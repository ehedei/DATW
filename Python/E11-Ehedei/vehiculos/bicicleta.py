from vehiculo import *

class Bicicleta(Vehiculo):
    def __init__(self, tipo='urbana', color='verde', ruedas=2):
        super().__init__(color, ruedas)
        self.__tipo = tipo


    def get_tipo(self):
        return self.__tipo


    def set_tipo(self, tipo):
        self.__tipo = tipo


    def __str__(self):
        return f'{super().__str__()}\nTipo: {self.__tipo}'