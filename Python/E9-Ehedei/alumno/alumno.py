class Alumno(object):
    def __init__(self, nombre, nota):
        if(self.__validar_nombre(nombre) and self.__validar_nota(nota)):
            self.nombre = nombre
            self.nota = nota
        else:
            raise Exception('Datos introducidos incorrectos.')


    """
    Getter de la propiedad nombre
    """
    def get_nombre(self):
        return self.nombre


    """
    Getter de la propiedad nota
    """
    def get_nota(self):
        return self.nota


    """
    Setter de la propiedad nombre
    """
    def set_nombre(self, nombre):
        if(self.__validar_nombre(nombre)):
            self.nombre = nombre
        else:
            raise Exception('La longitud del nombre introducido es incorrecta (debe ser entre 1 y 20 caracteres.')


    """
    Setter de la propiedad nota
    """
    def set_nota(self, nota):
        if(self.__validar_nota(nota)):
            self.nota = nota
        else:
            raise Exception('Rango de la nota introducido incorrecto (debe ser entre 0 y 10)')


    """
    Método que valida la longitud de la cadena de nombre, mayor que 0 y menor o igual que 20
    """
    def __validar_nombre(self, nombre):
        valido = True
        if len(nombre) > 20 or len(nombre) == 0:
            valido = False
        return valido


    """
    Método privado que valida que la nota es mayor o igual que 0 y menor o igual que 10
    """
    def __validar_nota(self, nota):
        valido = False
        if nota >= 0 and nota <= 10:
            valido = True
        return valido


    """
    Método que imprime los datos del alumno por consola
    """
    def imprimir_datos(self):
        mensaje = f"Nombre del alumno: {self.get_nombre()}\nNota de la asignatura: {str(self.get_nota())}"
        print('-----------------------------')
        print('Datos del Alumno:')
        print(mensaje)


    """
    Método que imprime la nota del alumno
    """
    def imprimir_nota(self):
        mensaje = f"Nota de la asignatura: {str(self.get_nota())}"
        print('-----------------------------')
        print(mensaje)


    """
    Método que imprime el nombre del alumno
    """
    def imprimir_nombre(self):
        print('-----------------------------')
        mensaje = f"Nombre del alumno: {self.get_nombre()}"
        print(mensaje)