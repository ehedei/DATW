class Vehiculo(object):
    def __init__(self, color='blanco', ruedas=0):
        self.__color = color
        self.__ruedas = ruedas


    def get_color(self):
        return self.__color


    def get_ruedas(self):
        return self.__ruedas


    def set_color(self, color):
        self.__color = color


    def set_ruedas(self, ruedas):
        self.__ruedas = ruedas


    def __str__(self):
        return f'Clase: {type(self).__name__}\nColor: {self.__color}\nRuedas: {self.__ruedas}'