from vehiculo import *

class Coche(Vehiculo):
    def __init__(self, velocidad=75, cilindrada=1400, color='rojo', ruedas=4):
        super().__init__(color, ruedas)
        self.__velocidad = velocidad
        self.__cilindrada = cilindrada


    def get_velocidad(self):
        return self.__velocidad


    def get_cilindrada(self):
        return self.__cilindrada


    def set_velocidad(self, velocidad):
        self.__velocidad = velocidad


    def set_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada


    def __str__(self):
        return f'{super().__str__()}\nVelocidad: {self.__velocidad}\nCilindrada: {self.__cilindrada}'