class Prestamo(object):

    def __init__(self, id_prestamo, fecha_prestamo, socio, material, devolucion):
        self.id = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.socio = socio
        self.material = material
        self.devolucion = devolucion

    def __str__(self):
        estado = "Devuelto" if self.devolucion else "Activo"
        return f"Prestamo N° {self.id} {self.socio} {self.material}" 
