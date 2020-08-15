from coche import *

class Camioneta(Coche):
    def __init__(self, carga=1200, velocidad=60, cilindrada=1600, color='azul', ruedas=6):
        super().__init__(velocidad, cilindrada, color, ruedas)
        self.__carga = carga


    def get_carga(self):
        return self.__carga


    def set_carga(self, carga):
        self.__carga = carga


    def __str__(self):
        return f'{super().__str__()}\nCarga: {self.__carga}'