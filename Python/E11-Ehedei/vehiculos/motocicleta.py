from bicicleta import *

class Motocicleta(Bicicleta):
    def __init__(self, velocidad=80, cilindrada=500, tipo='deportiva', color='negro', ruedas=2):
        super().__init__(tipo, color, ruedas)
        self.__velocidad = velocidad
        self.__cilindrada = cilindrada


    def __str__(self):
        return f'{super().__str__()}\nVelocidad: {self.__velocidad}\nCilindrada: {self.__cilindrada}'


    def get_velocidad(self):
        return self.__velocidad


    def get_cilindrada(self):
        return self.__cilindrada


    def set_velocidad(self, velocidad):
        self.__velocidad = velocidad


    def set_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada