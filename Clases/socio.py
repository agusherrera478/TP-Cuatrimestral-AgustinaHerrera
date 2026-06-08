class Socio(object):

    def __init__(self, dni, nombre, apellido, id_socio):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.id = id_socio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre} Apellido: {self.apellido}, DNI: {self.dni}"
