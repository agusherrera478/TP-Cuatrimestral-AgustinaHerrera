from clases.prestamo import Prestamo

class Biblioteca:

    def __init__(self):
        self.materiales = []
        self.socios = []
        self.prestamos = []

    def agregar_material(self, material):
        self.materiales.append(material)

    def buscar_material(self, titulo):
        return [m for m in self.materiales if titulo.lower() in m.titulo.lower()]

    def materiales_disponibles(self):
        return [m for m in self.materiales if m.disponible]

    def agregar_socio(self, socio):
        self.socios.append(socio)

    def buscar_socio(self, id_socio):
        for s in self.socios:
            if s.id == id_socio:
                return s
        return None

    def registrar_prestamo(self, socio, material, fecha):
        if material.disponible:
            prestamo = Prestamo(len(self.prestamos) + 1, fecha, socio, material, False)
            self.prestamos.append(prestamo)
            material.marcar_prestado()

            return prestamo
        else:
            print(f"Material {material.titulo} no disponible para préstamo")
            
            return None

    def registrar_devolucion(self, prestamo):

        if not prestamo.devolucion:
            prestamo.devolucion = True
            prestamo.material.marcar_devuelto()

            return prestamo

        else:
            print("El préstamo ya fue devuelto.")

            return None

    def prestamos_activos(self):
        return [p for p in self.prestamos if not p.devolucion]