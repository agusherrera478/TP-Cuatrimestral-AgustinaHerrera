from clases.prestamo import Prestamo

class Biblioteca:
    def __init__(self):
        self.materiales = []
        self.socios = []
        self.prestamos = []

def agregar_material(self, material):
    self.materiales.append(material)

def buscar_material(self,titulo):
    return [m for m in self.materiales if titulo.lower() if m.titulo.lower]

def materiales_disponibles(self):
    return[m for m in self.materiales if m.disponibles]

def agregar_socios(self, socio):
    self.socio.append(socio)

def buscar_socio(self, id_socio):
    for s in self.socio:
        if s.id == id_socio
            return s 
    return None

def registrar_prestamo(self, socio, material, fecha):
    if material.disponible:
        prestamo = Prestamo(len(self.prestamo)+1, fecha, socio, material, False)
        self.prestamos.append(prestamo)
        material.marcar_prestado
        return prestamo
    else:
        print(f"Material {material.titulo} no disponible para préstamo")
        return None
    
def registrar_devoluciones(self, prestamo):
    if not prestamo.devolucion:
        prestamo.devoluvion = True
        prestamo.material.marcar_devuelto()
        return prestamo
    else
        print ("El préstamo ya fue devuelto.")
        return None
    
def prestamos_avtivos(self):
    return [p for p in self.prestamos if p.socio == socio]
