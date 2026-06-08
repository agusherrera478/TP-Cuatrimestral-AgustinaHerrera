from abc import ABC

class Material(ABC):

    def __init__(self, titulo, editorial, ano):
        self.titulo = titulo
        self.editorial = editorial
        self.ano = ano 
        self.disponible = True

   
    def __str__(self):
        return f"Titulo: {self.titulo}, Editorial: {self.editorial}, Ano: {self.ano}"
        
        
class Libro(Material):
    def __init__(self, titulo, editorial, ano, autor, genero, id_libro):
        super().__init__(titulo, editorial, ano)
        self.autor = autor
        self.genero = genero
        self.id = id_libro
        
class Revista(Material):
    def __init__(self, titulo, editorial, ano, numero, fecha):
        super().__init__(titulo, editorial, ano)
        self.numero = numero
        self.fecha = fecha
        
        
a = Libro("La sirenita","Pececitos", "1999", "Cosme fulanito", "infantil", "465468468")
#print(a)

class Socio(object):

    def __init__(self, dni, nombre, apellido, id_socio):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.id = id_socio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre} Apellido: {self.apellido}, DNI: {self.dni}"
    
b = Socio("42123456", "Agustina", "Herrera",3)
#print(b)
        
class Prestamo(object):

    def __init__(self, id_prestamo, fecha_prestamo, socio, material, devolucion):
        self.id = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.socio = socio
        self.material = material
        self.devolucion = devolucion
    def __str__(self):
        return f"Prestamo N° {self.id} {self.socio} {self.material}" 
    
p = Prestamo(1, "07/06/2026", b, a, False)
print(p)
