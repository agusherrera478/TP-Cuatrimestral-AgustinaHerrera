from abc import ABC

class Material(object):

    def __init__(self, titulo, editorial, ano, disponible):
        self.titulo = titulo
        self.editorial = editorial
        self.ano = ano 
        self.disponible = disponible

   
    def __str__(self):
        return f"Titulo: {self.titulo}, Editorial: {self.editorial}, Ano: {self.ano}, {self.disponible}"
        
        
class Libro(Material):
    def __init__(self, titulo, editorial, ano, disponible, autor, genero, id_libro):
        super().__init__(titulo, editorial, ano, disponible)
        self.autor = autor
        self.genero = genero
        self.id = id_libro
        
class Revista(Material):
    def __init__(self, titulo, editorial, ano, disponible, numero, fecha):
        super().__init__(titulo, editorial, ano, disponible)
        self.numero = numero
        self.fecha = fecha
        
        
a = Libro("La sirenita","Pececitos", "1999", True, "Cosme fulanito", "infantil", "465468468")
print(a)
        
